# 14 — Global Variant Report (P0-01-D)

Date: 2026-10-14 | Regions covered: AU (primary), NZ, UK, SE/global (IKEA), US (partial), CN (via sibling P0-01-A). Pending: DE/AT primary docs, IT, JP, KR, SEA, ME.

## 1. Structures found in other countries

**UK (TKC, Wren, Finsahome, DIY-Kitchens)** — PAT-018 rigid-carcass system:
- 18mm MFC carcass, cam dowel + cam lock + wooden dowel (+glue on DIY-Kitchens).
- Solid 18mm back on BASE units, inset creating **41mm rear service void** (32mm on appliance/larder); wall units use 8mm back with concealed hangers.
- Wren variant: back slides into grooves in end panels then screwed into base edge at 9mm; corner units add a muntin front post; DIY-Kitchens corner adds a **diagonal rear back panel** (2 groove backs + diagonal member screwed into diagonal edges).
- Centre post (36mm) into pre-drilled top rail on units ≥700mm; 5 legs ≥700mm; legs 150–155mm (vs AU 145).
- Finsahome: pre-routered sides for Gola handleless profiles; drawer units with adjustable back for 450/500mm runners.
- Adjacent units joined through side faces with 30mm screws + cover caps; fillers via L-brackets.

**SE/global (IKEA METOD)** — PAT-015:
- Cam shaft + cam housing + dowels; dense 32mm-system hole grid covering entire side inner faces.
- Thin back (ships folded) slides into grooves = floating capture, no fasteners.
- Metal suspension-rail brackets at top rear corners (rail-hung wall cabs); mandatory anti-tip fixing; base cabs get separate legs/plinth.

**US (DIY literature — JCC, Ana White)** — PAT-019 face-frame system:
- 3/4in plywood; **toekick cut INTO side panels** (integral plinth, no legs); pocket-screw joinery.
- Face frame (1x2 stiles+rails) is a separate assembly **wider than the carcass** (carcass 1/2in narrower than target).
- 1/4in plywood back + nailing strips; 1x4 furring top supports; drawer rail spacing rules.
- Inch units throughout (4x4in toekick, 4-1/2in drawer spacing).

**CN (via P0-01-A DWG corpus)** — PAT-020:
- 18mm panels, minifix 3-in-1 (∅15×11 cam + ∅7×28 bolt); 5mm MDF backs; toe rail (脚条) member rather than legs+kickboard.
- Verified: innerW = W−36; door equal-split (4×394+22 @ W1598); inset door H = H−toe_rail−gap; HOLIKE standard H=2068.
- Sliding-door (趟门) cabinets: mid side panels inset variable (58/95/112, not fixed 110) — distinct sub-topology.

**NZ** — kaboodle NZ docs share all AU patterns (W-70xxx series); NZ-specific: metal-sided drawer hardware in 1-drawer doc.

## 2. Structures matching AU samples

- UK base/wall carcass envelope rules (720H×560D base, 720H×300D wall) match kaboodle dimensions exactly — same market sizing, different joinery/back method.
- NZ kaboodle = identical patterns (same manufacturer system across markets).
- METOD box topology (sides full H, top/bottom between sides) geometrically equals PAT-002 — difference is joinery + back method, not panel relations.

## 3. Dimensional/hardware-only differences (NOT new topology)

- UK leg height 150/155 vs AU 145 — parameter, same pattern role.
- UK 18mm vs AU 16mm panels — thickness parameter.
- kaboodle NZ metal-sided drawers — hardware variant of PAT-011.
- Fingerpull vs standard door — front treatment variant.
- Wren muntin post / DIY-Kitchens diagonal back = corner-unit variants within UK system.

## 4. Genuine assembly-topology differences found

| Difference | Where | vs AU baseline |
|---|---|---|
| Back panel INSET creating 41mm service void | UK TKC | AU overlay/inset backs have no designed service void; changes D semantics (internal depth 501 vs external 560) |
| Groove-inserted back + base-edge screwing | UK Wren, IKEA METOD | AU kaboodle = overlay screwed; Flatpax = overlay nailed |
| Muntin front post / diagonal rear back on corner units | UK | AU corners = L-plan or blind-positioned rectangles, no muntin |
| Centre post REQUIRED ≥700mm in front aperture | UK | AU uses vertical mid divider only in some lines (Flatpax), none in kaboodle bases |
| Integral toekick notch cut in sides | US | AU = separate adjustable legs + kickboard — different base strategy entirely |
| Face frame assembly separate & wider than carcass | US | AU frameless; changes all front-opening dims |
| Toe rail member (脚条) instead of legs | CN | plinth = horizontal board, not point legs |
| Minifix 3-in-1 boring map | CN | functionally same as cam+pin but different boring geometry |
| Thin folded back floating in grooves | IKEA | no fasteners at all on back |
| Stacked boxes between shared end panels | kaboodle AU (also UK tall?) | unique multi-carcass pattern |

## 5. New variants worth parametric branches

Priority for next-phase math:
1. **UK service-void back**: add `void_back` parameter; `internal_depth = D − void − t_back`; void ∈ {41 base, 32 appliance}.
2. **Groove-captured back**: `back.widthX = W − tL − tR + 2·groove_depth`; back.y ∈ grooves.
3. **Integral toekick**: side panel shape becomes non-rectangular (notched outline) — needs polygon-part support, not just bbox.
4. **Face frame**: separate stile/rail sub-assembly + frame/carcass width offset rule.
5. **Centre post rule**: `if W ≥ 700: add post at top rail, 36mm`.
6. **Legs vs toe-rail base options**: `base_system ∈ {legs+kickboard, toe_rail, integral_cutout}`.
7. **Shared-end-panel stacking**: end panel spans H_total; internal boxes positioned with door-type-dependent front offsets.

## 6. Honest coverage statement

Covered with assembly-level evidence: AU (2 flatpack systems + trade guide + vanity install), NZ (kaboodle NZ), UK (4 sources), SE/global IKEA, US (DIY literature only), CN (sibling DWG corpus).
Not covered: DE/AT primary sources, IT, FR, ES, PL, JP, KR, SEA, ME, CA production docs, US production (KCMA/manufacturer) docs.
Blocked: manualslib (403), kogan (robots), diy-kitchens PDF (403 — search text only), Bunnings product CDN partially.
"NOT_FOUND_IN_SEARCHED_SOURCES" ≠ nonexistent — e.g., no AU dove-tail drawer, no German 32mm primary doc yet.
