# 15 — Handoff for Formula Generation (P0-01-D → math agent)

Date: 2026-10-14 | Records: 20 patterns, 36 instances, 38 parts, 30 joints, 32 constraints, 6 param candidates.
Coordinate system & field semantics: see SCHEMA.md. All unknowns are explicit — do NOT guess; resolve via 12_UNKNOWN_AND_CONFLICTS.md.

## 1. Recommended mathematisation order

| Priority | Pattern | Why |
|---|---|---|
| 1 | PAT-001 (kaboodle base) | most instances (10+), all dims nominal, golden-test ready |
| 2 | PAT-002 (kaboodle wall) | same joint system; adds top panel param |
| 3 | PAT-005 (pantry) | = PAT-002 + fixed mid shelf + tall H; tests shared template |
| 4 | PAT-003/004 (L-plan corner) | tests non-rectangular outline support |
| 5 | PAT-011 (drawer box) | small self-contained parametric object |
| 6 | PAT-017 (Flatpax) | second joinery system on same AU dims |
| 7 | PAT-018 (UK rigid) | adds service-void + centre-post rules |
| 8 | PAT-015 (METOD) | groove back + suspension rail + 32mm grid |
| 9 | PAT-019 (US face frame) | frame assembly + integral toekick (polygon parts) |
| 10 | PAT-006 (stacked towers) | multi-carcass composition rules |

## 2. Inputs per pattern

Common: `W, D, H, tL, tR, tTop, tBtm, tBack, unit, dimension_basis`.
Pattern-specific:
- PAT-001: + `legH` (nominal 145), `rail cross-section dims` [UNKNOWN — factory confirm]
- PAT-002/005: + `shelf_count`, `fixed_shelf_z` (PAT-005)
- PAT-003/004: + L-leg extents `Wa, Wb`, corner notch dims [partially UNKNOWN]
- PAT-006: + `unit_heights[]`, `door_type ∈ {melamine, thermoformed}` → front offset 18/20
- PAT-007/010: + appliance opening spec; PAT-010 mid-panel z = site-set (non-parametric)
- PAT-011: + `innerW` (drawer bay), `runner_offset`, drawer wall height
- PAT-015: + `groove_depth`, `back_t (~3-4)`, `rail_bracket positions`
- PAT-017: + `divider` presence/position, back nail spacing
- PAT-018: + `void_back` (41 base / 32 appliance), `centre_post` when W≥700, `leg_count` when W≥700→5
- PAT-019: + `toekick_h×d` (4×4in), `frame_overhang` (frame = carcass+1/2in), `stile/rail widths (2in)`
- PAT-020: + `toe_rail_h`, `gap_total`, door count for equal-split

## 3. Per-panel coordinate definitions (normative shapes)

Rectangular parts → `(dimensions_xyz, position_min_xyz)` as in 05_PARTS.jsonl.
Non-rectangular parts needing outline support:
- L-shaped panels (PAT-003/004 bottom/top/shelf): polygon outline + thickness.
- Side panel with integral toekick (PAT-019): rectangle minus front-bottom notch.
- Diagonal rear back (DIY-Kitchens corner): angled panel, length = L-diagonal.
Local axes convention in parts file records length/width/thickness mapping to world axes.

## 4. Contact/connection relations (joint topology summary)

- `end_into_face`: all horizontal panels into sides (kaboodle/flatpax/METOD/TKC) — the dominant joint class.
- `overlay_face`: AU backs onto rear edges; kickboards onto legs; MW box onto lower cab.
- `floating_capture`: groove backs (METOD, Wren pre-screw, KB-guide variant).
- `pin-supported` (shelves, `+Z` adjust).
- `stacked_between_shared_panels` (PAT-006 boxes↔end panels, 28mm screws).
- `to_wall`: screw-through-back to studs (AU), suspension rail brackets (IKEA), concealed hangers (UK), ≥2 support beams (ADP vanity), anti-tip device (IKEA mandatory).
Connection types: kaboodle = fixed_confirmed face screws; Flatpax/METOD/UK = removable cam systems; drawer/hinge = movable.

## 5. Confirmed constraints (machine-checkable)

In 07_CONSTRAINTS.jsonl — highlights:
- `bottom.widthX = W − tL − tR` (PAT-001/002/005/017)
- `back.widthX = W; back.heightZ = H` (overlay backs only)
- `centre_post required when W≥700` (UK); `legs=5 when W≥700` (UK); AU legs 4→6 by width/corner
- `service void = 41mm base / 32mm appliance` (UK TKC)
- `kickboard setback = 50 (70 pantry)`; `legs nominal 145` AU, `150/155` UK
- `stack front offset = 18 | 20 by door_type`; `MW box 360mm from tower top`
- `end panel protrudes 14mm past front; rear void 20mm` (corner pantry)
- `innerW = W−36` (CN 18mm panels, DWG-verified)
- `door.width = (W − gap_total)/n` equal split (CN: 22mm @ W1598)
- `hinge cup = 35mm; side gap 1–2mm` (AU guide)

## 6. Candidate formulas (see 08_PARAMETER_CANDIDATES.jsonl)

PC-001..006 cover PAT-001/002/005/006/011/015. Extend with:
- `internal_depth = D − void_back − tBack` (PAT-018)
- `back.widthX = W − tL − tR + 2·groove_depth` (groove backs)
- `frame.widthX = carcass.W + 12.7` (US PAT-019)
- `shelf.widthX = W − tL − tR − 2·g_shelf` (g ≈1-2 unknown exact)
- `divider.heightZ = H − tTop − tBtm` (Flatpax vertical divider)

## 7. Applicability conditions

- Formula `bottom.widthX = W−tL−tR` ONLY when horizontals are between sides (all AU flatpack patterns confirmed); INVALID for US face-frame plywood cabs where bottom may span differently — verify per source.
- `back=W×H` ONLY for external overlay; groove/internal backs use different dims.
- Leg/pin/void rules are manufacturer-family constants — expose as parameters with provenance, not global constants.
- Dimension basis must be resolved per source (kaboodle 720H excludes legs & door; CN shop drawings include door in D sometimes — see P0-01-A note "深含门板").

## 8. Supporting vs contradicting instances

- PAT-001 supported: W-51600..06 family (7 widths), CTM, W-70106. Contradicting same-category alternatives: PAT-017 (flatpax), PAT-018 (UK), PAT-019 (US).
- "Solid backs on all cabinets" (prior assumption) CONTRADICTED by oven cab (no back), blind pantry (no back), rangehood (open bottom).
- "Blind corner = special internal structure" contradicted: AU blind = plain carcass + positioning/panel accessories.
- Kaboodle vs Flatpax at SAME 600mm 2-door base size = two real competing topologies — golden pair for variant testing.

## 9. Unknown parameters needing data before final formulas

- kaboodle front rail cross-section; shelf depth setback; hinge boring map; fingerpull rebate dims.
- Flatpax support rail extent/orientation.
- METOD panel thicknesses (assume ~18 side / ~3-4 back — VISUAL_ONLY).
- UK drawer-unit adjustable-back travel range.
- Face-frame production standards (KCMA) — current evidence is DIY literature.
- PAT-020 (CN): deeper hole-position maps exist in DWG corpus (CadEllipse extracted) — mine per-need.

## 10. Golden-test feasibility

Ready now:
- GT-01: kaboodle W-51605, W600 D560 H720 t16 → bottom 568×560; back 600×720; sides 16×560×720.
- GT-02: kaboodle W-51620 wall W200 → top/bottom 168×300.
- GT-03: TKC W600 base → internal depth 560−41−18=501 (matches doc's 501mm internal depth — self-validating!).
- GT-04: CN Yupenghui W1598 → doors 4×394 (DWG-verified).
Blocked/needs data: PAT-001 rail dims; PAT-006 full stack geometry (unit heights present but panel-level dims for each box are nominal only).

Verification harness suggestion: generate parts for GT-01..04, assert bbox sums close to envelope (W = tL + inner + tR etc.), then diff vs these recorded values.
