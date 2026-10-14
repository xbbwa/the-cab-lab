# 10 — Structural Variant Matrix (P0-01-D)

Scope: confirmed from manufacturer assembly docs actually read this run.
"NOT_FOUND_IN_SEARCHED_SOURCES" means absent from the searched corpus — NOT "does not exist".

## A. Carcase topology matrix (box construction)

| Pattern | sides | top | bottom | back | front/top rail | legs | seen in |
|---|---|---|---|---|---|---|---|
| PAT-001 | full H+D | ABSENT | inset between sides | solid external overlay, full W×H | 1 front rail at top | 4-6 adj legs | kaboodle base 150–900, CTM, blind-corner base |
| PAT-002 | full H | inset between sides | inset between sides | solid external overlay | n/a (closed box) | none | kaboodle wall/deep/slimline/medium/fingerpull, MW box |
| PAT-003 | 2, at outer ends of L, full H, **overhang past backs** | L-shape full plan | L-shape | 2 overlay backs (one per leg) | inner-top flat bracket | 5–6 | kaboodle 900 corner base |
| PAT-004 | 2, outer ends of L | L-shape | L-shape | 2 overlay backs | n/a | none | kaboodle 600 corner wall, fingerpull corner wall |
| PAT-005 | full H (2000–2345) | inset | inset | solid overlay | n/a | 4–6 legs | kaboodle pantry/tall pantry single carcass |
| PAT-006 | shared full-height end panels | per stacked box | per stacked box | per box | per box | on lowest box | corner pantry 865+1335, oven towers, MW stack |
| PAT-007 | full H | ABSENT | inset | **ABSENT_CONFIRMED** | 2 full-width support panels (oven shelf positions) | legs | kaboodle oven cab 600/900 |
| PAT-008 | full H (460) | ABSENT (open top) | inset | overlay | 2 front apron rails | 6 legs | kaboodle farmhouse sink cab |
| PAT-009 | full H | inset | inset | overlay | n/a | none (stacker) | kaboodle microwave box |
| PAT-010 | full H | inset | **ABSENT_CONFIRMED (open bottom)** | overlay | n/a | none | kaboodle slideout rangehood cabs |
| PAT-012 | full H | inset | inset | **ABSENT_CONFIRMED** | fixed mid shelf (cam+pin ×8) | 6 legs | kaboodle 1000 blind corner pantry |
| PAT-013 | full H | inset | inset | overlay | fixed mid shelf | none | kaboodle open-shelf W-77932 (cam/dowel build) |
| PAT-015 | full H, 32mm hole grid | inset | inset | **thin board in grooves (floating capture)** | n/a | none (rail hung) | IKEA METOD wall |
| PAT-016 | ends full H | rails (or open) | inset | 4 documented methods | 2 rails (front may be on-edge) | per design | AU training guide generic |

## B. Back-panel variants (all confirmed somewhere in evidence)

| method | where confirmed | dimension effect |
|---|---|---|
| external solid overlay full W×H | kaboodle base/wall/pantry/corner/sink; CFP | back.x = W, back.z = H; adds t_back to depth axis rear |
| internal back (inside width, fixed through sides) | KB guide only (PAT-016) | back.x = W − tL − tR |
| rebated/grooved back | KB guide (PAT-016); IKEA METOD (PAT-015, floating in groove) | back.x ≈ W − tL − tR + 2·groove |
| rail-and-panel (thin board + rear rail) | KB guide only | thin back + separate rear rail part |
| ABSENT | kaboodle oven cab, blind corner pantry, rangehood(open bottom different axis) | removes rear rigidity member |
| thin folded panel in grooves | METOD | floating capture, no fasteners |

## C. Joinery variants

| method | seen in | fixing visibility |
|---|---|---|
| countersunk screw through outer face (50mm carcass, 28mm rails/legs) | kaboodle standard line | visible on outside faces |
| cam+pin + 40mm dowel + glue | kaboodle open shelf (W-77932), blind pantry shelf (cam+pin ×8) | none outside |
| cam shaft + cam housing + dowels | IKEA METOD | none outside |
| mortice-and-tenon + Rafix/Euro screws | Custom Flatpack AU | concealed |
| metal-sided drawer system | kaboodle NZ 1-drawer doc | n/a |

## D. Key numeric rules confirmed

- Base carcass H=720, D=560 (kaboodle), legs 145 nominal → overall ~865+top.
- Wall cab H=720, D=300 (deep 400).
- Fingerpull wall variant: box 20mm shorter + finger-pull rebate.
- Corner base footprint 900×900×560; blind corner base is a straight 1000/984mm carcass positioned blind (no internal blind structure).
- Microwave box → lower cabinet front offset: 18mm melamine / 20mm thermoformed; MW box sits 360mm below tower top.
- Kickboard setback: 50mm standard, 70mm pantry; scribed to uneven floor.
- Wall fixing: ≥8g ×65mm into studs (kaboodle); 75mm studs (CFP); METOD = supplied anti-tip + suspension rail.
- Hinge cup 35mm; finished door side gap ~1–2mm (KB guide).
- Corner pantry: end panels protrude 14mm past front; 20mm rear void needs packing; ≥8 wall fixings.
- Broom-cupboard retrofit shelf in 600 pantry: 1664mm up from inside base, holes 50mm & 498mm back from front edge.

## E. Dimensional-vs-topological dedup verdicts

- All kaboodle straight bases 150–900mm = SAME pattern (PAT-001), width parameter only.
- All kaboodle wall cabs incl. deep/slimline/medium = PAT-002; fingerpull = PAT-002 + height/end-panel rule variant.
- NZ kaboodle docs = same patterns as AU (product-family ≠ country difference). NZ-specific: metal-sided drawer hardware variant.
- METOD vs kaboodle wall = TRUE topology difference (groove back + cam joinery + rail hang vs overlay back + face screws + screw-through to studs).
- CFP = TRUE topology difference (mortice-tenon joinery vs face screws).

## F. Not yet found in searched sources

- Face-frame (US-style) carcass — NOT_FOUND_IN_SEARCHED_SOURCES.
- Top/bottom panels capping side ends (sides between top+bottom) — NOT_FOUND.
- Fixed internal divider full-height in base cab (double-bay) — NOT_FOUND in kaboodle (broom kit adds divider to pantry only).
- Integrated (not separate) kickboard/plinth structural base — NOT_FOUND; all AU evidence uses separate legs+kickboard.
- Drawer box with grooved-in bottom — NOT_FOUND (kaboodle = walls stand on bottom).
