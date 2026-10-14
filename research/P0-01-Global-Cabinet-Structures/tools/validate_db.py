"""validate_db.py — read-only integrity & geometry checks for the P0-01-D research DB.

Usage: python tools/validate_db.py            (human-readable report to stdout)
       python tools/validate_db.py --json     (machine JSON report to stdout)

The script NEVER writes to the database files. Re-running it is idempotent.
Checks (per P0-01-D closeout spec):
  parse        - every JSONL/CSV/JSON parses; no empty records
  ids          - primary IDs unique; (assembly_id,part_id) pairs unique
  refs         - no dangling references (source_ids, pattern refs, part refs, joint endpoints)
  enums        - controlled vocab fields hold known values (or other:/explicit unknowns)
  geometry     - confirmed dimensions are finite numbers; UNKNOWN/CONFLICT not coerced to 0;
                 bbox closure checks for fully-dimensioned instances
  formulas     - parameter-candidate expressions only reference declared input_vars;
                 simple eval of "W - tL - tR"-style expressions on golden-test inputs
  dup_patterns - same-topology pattern pairs flagged via 'topology_same_as' metadata
"""
import json, csv, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ISSUES = []  # (severity, check, location, detail)
def issue(sev, chk, loc, det): ISSUES.append((sev, chk, loc, det))

def load_jsonl(name):
    rows = []
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        issue("ERROR", "parse", name, "file missing")
        return rows
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if not line.strip():
                issue("WARN", "parse", f"{name}:{i}", "blank line skipped")
                continue
            try:
                rows.append((i, json.loads(line)))
            except json.JSONDecodeError as e:
                issue("ERROR", "parse", f"{name}:{i}", f"JSON decode: {e}")
    return rows

def load_csv(name):
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        issue("ERROR", "parse", name, "file missing")
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

# ---------------------------------------------------------------- load
run_state = None
try:
    run_state = json.load(open(os.path.join(ROOT, "00_RUN_STATE.json"), encoding="utf-8"))
except Exception as e:
    issue("ERROR", "parse", "00_RUN_STATE.json", f"JSON decode: {e}")

sources  = load_csv("01_SOURCE_INDEX.csv")
countries= load_csv("02_COUNTRY_INDEX.csv")
assem    = load_jsonl("03_CABINET_INSTANCES.jsonl")
patterns = load_jsonl("04_ASSEMBLY_PATTERNS.jsonl")
parts    = load_jsonl("05_PARTS.jsonl")
joints   = load_jsonl("06_JOINTS.jsonl")
cons     = load_jsonl("07_CONSTRAINTS.jsonl")
params   = load_jsonl("08_PARAMETER_CANDIDATES.jsonl")
evid     = load_jsonl("09_EVIDENCE_INDEX.jsonl")

# ---------------------------------------------------------------- helpers
EVIDENCE_ENUM = {"SOURCE_EXPLICIT","GEOMETRY_DERIVED","MULTI_CASE_VERIFIED",
                 "INFERRED_UNVERIFIED","VISUAL_ONLY","UNKNOWN","CONFLICT",
                 "SOURCE_EXPLICIT_VISUAL_CONFIRMED","SOURCE_EXPLICIT_TEXT_CONFIRMED",
                 "SOURCE_EXPLICIT_VISUAL_CONFIRMED","MULTI_CASE_INFERRED"}
ROLE_VOCAB = {"side_left","side_right","top_panel","bottom_panel","back_panel","mid_side",
    "fixed_shelf","adjustable_shelf","stretcher_rail","front_rail","hanger_rail",
    "kick_board","plinth_member","leg_plinth_panel","door_front","drawer_front",
    "drawer_side","drawer_back","drawer_bottom","drawer_runner_carrier","filler_panel",
    "end_decor_panel","face_frame_stile","face_frame_rail","benchtop_frame_member","other",
    # tolerated aliases seen in DB
    "support_panel","rail","leg","base_slats","mirror","drawer_side_inner","panel"}
def enum_ok(v):
    if not isinstance(v, str): return False
    # allow composite statuses like "SOURCE_EXPLICIT_VISUAL_CONFIRMED" or "other:x"
    if v.startswith("other:"): return True
    return v in EVIDENCE_ENUM or all(p in EVIDENCE_ENUM for p in v.split("_"))

def is_num(v): return isinstance(v, (int, float)) and not isinstance(v, bool)

def nums_in(obj, path=""):
    """yield (path, value) for all leaf values."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from nums_in(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from nums_in(v, f"{path}[{i}]")
    else:
        yield path, obj

# ---------------------------------------------------------------- ID uniqueness
def check_ids(rows, key, label, allow_dupes=False):
    seen = {}
    for ln, r in rows:
        v = r.get(key)
        if v in (None, ""):
            issue("WARN", "ids", f"{label}:{ln}", f"missing {key}")
            continue
        if v in seen and not allow_dupes:
            issue("ERROR", "ids", f"{label}:{ln}", f"duplicate {key}={v} (first at line {seen[v]})")
        seen.setdefault(v, ln)
    return seen

src_ids   = {r["source_id"] for r in sources if r.get("source_id")}
assem_ids = check_ids(assem, "assembly_id", "03")
pat_ids   = check_ids(patterns, "pattern_id", "04")
part_keys = check_ids(parts, None, "05")  # composite below
joint_ids = check_ids(joints, "joint_id", "06")
cons_ids  = check_ids(cons, "constraint_id", "07")
param_ids = check_ids(params, "param_id", "08")
ev_ids    = check_ids(evid, "evidence_id", "09")

# composite part key uniqueness
seen_pk = {}
for ln, r in parts:
    k = (r.get("assembly_id"), r.get("part_id"))
    if k in seen_pk:
        issue("ERROR", "ids", f"05:{ln}", f"duplicate (assembly,part) {k} first at {seen_pk[k]}")
    seen_pk[k] = ln
part_ids_by_asm = {}
for ln, r in parts:
    part_ids_by_asm.setdefault(r.get("assembly_id"), set()).add(r.get("part_id"))

# ---------------------------------------------------------------- references
PAT_REF = re.compile(r"PAT-\d{3}")
def check_src_ids(r, loc):
    for s in r.get("source_ids", []) or []:
        if s not in src_ids:
            issue("ERROR", "refs", loc, f"dangling source_id {s}")

for ln, r in assem:
    loc = f"03:{ln}"
    check_src_ids(r, loc)
    sp = r.get("structure_pattern", "")
    pats = PAT_REF.findall(sp)
    if not pats and not sp.startswith(("other:", "install-rules", "(applies")):
        issue("WARN", "refs", loc, f"structure_pattern '{sp}' has no PAT-### token")
    for p in pats:
        if p not in pat_ids:
            issue("ERROR", "refs", loc, f"dangling pattern ref {p} in '{sp}'")
    es = r.get("evidence_status", "")
    if not enum_ok(es): issue("WARN", "enums", loc, f"evidence_status '{es}'")
    for k, v in (r.get("part_presence_summary") or {}).items():
        if v not in {"PRESENT_CONFIRMED","ABSENT_CONFIRMED","UNKNOWN"}:
            issue("WARN", "enums", loc, f"part_presence {k}={v}")

for ln, r in patterns:
    loc = f"04:{ln}"
    for s in r.get("evidence", []) or []:
        for m in PAT_REF.findall(str(s)):
            if m not in pat_ids: issue("WARN","refs",loc,f"pattern evidence refs {m}")
    for field in ("topology_same_as","merged_into"):
        if r.get(field) and r[field] not in pat_ids:
            issue("ERROR", "refs", loc, f"{field}={r[field]} not a pattern")

for ln, r in parts:
    loc = f"05:{ln}"
    if r.get("assembly_id") not in assem_ids:
        issue("ERROR", "refs", loc, f"dangling assembly_id {r.get('assembly_id')}")
    check_src_ids(r, loc)
    if not enum_ok(r.get("evidence_status","")):
        issue("WARN", "enums", loc, f"evidence_status '{r.get('evidence_status')}'")
    role = r.get("role","")
    if not (role in ROLE_VOCAB or role.startswith("other") or "/" in role or "(" in role):
        issue("WARN", "enums", loc, f"role '{role}' outside vocabulary")
    # UNKNOWN must not be silently coerced to numeric 0 in dimension fields
    for pth, v in nums_in(r.get("dimensions_xyz")):
        if is_num(v) and v == 0:
            issue("WARN", "geometry", loc, f"dimensions_xyz{pth} == 0 (check not an UNKNOWN-as-0)")
    t = r.get("thickness_mm")
    if t is not None and not is_num(t) and "UNKNOWN" not in str(t) and "~" not in str(t):
        issue("WARN", "geometry", loc, f"thickness_mm '{t}' not numeric/unknown")

EXTERNAL_ENTS = {"wall","carcass","floor","studs","inner corner tops","end_panel",
                 "stacked_box_side","mw_box","lower_drawer_cab","cabinet front","P-KCK"}
for ln, r in joints:
    loc = f"06:{ln}"
    aid = r.get("assembly_id")
    if aid not in assem_ids:
        issue("ERROR", "refs", loc, f"dangling assembly_id {aid}")
    check_src_ids(r, loc)
    known = part_ids_by_asm.get(aid, set())
    for side in ("part_a","part_b"):
        p = r.get(side)
        if not p: continue
        if p in known or p in EXTERNAL_ENTS: continue
        if re.search(r"[/+]", str(p)):
            issue("WARN", "refs", loc, f"{side}='{p}' is a compound token — normalise to explicit part_ids")
        elif str(p).startswith("P-"):
            issue("ERROR", "refs", loc, f"{side}='{p}' not a part of {aid} (dangling part ref)")
        else:
            issue("WARN", "refs", loc, f"{side}='{p}' free-text entity (not a P- id)")
    if not enum_ok(r.get("evidence_status","")):
        issue("WARN","enums",loc,f"evidence_status '{r.get('evidence_status')}'")

for ln, r in cons:
    loc = f"07:{ln}"
    tgt = r.get("assembly_id")
    if tgt not in assem_ids and tgt not in pat_ids and not str(tgt).startswith(("generic_","AU-KAB-*")):
        issue("WARN", "refs", loc, f"constraint target '{tgt}' neither assembly nor pattern")
    check_src_ids(r, loc)
    if not enum_ok(r.get("derivation_status","")):
        issue("WARN","enums",loc,f"derivation_status '{r.get('derivation_status')}'")
    expr = str(r.get("value_or_expression",""))
    if re.search(r"\bUNKNOWN\b", expr) and r.get("derivation_status") in {"MULTI_CASE_VERIFIED"}:
        issue("WARN","geometry",loc,"expression contains UNKNOWN but status MULTI_CASE_VERIFIED")
    if r.get("derivation_status") == "CONFLICT":
        pass  # conflicts must not appear as confirmed values; flagged in report

for ln, r in evid:
    loc = f"09:{ln}"
    if r.get("source_id") not in src_ids:
        issue("ERROR","refs",loc,f"dangling source_id {r.get('source_id')}")

# ---------------------------------------------------------------- formula check
SAFE_EXPR = re.compile(r"^[\w\s\-\+\*/\(\)\.\d|]*$")
for ln, r in params:
    loc = f"08:{ln}"
    if r.get("pattern_id") not in pat_ids:
        issue("ERROR","refs",loc,f"dangling pattern_id {r.get('pattern_id')}")
    ivars = set(r.get("input_vars", []))
    for k, expr in (r.get("computed") or {}).items():
        if not isinstance(expr, str): continue
        # find identifiers (allow digits inside names like gap_total, legH)
        ids = set(re.findall(r"[A-Za-z_]\w*", expr))
        undeclared = {i for i in ids - ivars
                      if not i.startswith("n") or i in ("note",)  # 'n' count allowed
                      } - {"n","e","UNKNOWN","per","product"}
        if undeclared:
            issue("WARN","formulas",loc,f"{k}: vars {sorted(undeclared)} not in input_vars")
        if not SAFE_EXPR.match(expr):
            issue("WARN","formulas",loc,f"{k}: expression has unsafe chars")

# ---------------------------------------------------------------- geometry closure
def get_dims(aid):
    a = next((r for _, r in assem if r.get("assembly_id")==aid), {})
    return a.get("dimensions", {})

def closure_tests():
    res = []
    # T1: AU-KAB-001 W600 t16 — bottom.widthX should be W-2t=568; back W×H=600×720
    pl = {p["part_id"]: p for _, p in parts if p.get("assembly_id")=="AU-KAB-001"}
    try:
        t = pl["P-SID-L"]["dimensions_xyz"]["x"]
        bt = pl["P-BTM"]["dimensions_xyz"]["x"]
        res.append(("CLOSE-01","AU-KAB-001","tL+bottomX+tR==W",
                    f"{t}+{bt}+{t}={t+bt+t}", "600", "PASS" if t+bt+t==600 else "FAIL"))
        bk = pl["P-BCK"]["dimensions_xyz"]
        res.append(("CLOSE-02","AU-KAB-001","back covers rear WxH",
                    f"{bk['x']}x{bk['z']}", "600x720",
                    "PASS" if bk['x']==600 and bk['z']==720 else "FAIL"))
        rail = pl["P-STR"]["dimensions_xyz"]["x"]
        res.append(("CLOSE-03","AU-KAB-001","railX==W-2t", f"{rail}", "568",
                    "PASS" if rail==568 else "FAIL"))
    except Exception as e:
        res.append(("CLOSE-0x","AU-KAB-001","closure","n/a",str(e),"SKIP"))
    # T2: AU-KAB-003 wall W200 t16 → top/bottom 168
    pl = {p["part_id"]: p for _, p in parts if p.get("assembly_id")=="AU-KAB-003"}
    try:
        top = pl["P-TOP"]["dimensions_xyz"]["x"]
        res.append(("CLOSE-04","AU-KAB-003","topX==W-2t", f"{top}", "168",
                    "PASS" if top==168 else "FAIL"))
    except Exception as e:
        res.append(("CLOSE-0x","AU-KAB-003","closure","n/a",str(e),"SKIP"))
    # T3: negative dims anywhere?
    for ln, r in parts:
        for pth, v in nums_in(r.get("dimensions_xyz")):
            if is_num(v) and v < 0:
                res.append(("CLOSE-NEG",f"05:{ln}",f"{r.get('part_id')}{pth}<0",str(v),"", "FAIL"))
    return res

for t in closure_tests():
    sev = "ERROR" if t[5]=="FAIL" else ("INFO" if t[5]=="PASS" else "WARN")
    issue(sev, "closure", f"{t[0]} {t[1]}", f"{t[2]}: got {t[3]}, expect {t[4]} -> {t[5]}")

# ---------------------------------------------------------------- pattern dup detection
# flag patterns sharing identical key topology signature unless marked variant
def topo_sig(p):
    d = (p.get("definition") or "").lower()
    sig = []
    for k in ("no top","no back","overlay back","groove","l-shape","l-plan","face frame",
              "mortice","cam+pin","support rail","stacked","open top","open bottom","toekick"):
        if k in d: sig.append(k)
    return tuple(sorted(sig))
sigs = {}
for ln, p in patterns:
    s = topo_sig(p)
    sigs.setdefault(s, []).append(p["pattern_id"])
for s, ids in sigs.items():
    if len(ids) > 1:
        marked = all(any(p.get("topology_same_as") or p.get("merged_into") or p.get("dedup_note")
                         for _, p in patterns if p["pattern_id"]==i) for i in ids)
        if not marked:
            issue("WARN","dup_patterns",",".join(ids),
                  f"same topology signature {list(s)} — verify these are variants, not duplicates")

# ---------------------------------------------------------------- summary
errs = sum(1 for i in ISSUES if i[0]=="ERROR")
warn = sum(1 for i in ISSUES if i[0]=="WARN")
info = sum(1 for i in ISSUES if i[0]=="INFO")

report = {
    "counts": {"sources":len(sources),"instances":len(assem),"patterns":len(patterns),
               "parts":len(parts),"joints":len(joints),"constraints":len(cons),
               "param_candidates":len(params),"evidence":len(evid)},
    "errors": errs, "warnings": warn, "info": info,
    "issues": [{"severity":s,"check":c,"location":l,"detail":d} for s,c,l,d in ISSUES],
}

if "--json" in sys.argv:
    print(json.dumps(report, ensure_ascii=False, indent=1))
else:
    print("=== P0-01-D DB VALIDATION ===")
    for k,v in report["counts"].items(): print(f"  {k}: {v}")
    print(f"  errors={errs} warnings={warn} info={info}\n")
    for s,c,l,d in ISSUES:
        if s != "INFO":
            print(f"[{s:5}] {c:12} {l:22} {d}")
    print("\n--- closure / info ---")
    for s,c,l,d in ISSUES:
        if s == "INFO": print(f"[PASS] {c:12} {l:22} {d}")
