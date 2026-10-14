# 12 — Unknowns, Conflicts, Gaps (P0-01-D)

## Explicit UNKNOWNs (do not guess downstream)

1. **Kaboodle front support rail cross-section** (PAT-001): rail depth (Y) and height (Z) not dimensioned in W-51605 doc. Known: spans inner width, sits at top-front. Needed: cut-list dimension → flag factory-confirmation.
2. **Kaboodle back-panel edge registration**: overlay back is flush with outer side edges or overhangs? Render suggests flush to outer envelope. CONFIRM.
3. **Adjustable shelf depth/setback**: shelves are partial-depth but exact Y not stated in any doc scanned.
4. **Kaboodle panel thickness**: 16mm asserted family-wide (P0-01-B + 28/50mm screw lengths consistent), but per-panel t not printed in assembly text → mark MULTI_CASE_INFERRED.
5. **Corner base bracket position & L-bottom notch dims**: bracket exists; exact dims UNKNOWN.
6. **Pantry fixed-shelf z-position** for each SKU (broom kit gives 1664mm on 600 only).
7. **METOD back panel groove depth / exact panel thicknesses (~18mm sides, ~3–4mm back)**: visual only, not dimensioned.
8. **METOD side-panel depth** (370mm nominal per IKEA catalog — needs source confirmation).
9. **Blind corner pantry rear**: NO back panel in parts list — but does it rely on wall for racking? Confirm with W-70116 diagram re-check.
10. **Drawer runner positions/boring pattern**: not dimensioned in assembly docs (runner brackets only).
11. **Hinge hole boring positions on sides** (corner pantry gives 132/222, 116/227 refs — per-product constants, not system rule).
12. **Fingerpull rebate profile dimensions**.
13. **CFP mortice-tenon geometry** (tenon size/location): described qualitatively only.
14. **Which kaboodle panels are edge-banded and where**: not stated per-part.

## Conflicts / things to resolve

- P0-01-B pattern table claimed "16mm solid backs" across kaboodle — W-70116 blind pantry and W-51609 oven cab are counter-examples (NO back). Baseline corrected here.
- Earlier assumption "kaboodle top panel": standard base has NO top panel (front rail only). Wall cabs DO have top panel. Distinguish by category.
- NZ 1-drawer doc shows metal-sided drawers vs order guide "timber drawers standard" — market/hardware variant, record both.

## Coverage gaps (for next phases)

- No AU wardrobe-specific carcass doc yet (CFP covers generic/wardrobe claim; need dedicated wardrobe source).
- No AU vanity/laundry-specific carcass doc (kaboodle laundry exists? not in queue).
- UK/US/EU sources not yet mined (phase 4).
- Bunnings CDN docs partially robots-blocked; manualslib 403; kogan robots deny.
- IKEA METOD base/high cab doc (a53333c8) not yet visually inspected beyond warnings pages.
- Corner WALL cabinet door-opening face: front L-notch orientation needs second render to confirm door arrangement.

## Access restrictions encountered

- manualslib.com: HTTP 403 → skipped.
- kogan.com: robots deny → skipped.
- wallbeds.com.au: 403 on fetch.py; partial via webfetch.
- a.storyblok.com / cdn domains: public, fetched with rate limiting.
