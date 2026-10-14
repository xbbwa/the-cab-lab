# 13 — Australian Cabinet Assembly Structure Baseline (P0-01-D)

Date: 2026-10-14 | Evidence basis: 44 sources, 92 manufacturer PDFs fetched, 20 assembly pages visually verified by render, plus sibling-project cross-refs (KB training guide = SRC-D-0028, Custom Flatpack = SRC-D-0029, CN DWG = SRC-D-0043).

IMPORTANT: nothing below is presented as "the" Australian standard. Two distinct flatpack construction systems are confirmed coexisting (kaboodle face-screw system vs Flatpax cam+pin+thin-back system), plus a third system (Custom Flatpack mortice-tenon) and imported products (IKEA METOD).

## 1. Confirmed cabinet structures in AU public material

| Category | Confirmed structures (pattern → instances) |
|---|---|
| C01 base cabinet | PAT-001 (kaboodle rail-top base, W-51600..06); PAT-017 (Flatpax cam+pin, mid divider); PAT-014 (CFP mortice-tenon) |
| C02 drawer base | PAT-001 carcass + PAT-011 timber drawer box (kaboodle W-51611-16); Flatpax drawer cupboards; NZ metal-sided drawer variant |
| C03 wall cabinet | PAT-002 (kaboodle inset top/bottom + overlay back); Flatpax wall cupboards (nailed 3mm back); METOD PAT-015 (groove back + suspension rail) |
| C04 tall/pantry | PAT-005 single tall carcass w/ fixed mid shelf; PAT-006 two-piece stack (corner pantry 865+1335); Flatpax tall cupboard |
| C05 wardrobe | PAT-017 family covers cupboards; dedicated robe evidence still thin (Flatpax wall/floor units used in robes; Stegbar BIR08 tower documented in P0-01-B) |
| C06 bathroom/vanity | ADP install rules (support beams, plumbing cutouts); Mocka vanity bolt+locknut construction |
| C07 laundry | Flatpax linen chute cupboard; broom cupboards; ADP floor-mount rules |
| C08 corner | PAT-003 L-plan corner base (kaboodle); PAT-004 L-plan corner wall; Flatpax blind-corner rectangle + blind panel; kaboodle blind units = straight carcass positioned blind |
| C09 appliance | PAT-007 oven base (no back/top, 2 support panels); PAT-009 microwave box; PAT-010 rangehood (open bottom, site-set shelf); PAT-006 oven tower (stacked boxes + shared end panels) |
| C10 open | PAT-013 open shelf (cam+pin+dowel, no visible fixings) |
| C11 multi-cabinet | PAT-006 stacking with shared end panels; adjacent-unit clamp+screw joining; kickboard/scribe rules |
| C12 special | fingerpull variant (20mm rebate); slimline/deep wall depth variants; pullout basket interiors |

## 2. Panel composition per structure

- **PAT-001 base**: side L/R (full H,D) + bottom (inset) + solid overlay back (full W×H) + front top support rail + adjustable legs + partial-depth adjustable shelf. NO top panel.
- **PAT-002 wall**: side L/R + top + bottom (both inset) + overlay back + adjustable shelf.
- **PAT-003 corner base**: L-shaped bottom + 2 overlay backs + 2 sides (overhang past backs = built-in wall rebate) + inner-top flat bracket + 5-6 legs + L-shelf.
- **PAT-005 pantry**: sides full H + top + bottom + FIXED mid shelf (structural) + overlay back + legs + adjustable shelves.
- **PAT-007 oven base**: sides + bottom + 2 horizontal support panels (oven shelf positions) + legs. ABSENT: back, top.
- **PAT-008 farmhouse sink**: sides + bottom + overlay back + front apron rails (open top).
- **PAT-011 drawer box**: full-footprint bottom floor + 4 walls standing on it; side walls overlap front/back ends.
- **PAT-017 Flatpax**: sides + bottom (cam+pin) + fixed vertical mid divider + support rail(s) + 3mm nailed thin back + feet 145mm.
- **PAT-012 blind pantry**: sides + top + bottom + fixed shelf (cam+pin) + shelves + legs. ABSENT: back.
- **PAT-015 METOD**: sides + top + bottom (cam+dowel) + thin folded back in grooves + suspension rail brackets.
- **PAT-014 CFP**: panels with integral mortice-tenon edges + Rafix/Euro screws; kickboards scribed to feet.

## 3. Relative placement (all per SCHEMA coordinate system)

- Kaboodle convention: side panels span full carcass height and depth; horizontal members (bottom, top, rails, shelves, support panels) are trapped BETWEEN sides → `horiz.widthX = W − tL − tR`. Overlay back covers entire rear face → `back.x = W, back.z = H`, sitting at y = D…D+t.
- Front top rail sits at top-front between sides (benchtop fixing); rail cross-section dims not published (UNKNOWN).
- Corner units: L-plan; the two "sides" are only the outer ends of the L; sides are deeper than the back position so the cabinet self-rebates for out-of-square walls.
- Two-piece stacks (PAT-006): separate carcasses share full-height end panels; box fronts sit 18mm (melamine) or 20mm (thermoformed) behind end-panel fronts.
- Flatpax: vertical mid divider (not horizontal shelf) between sides via cam+pin; 3mm back nailed flush over rear; same 145mm feet convention as kaboodle.
- Drawer box: bottom = full footprint floor at z=0 of the drawer box; all four walls stand ON it.

## 4. Explicitly confirmed connection methods

| Joint | Method (evidence) |
|---|---|
| side↔bottom/top (kaboodle) | 50mm countersunk wood screws through outer side faces into panel ends; countersunk holes identify outer faces |
| back↔sides/bottom (kaboodle) | 50mm screws through back face into rear edges — overlay_face |
| rail↔sides (kaboodle) | 28mm screws |
| legs↔bottom | leg screws (kaboodle 4-6 legs; flatpax feet into pre-drilled holes, "face outwards") |
| kickboard↔legs | 28mm screws through leg backs; setback 50mm (70mm pantry); scribed to floor |
| adjacent cabinets | level, clamp, pre-drill, screw together (kaboodle); CFP cabinet connectors |
| wall fixing | ≥8-gauge ×65mm screws into studs (kaboodle); CFP 75mm; ADP ≥2 support beams for vanities |
| Flatpax carcass | cam+pin ×26-48; 1-inch nails ×20-40 + 14mm screws for 3mm back |
| kaboodle premium/open | cam+pin + 40mm dowel + glue (8mm dowel holes); face-screw option only when hidden |
| METOD | cam shaft 112996 + cam housing 113434 + dowels; back floats in grooves; suspension-rail brackets; mandatory anti-tip |
| CFP | mortice-and-tenon + Rafix + Euro/chipboard screws |

## 5. Dimensions determined by overall dims + thickness

Confirmed derivable (see 07_CONSTRAINTS.jsonl):
- `bottom.widthX = W − tL − tR` (all inset-horizontals patterns)
- `back.widthX = W`, `back.heightZ = H` (external overlay backs only)
- `sides.z = H`, `sides.y = D` (full-height sides)
- `rail.widthX = W − tL − tR`; `fixed_shelf.widthX = W − tL − tR`
- door `width ≈ W − 2·gap` (full overlay, gap ~1–2mm per KB guide)
- Golden-test values: W600 base → bottom 568; W200 wall → top 168 (t=16)

## 6. Constraints needing extra conditions

- Leg count: 4 base / 5-6 wide or corner (kaboodle ≥900, corner, farmhouse 6; UK rule ≥700 → 5 legs).
- Back panel method must be selected before sizing (overlay vs internal vs groove vs absent change back dims AND depth semantics).
- Blind "corner" units: AU practice = rectangular carcass positioned blind (kaboodle) or rectangle + blind panel + fillers (Flatpax); the L-plan corner (PAT-003) is a different real topology — do not merge.
- Appliance units: opening dims driven by appliance spec; rangehood inner panel site-drilled (not factory dimensioned).
- Stacking offsets are door-material-dependent (18/20mm).
- Kickboard setback differs base (50) vs pantry (70).

## 7. Patterns sharing a parametric template

- All kaboodle straight bases 150–900 + CTM + blind-corner base = PAT-001 (W parameter only).
- All kaboodle wall cabs incl deep/slimline/medium/fingerpull = PAT-002 (+depth/height params; fingerpull adds rebate rule).
- PAT-001⊂PAT-005 (pantry = same joint system + fixed mid shelf + tall H).
- Flatpax family all share PAT-017 (cam+pin + divider + nailed back), varying divider count and feet.
- METOD wall/base share PAT-015 (cam+dowel+groove back).

## 8. Independent variants (cannot merge)

- PAT-001 vs PAT-002 differ (top panel presence) — separate branches.
- PAT-003/004 L-plan — separate.
- PAT-007/008/010 open-back/open-top/open-bottom appliance variants — separate.
- PAT-006 stacked+shared-end-panels — separate.
- PAT-014 mortice-tenon, PAT-017 cam+pin+nailed-back, PAT-015 cam+dowel+groove back, PAT-019 US face-frame+integral toekick — all genuinely different topology/joinery.

## 9. Evidence sufficient for formula derivation

Sufficient (multi-doc + rendered): PAT-001, 002, 003, 005, 006, 007, 011, 013, 015, 017, 018.
Partial (text only / one doc): PAT-008, 009, 010, 012, 014, 016, 019, 020 (020 has strongest evidence via DWG).

## 10. Needs manufacturer/customer confirmation

- kaboodle rail cross-section dims; shelf depth offsets; hinge boring map per SKU; fingerpull rebate profile; edge-banding spec per panel.
- Flatpax support rail orientation/extent (back rail vertical vs horizontal interpretation — visually ambiguous in renders).
- Blind corner pantry (W-70116) racking support without back.
- Any AU production (non-flatpack) manufacturer's boring maps — all evidence so far is flatpack; custom-shop practice via KB guide only.
