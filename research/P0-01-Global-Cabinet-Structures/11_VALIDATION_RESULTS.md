# 11 — Validation Results (P0-01-D)

## Dimensional closure checks performed

| Test | Pattern | Check | Result |
|---|---|---|---|
| VT-01 | PAT-001 | W600 base: tL+inner+tR = 16+568+16 = 600 | PASS (render + parts list consistent) |
| VT-02 | PAT-002 | W200 wall: top.widthX = 200−32 = 168 | PASS (derived, consistent with drawing) |
| VT-03 | PAT-018 (TKC) | internal depth = D − void − tBack = 560−41−18 = 501 | PASS — doc states "Internal depth: 501mm (base units)" — SELF-VALIDATING CROSS-CHECK |
| VT-04 | PAT-018 | appliance/larder: 560−32−... → doc internal 519 = 560−32−9? back 9mm? | PARTIAL — doc says 519mm internal w/ 32 void → implies back ~9mm on appliance/larder (8mm wall back consistent) — recorded as derived |
| VT-05 | PAT-006 | corner pantry 865+1335 = 2200 total | PASS (doc explicit) |
| VT-06 | PAT-020 (CN) | innerW = W−36 on boards 36/37/73 | PASS (DWG-verified, sibling) |
| VT-07 | PAT-001 part count | render shows 1 rail (front); screws 29×50mm+19×28mm ≈ joint counts | PASS (qualitative) |

## Parameter variation checks

- W=800 on PAT-001 → bottom predicted 768: formula-consistent, but NOT independently verified against a factory drawing → flagged GEOMETRY_DERIVED, not production-verified.

## Counter-example checks

- "All cabinets have solid backs" — REFUTED: PAT-007 (no back), PAT-012 (no back), PAT-010 (open bottom), PAT-015/018 (groove/inset void backs).
- "Blind corner needs special carcass" — REFUTED for AU: kaboodle blind = straight carcass; Flatpax adds accessory panel only.
- Face-frame assumption for US — CONFIRMED in DIY literature (PAT-019); production-standard source still missing.

## Assembly-sequence constraints captured

- Corner pantry: adjustable shelf must be inserted BEFORE final side panel (ordering constraint).
- Wren: cam locks hand-tighten only after back panel positioned (ordering).
- kaboodle: leg height set to 145 before standing unit; kickboard after cabinets levelled.
- METOD: back slides into grooves before cam tightening? (VISUAL — order inferred from drawing sequence, mark INFERRED).

## Golden tests nominated

GT-01..04 defined in 15_HANDOFF §10 (kaboodle base/wall, TKC base, CN doors).
