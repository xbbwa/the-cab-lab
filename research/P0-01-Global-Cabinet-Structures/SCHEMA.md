# SCHEMA — P0-01-D Global Cabinet Assembly Structures

Version: 1.0 | Units: mm unless stated | Coordinate system per section 7 of task spec.

## World coordinate system (all instances normalised to this)

- Origin O: outer bounding box, left-front-bottom corner.
- +X: left -> right (width W)
- +Y: front -> back (depth D)
- +Z: bottom -> top (height H)
- Cabinet front faces -Y direction (observer at -Y looking toward +Y).

## Dimension basis vocabulary (`dimension_basis`)

- `carcass_only` — box without doors/drawer fronts, without legs/plinth height
- `carcass_with_legs` — includes leg/plinth height
- `overall_with_fronts` — includes door/drawer front thickness in depth
- `cut_part` — factory cut size of a single panel
- `nominal_product` — marketing size (may include rounding)
- `unknown` — basis not stated in source (record, do not guess)

## ID scheme

- `source_id`: `SRC-D-####` (sequential, in 01_SOURCE_INDEX.csv)
- `assembly_id`: `<REGION>-<MAKER>-<NNN>` e.g. `AU-KAB-001`
- `pattern_id`: `PAT-<NNN>`
- `part_id`: `P-<ROLE>` inside an assembly, e.g. `P-SID-L`, `P-TOP`, `P-BTM`, `P-BCK`, `P-DIV`, `P-SHF-F`, `P-SHF-A`, `P-STR`, `P-DRF`, `P-DWR-S`, `P-DWR-F`, `P-DWR-B`, `P-DWR-BTM`, `P-KCK`, `P-FIL`, `P-END-DEC`, `P-FRM-*` (face frame), `P-HGR` (hanger/rail)
- `joint_id`: `J-<assembly>-<NNN>`
- `constraint_id`: `C-<assembly>-<NNN>`
- `param_id`: `PC-<NNN>`

## Part `role` vocabulary (controlled)

side_left, side_right, top_panel, bottom_panel, back_panel, mid_side (divider),
fixed_shelf, adjustable_shelf, stretcher_rail (horizontal rail, partial depth/width),
front_rail, hanger_rail (wall-cabinet structural rail), kick_board, plinth_member,
leg_plinth_panel, door_front, drawer_front, drawer_side, drawer_back, drawer_bottom,
drawer_runner_carrier (metal drawer side), filler_panel, end_decor_panel,
face_frame_stile, face_frame_rail, benchtop_frame_member, other (specify in notes)

## Part `presence` / evidence_status enums

part presence: `PRESENT_CONFIRMED` | `ABSENT_CONFIRMED` | `UNKNOWN`

evidence_status (part/joint): `SOURCE_EXPLICIT` | `GEOMETRY_DERIVED` | `MULTI_CASE_VERIFIED` | `INFERRED_UNVERIFIED` | `VISUAL_ONLY` | `UNKNOWN` | `CONFLICT`

derivation_status (constraint/param): same enum.

## Joint `joint_topology` vocabulary

- `butt_contact` — flat face against flat face/end
- `end_into_face` — panel end bears on face of perpendicular panel
- `dado_groove` — panel end/edge seated in groove across grain direction of other
- `rebate_rabbet` — seated in L-shaped edge rebate
- `mitre` — angled faces
- `overlay_face` — face-on-face contact (e.g. back panel nailed on outside)
- `edge_band_abut` — edge-to-edge co-planar
- `floating_capture` — panel captured in grooves on 2-4 sides (thin back in groove)
- `unknown` | `other:<desc>`

## Joint `connection_type` vocabulary

`fixed_confirmed` (documented fasteners/dowels/cams/glue), `fixed_assumed`,
`removable` (knock-down fittings), `movable` (hinge/slide), `adjacent_unfixed`,
`unknown`. Hardware goes in `hardware_refs` as free refs to source text.

## JSONL files

### 03_CABINET_INSTANCES.jsonl (assembly record)
```json
{"assembly_id":"AU-KAB-001","region":"AU","manufacturer":"kaboodle (DIY Resolutions/Bunnings)","product":"600mm 1 drawer base cabinet","category":"C02","structure_pattern":"PAT-001","dimensions":{"W":600,"D":null,"H":null,"unit":"mm","dimension_basis":"nominal_product"},"part_presence_summary":{"top_panel":"PRESENT_CONFIRMED","mid_side":"ABSENT_CONFIRMED"},"source_ids":["SRC-D-####"],"evidence_status":"SOURCE_EXPLICIT","notes":""}
```

### 05_PARTS.jsonl
```json
{"part_id":"P-SID-L","assembly_id":"AU-KAB-001","role":"side_left","quantity":1,"material_ref":"16mm melamine PB (per product family)","thickness_mm":16,"dimensions_xyz":{"x":16,"y":null,"z":null},"position_min_xyz":{"x":0,"y":0,"z":0},"local_axes":{"length":"+Z","width":"+Y","thickness":"+X"},"position_basis":"derived_from_topology","evidence_status":"GEOMETRY_DERIVED","source_ids":[],"notes":""}
```

### 06_JOINTS.jsonl
```json
{"joint_id":"J-AU-KAB-001-01","assembly_id":"AU-KAB-001","part_a":"P-SID-L","part_b":"P-BTM","joint_topology":"end_into_face","connection_type":"removable","contact_face_a":"inner_face","contact_face_b":"left_end","hardware_refs":["cam+pin","28mm screws (kit)"],"machining_features":"pre-drilled holes; countersunk holes face outwards","assembly_direction":"+X/-X","source_ids":[],"evidence_status":"SOURCE_EXPLICIT","notes":""}
```

### 07_CONSTRAINTS.jsonl
```json
{"constraint_id":"C-AU-KAB-001-01","assembly_id":"AU-KAB-001","subject":"P-BTM","property":"dimensions_xyz.x","relation":"equals","value_or_expression":"W - tL - tR","depends_on":["W","tL","tR"],"conditions":["side_panels_full_height","bottom_between_sides"],"derivation_status":"GEOMETRY_DERIVED","source_ids":[],"notes":""}
```

### 08_PARAMETER_CANDIDATES.jsonl
```json
{"param_id":"PC-001","pattern_id":"PAT-001","input_vars":["W","D","H","tL","tR","tTop","tBtm","tBack","legH"],"computed":{"bottom.widthX":"W - tL - tR"},"condition_branch":"back_panel_solid_full","evidence":"MULTI_CASE_VERIFIED","counter_cases":[],"golden_test_refs":[]}
```

### 09_EVIDENCE_INDEX.jsonl
```json
{"evidence_id":"EV-0001","source_id":"SRC-D-####","locator":"PDF p.2 'assembling cabinet'","what_it_proves":"bottom panel + sides joined by cam/pin; countersunk holes outward","snapshot_file":"raw_snapshots/...","text_file":"evidence_text/...","accessed_at":"2026-10-13","reliability":"manufacturer_doc"}
```

## Structure pattern naming

`<side_extent>_<topbottom_relation>_<back_method>[_<modifier>]`

e.g. `full_height_sides_inset_top_bottom_solid_back`, `sides_between_top_bottom_thin_overlay_back`.

Pattern identity test (sec 13): a pattern differs if any of {panel set, which panels span full envelope, which are trapped between, back mounting, shared vs independent panels, joint topology affecting dimension formulas} differs.
