# -*- coding: utf-8 -*-
# build_records.py — emit machine-readable structural records from verified evidence.
# Every instance/pattern entry below is backed by a fetched PDF/text/render or a
# sibling-project source (cross-referenced as B:S###). Nothing here is invented;
# unknowns are marked UNKNOWN per SCHEMA.md.

import json, csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def w(name, obj):
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8', newline='') as f:
        if name.endswith('.jsonl'):
            for r in obj:
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
        else:
            f.write(obj)
    print('wrote', name, len(obj) if isinstance(obj, list) else 'md')

# ---------------- SOURCES ----------------
SOURCES = [
    # source_id, url, publisher, doc, region, snapshot/text/render locator
    ("SRC-D-0001","https://kaboodle.com.au/assembly-library/cabinets","kaboodle (Bunnings/DIY Resolutions)","assembly library index page","AU","raw_snapshots/kaboodle_com_au__*.html"),
    ("SRC-D-0002","https://a.storyblok.com/f/188515/x/3d5c1f4124/1-kbau_kit_order_guide_26_e17_v_5_lr.pdf","kaboodle","AU kit order guide 38pp (dimension matrix)","AU","raw_snapshots/a_storyblok_com__2cb020914d0947f6.pdf"),
    ("SRC-D-0003","https://a.storyblok.com/f/188515/x/0dab14c967/kaboodle-flat-pack-kitchens-600mm-base-cabinet-instructions.pdf","kaboodle","600mm base cabinet W-51605 assembly","AU","snap a_storyblok_com__0e4dc19e1e1c6a83; render p2"),
    ("SRC-D-0004","https://a.storyblok.com/f/188515/x/b3f9f64694/kaboodle-flat-pack-kitchens-200mm-wall-cabinet-instructions.pdf","kaboodle","200mm wall cabinet W-51620 assembly","AU","snap a_storyblok_com__f1939afbad8b45d6; render p2"),
    ("SRC-D-0005","https://a.storyblok.com/f/188515/x/ed0b72e0ac/kb_kit_w-51624-600mediumwallcabinet-instruct-v-1-4-lr.pdf","kaboodle","600mm medium wall cabinet W-51624","AU","snap a_storyblok_com__cec1d2da*/text"),
    ("SRC-D-0006","https://a.storyblok.com/f/188515/x/8d04b109c3/kaboodle-flat-pack-kitchens-900mm-corner-base-cabinet-instructions.pdf","kaboodle","900mm corner base W-51608 assembly","AU","snap a_storyblok_com__089e1dcfb8ccd4f3; render p2"),
    ("SRC-D-0007","https://a.storyblok.com/f/188515/x/c716333a6e/kaboodle-flat-pack-kitchens-600mm-corner-wall-cabinet-instructions.pdf","kaboodle","600mm corner wall W-51627 assembly","AU","snap a_storyblok_com__5265e75adfc462d4; render p2"),
    ("SRC-D-0008","https://a.storyblok.com/f/188515/x/e736124079/kaboodle-flat-pack-kitchens-600mm-3-drawer-base-cabinet-instructions.pdf","kaboodle","600mm 3-drawer base W-51615 assembly","AU","snap a_storyblok_com__907f2c4e26d5816d; render p2 (drawer box construction)"),
    ("SRC-D-0009","https://a.storyblok.com/f/188515/x/84562382db/kb_kit_inst_w-51609_600_oven_cab-v11-lr.pdf","kaboodle","600mm oven cabinet W-51609 assembly","AU","snap a_storyblok_com__2c5f1ba312d9f91d; render p2"),
    ("SRC-D-0010","https://a.storyblok.com/f/188515/x/7bc598b7d1/kb_kit_inst_w-51610_900_oven_cab-v11-lr.pdf","kaboodle","900mm oven cabinet W-51610 assembly","AU","snap/text (width variant of W-51609)"),
    ("SRC-D-0011","https://a.storyblok.com/f/188515/x/135f5be71d/kaboodle-flat-pack-kitchens-600mm-pantry-instructions.pdf","kaboodle","600mm pantry W-51633 assembly","AU","snap a_storyblok_com__4d53d00b3722ac85; render p2"),
    ("SRC-D-0012","https://a.storyblok.com/f/188515/x/66314e375a/kaboodle-flat-pack-kitchens-corner-pantry-cabinet-instructions.pdf","kaboodle","corner pantry cabinet (two-piece stack) assembly","AU","snap a_storyblok_com__815c5e2c336a4706 (also in P0-01-B evidence)"),
    ("SRC-D-0013","https://a.storyblok.com/f/188515/x/17b294de17/kb_kit_w-51896_2345h_1000mm-tall-blind-corner-pantry-v-1-5-lr.pdf","kaboodle","1000mm tall blind corner pantry W-51896 (2345H)","AU","snap/text"),
    ("SRC-D-0014","https://a.storyblok.com/f/188515/x/ba2078548b/kbnz_kit_w-70106_1000_blind_cnr_bc-v9_2.pdf","kaboodle NZ","1000mm blind corner base W-70106 assembly (NZ)","NZ","snap a_storyblok_com__21fe07e38e7c92c7; render p2"),
    ("SRC-D-0015","https://a.storyblok.com/f/188515/x/d7b4c60486/kaboodle-flat-pack-kitchens-blind-corner-pantry-cabinet-instructions.pdf","kaboodle","blind corner pantry W-70116 assembly","AU/NZ","snap a_storyblok_com__34ef7bab3bc6354c; render p2; text shows NO back panel + cam+pin x8"),
    ("SRC-D-0016","https://a.storyblok.com/f/188515/x/3921102902/kaboodle-flat-pack-kitchens-600mm-1-drawer-base-cabinet-instructions.pdf","kaboodle","600mm 1-drawer base W-51611 (290H)","AU","snap a_storyblok_com__1c8ef854b09a7e25"),
    ("SRC-D-0017","https://a.storyblok.com/f/188515/x/2ef5348fc5/kaboodle-flat-pack-kitchens-600mm-1-drawer-base-cabinet-instructions-assembly-nz.pdf","kaboodle NZ","600mm 1-drawer base NZ (metal-sided drawer)","NZ","text; metal drawer sides variant"),
    ("SRC-D-0018","https://a.storyblok.com/f/188515/x/63108ac007/kaboodle-flat-pack-kitchens-890mm-high-oven-tower-instructions.pdf","kaboodle","890mm-high oven tower (stacked cabs between end panels)","AU","snap a_storyblok_com__8dbd9653d03d0169; render p2"),
    ("SRC-D-0019","https://a.storyblok.com/f/188515/x/5d05a59347/kaboodle-flat-pack-kitchens-600mm-high-oven-tower-instructions-nz.pdf","kaboodle NZ","600mm high oven tower NZ (same stack topology)","NZ","snap a_storyblok_com__8dbd9653d03d0169"),
    ("SRC-D-0020","https://a.storyblok.com/f/188515/x/2a2d9a68cd/kaboodle-flat-pack-kitchens-microwave-box.pdf","kaboodle","microwave box assembly (closed box stacking unit)","AU","snap a_storyblok_com__a01495b7068d4467; render p2"),
    ("SRC-D-0021","https://a.storyblok.com/f/188515/x/9ef08b3512/w-51628_600mm_slideout_rangehood_cabinet_ins_v_1-2_lr.pdf","kaboodle","600mm slideout rangehood cabinet W-51628","AU","snap a_storyblok_com__361d1727a0131b1c; render p2"),
    ("SRC-D-0022","https://a.storyblok.com/f/188515/x/347d9aff32/kb-anz-kit-ins-w-77932-openshelf-fixedshelves-v1-lr.pdf","kaboodle","open shelf fixed-shelf cabinet W-77932 (dowel/cam AND screw variants)","AU","snap a_storyblok_com__1705924f67895dec; render p2"),
    ("SRC-D-0023","https://a.storyblok.com/f/188515/x/a626f56163/kb_kit_ctm-cabinets_inst_v_2.pdf","kaboodle","CTM customisable cabinets inst","AU","snap a_storyblok_com__972555fb523d6a0b; render p2"),
    ("SRC-D-0024","https://a.storyblok.com/f/188515/x/d63be68728/kaboodle-flat-pack-kitchens-attaching-kickboards-instructions.pdf","kaboodle","attaching kickboards (50mm setback / 70mm pantry)","AU","snap a_storyblok_com__ef29e6646d5a5e18; render p2"),
    ("SRC-D-0025","https://a.storyblok.com/f/188515/x/8535a5178b/w-51899_600mm_pantry-broom-cupboard-kit-ins-v-1-7-lr.pdf","kaboodle","600mm pantry broom cupboard kit W-51899 (internal divider retrofit)","AU","snap a_storyblok_com__1eb47473ca7e6064; render p2"),
    ("SRC-D-0026","farmhouse sink cabinet instructions (kaboodle storyblok)","kaboodle","600mm farmhouse sink cabinet W-79959 (460H, open top)","AU","snap a_storyblok_com__7107b2402339c42d; render p2"),
    ("SRC-D-0027","kaboodle order guide NZ (1-kbnz_kit_order_guide_26-e14)","kaboodle NZ","NZ kit order guide","NZ","snap a_storyblok_com__ee41618da5"),
    ("SRC-D-0028","B:S001","Commonwealth of Australia (Workspace Training)","Cabinetmaking learner guide 64pp — carcase/back/joinery reference","AU","P0-01-Australia-Research/09_EVIDENCE/www_kbcabinetmaking_com_au__2fec4ffc7ee24631.txt"),
    ("SRC-D-0029","customflatpack.com.au assembly pdf","Custom Flatpack Australia","16pp assembly — mortice-and-tenon + Rafix connectors","AU","P0-01-B evidence customflatpack_com_au__dc082db7a441716e.txt"),
    ("SRC-D-0030","https://www.ikea.com/... METOD wall cabinet assembly pdf","IKEA","METOD wall cabinet assembly (image-only, rendered)","SE/global","snap www_ikea_com__9a2ff823d34641d0; renders p7-p10"),
    ("SRC-D-0031","https://www.ikea.com/... METOD base/high cabinet assembly pdf","IKEA","METOD second assembly doc","SE/global","snap www_ikea_com__a53333c82813f290"),
    ("SRC-D-0032","kaboodle various width-family PDFs (150-900 base/wall/drawer, slimline, deep, fingerpull, wine rack, pullout baskets, handle template)","kaboodle","dimensional family members of PAT-001/002 — enumerated in logs/pdf_queue_all.txt (77 urls)","AU","raw_snapshots/a_storyblok_com__*"),
]

with open(os.path.join(ROOT,'01_SOURCE_INDEX.csv'),'w',encoding='utf-8',newline='') as f:
    c=csv.writer(f); c.writerow(['source_id','url_or_ref','publisher','document','region','local_locator'])
    c.writerows(SOURCES)
print('wrote 01_SOURCE_INDEX.csv', len(SOURCES))

with open(os.path.join(ROOT,'02_COUNTRY_INDEX.csv'),'w',encoding='utf-8',newline='') as f:
    c=csv.writer(f); c.writerow(['region','sources','status','notes'])
    c.writerows([
        ('AU','SRC-D-0001..0029, 0032 (kaboodle AU + CFP + KB guide)','PRIMARY_BASELINE','flatpack frameless, face-screw + cam variants'),
        ('NZ','SRC-D-0014,0015,0017,0019,0027 (kbnz_* docs)','COVERED','kaboodle NZ shares AU patterns; metal-sided drawers appear in NZ 1-drawer doc'),
        ('SE/global','SRC-D-0030,0031 (IKEA METOD)','COVERED_PARTIAL','METOD sold in AU but documented globally; cam+dowel+groove-back system'),
        ('UK','none yet','PENDING','phase4'),
        ('DE/AT','none yet','PENDING','32mm system evidence via METOD side-hole grid (partial)'),
        ('US/CA','none yet','PENDING','face-frame target'),
        ('CN/JP','none yet','PENDING','P0-01-A CAD catalog cross-ref possible'),
    ])
print('wrote 02_COUNTRY_INDEX.csv')

# ---------------- PATTERNS ----------------
PATTERNS = [
 {"pattern_id":"PAT-001","name":"full_height_sides_inset_bottom_no_top_panel_solid_overlay_back_front_top_rail",
  "family":"base_cabinet","origin":"kaboodle AU flatpack","frame":"frameless",
  "definition":"Sides span full carcass H and D. Bottom panel trapped between sides at z=0..tBtm. NO full top panel — a single front support rail spans between sides at the top-front. Back panel = solid board overlaying the full rear face (W x H), screwed through its face into rear edges of sides/bottom. Adjustable legs under bottom. Adjustable shelf(es) on pins inside.",
  "key_roles":["side_left","side_right","bottom_panel","back_panel","stretcher_rail(front top)","leg_plinth_panel(legs)","adjustable_shelf","kick_board(separate)"],
  "joinery":"50mm wood screws through outer faces of back/sides/bottom (countersunk, holes face outwards); 28mm screws for rail & legs",
  "instances":["W-51600..51606 bases 150-900mm","W-70106 1000 blind corner base NZ","CTM custom cabinets","farmhouse differs (PAT-008)"],
  "evidence":["SRC-D-0003 render p2","SRC-D-0023 render p2","SRC-D-0014 render p2","SRC-D-0028 p44-45 (generic rail variant)"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-002","name":"full_height_sides_inset_top_bottom_solid_overlay_back",
  "family":"wall_cabinet / closed box","origin":"kaboodle AU flatpack","frame":"frameless",
  "definition":"Sides full H. Top and bottom panels trapped between sides. Solid back = full-size external overlay panel screwed into rear edges. Adjustable shelf on pins. No legs. Wall-fixed through back/top region into studs (>=8g 65mm screws).",
  "key_roles":["side_left","side_right","top_panel","bottom_panel","back_panel","adjustable_shelf"],
  "joinery":"50mm screws through side faces into top/bottom ends; back screwed through face",
  "instances":["W-51620..51627 wall family 150-900mm","deep wall 400D","slimline ~reduced D","medium wall","fingerpull (20mm lower box + finger-pull rebate)","microwave box (PAT-009 is same topology used as stacker)"],
  "evidence":["SRC-D-0004 render p2","SRC-D-0005","SRC-D-0020 render p2"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-003","name":"L_plan_corner_base_L_bottom_two_overlay_backs_two_sides",
  "family":"corner_base_cabinet","origin":"kaboodle AU","frame":"frameless",
  "definition":"L-shaped plan. L-shaped bottom panel. Two full-height back panels (one per leg, external overlay). Two full-height side panels at the outer ends; sides are DEEPER than the back position — they overhang past the backs (self-rebating for uneven walls, per doc). Flat bracket ties the inner top corner. 5-6 adjustable legs.",
  "key_roles":["side_left","side_right","back_panel x2","bottom_panel(L)","flat_bracket(inner top corner)","adjustable_shelf(L)","leg x5+"],
  "joinery":"50mm screws through outer faces; 28mm for legs/bracket",
  "instances":["W-51608 900mm corner base (720x900x900x560)"],
  "evidence":["SRC-D-0006 render p2 + text 'side panels will overhang from the back panels'"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-004","name":"L_plan_corner_wall_L_top_L_bottom_two_overlay_backs_two_sides",
  "family":"corner_wall_cabinet","origin":"kaboodle AU","frame":"frameless",
  "definition":"L-shaped plan. L-shaped top and bottom panels. Two overlay backs. Two side panels at outer ends of the L. L-shaped adjustable shelf on pins. Front V-notch opening for corner doors.",
  "key_roles":["side x2","top_panel(L)","bottom_panel(L)","back_panel x2","adjustable_shelf(L)"],
  "joinery":"50mm screws through faces",
  "instances":["W-51627 600mm corner wall","W-51908 fingerpull corner wall"],
  "evidence":["SRC-D-0007 render p2"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-005","name":"full_height_sides_inset_top_bottom_fixed_mid_shelf_solid_back_tall",
  "family":"pantry / tall cabinet (single carcass)","origin":"kaboodle AU","frame":"frameless",
  "definition":"Sides full H (2000-2345). Top & bottom trapped between sides. One FIXED structural shelf spanning between sides at mid height (cam+pin or screw). Solid overlay back. Adjustable legs. Multiple adjustable shelves on pins.",
  "key_roles":["side_left","side_right","top_panel","bottom_panel","fixed_shelf","back_panel","adjustable_shelf xN","leg x4-6"],
  "joinery":"50mm screws; fixed shelf via cam+pin (8x in blind pantry) or screws",
  "instances":["W-51633 600 pantry","W-51866 450 tall pantry 2345H","W-51890 600 tall pantry","W-51893 900 tall pantry","W-51632 450 pantry","W-51899 broom cupboard retrofit adds upper divider"],
  "evidence":["SRC-D-0011 render p2","SRC-D-0025"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-006","name":"two_carcass_stack / stacked_boxes_between_shared_end_panels",
  "family":"corner pantry / oven tower","origin":"kaboodle AU/NZ","frame":"frameless",
  "definition":"Tall unit formed from separate carcass boxes stacked vertically, with full-height decorative/structural end panels spanning the column sides (or, for corner pantry, a base unit 865H + top unit 1335H each with own panels). Boxes screwed to end panels via 28mm screws. Front setback of boxes vs end panels is door-type dependent (18mm melamine / 20mm thermoformed).",
  "key_roles":["end_panel x2 (full column height)","stacked carcass boxes (each a PAT-001/002-like box)","fixed shelf in top unit","back panels per box"],
  "joinery":"28mm screws box->end panel",
  "instances":["corner pantry (base 865 + top 1335)","890mm-high oven tower","600mm high oven tower NZ","underbench MW stack (MW box on 1-drawer cab, 18/20mm front offset)"],
  "evidence":["SRC-D-0018 render p2","SRC-D-0012","SRC-D-0020 render p2"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-007","name":"full_height_sides_inset_bottom_no_back_no_top_2_support_panels",
  "family":"oven_base_cabinet","origin":"kaboodle AU","frame":"frameless",
  "definition":"Sides full H. Bottom between sides. TWO full-width horizontal support panels between sides (one mid-height = oven shelf, one higher forming top of opening). NO back panel (open rear for ventilation/cabling). NO top panel. Adjustable legs. Oven cleats on sides.",
  "key_roles":["side_left","side_right","bottom_panel","support_panel x2","back_panel=ABSENT_CONFIRMED","top_panel=ABSENT_CONFIRMED","legs","oven cleats"],
  "joinery":"50mm screws through side faces",
  "instances":["W-51609 600 oven cab","W-51610 900 oven cab"],
  "evidence":["SRC-D-0009 render p2 (no back/top labels; support panel x2)"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-008","name":"open_top_sink_cabinet_front_apron_rails",
  "family":"sink_base_cabinet","origin":"kaboodle AU","frame":"frameless",
  "definition":"Sides full H (460H farmhouse unit). Bottom trapped between sides (assembled upside-down, screwed up through bottom). Solid overlay back. OPEN TOP — farmhouse/apron sink sits on the box. Front has horizontal apron rails top and mid forming the apron-sink opening. 6 legs.",
  "key_roles":["side x2","bottom_panel","back_panel","front_rail x2","leg x6"],
  "instances":["W-79959 600 farmhouse sink cab"],
  "evidence":["SRC-D-0026 render p2"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-009","name":"closed_5panel_box_stacking_microwave",
  "family":"microwave/underbench appliance box","origin":"kaboodle AU","frame":"frameless",
  "definition":"Closed rectangular box: 2 sides full H, top & bottom inset, solid overlay back, open front. Designed to stack on top of a base/drawer cabinet; front alignment offset vs lower cabinet is door-type dependent (18mm melamine / 20mm thermoformed), fixed with 28mm screws.",
  "key_roles":["side x2","top_panel","bottom_panel","back_panel"],
  "joinery":"50mm screws faces + 28mm to lower cab",
  "instances":["600mm microwave box"],
  "evidence":["SRC-D-0020 render p2"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-010","name":"open_bottom_rangehood_field_position_shelf",
  "family":"rangehood_cabinet","origin":"kaboodle AU","frame":"frameless",
  "definition":"Sides full H, top inset, solid overlay back. NO bottom (open for slide-out rangehood). One full-width interior panel whose height is SET ON SITE by drilling (position depends on rangehood brand) — not factory-fixed.",
  "key_roles":["side x2","top_panel","back_panel","adjustable-height interior panel (site-drilled)","bottom=ABSENT_CONFIRMED"],
  "instances":["W-51628 600 slideout rangehood","W-51888 600 medium rangehood","W-51636/51889 900 rangehood"],
  "evidence":["SRC-D-0021 render p2"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-011","name":"drawer_box_walls_stand_on_full_bottom_screwed_through_sides",
  "family":"drawer_box (timber)","origin":"kaboodle AU","frame":"n/a",
  "definition":"Drawer bottom panel = full footprint floor. Front, back and the two side panels STAND ON TOP of the bottom panel (bottom underlaps all four walls). Walls joined: screws through side panels into front/back ENDS; screws up through bottom into wall bottom edges. 14mm drawer screws + 28/50mm kit screws. (NZ 1-drawer doc: metal-sided drawer system instead — hardware variant.)",
  "key_roles":["drawer_bottom","drawer_front(inner)","drawer_back","drawer_side x2"],
  "instances":["all W-5161x timber drawer cabs"],
  "evidence":["SRC-D-0008 render p2"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-012","name":"tube_no_back_blind_corner_pantry",
  "family":"blind corner pantry","origin":"kaboodle NZ/AU","frame":"frameless",
  "definition":"Rectangular tall tube: sides full H, top & bottom inset, ONE fixed mid shelf via cam+pin x8, adjustable shelves, 6 legs. NO back panel in parts list (blind section sits against wall/in corner).",
  "key_roles":["side x2","top","bottom","fixed_shelf","back_panel=ABSENT_CONFIRMED","adjustable shelves","legs"],
  "instances":["W-70116 1000 blind corner pantry"],
  "evidence":["SRC-D-0015 render p2 + text parts list (no back panel, cam+pin x8)"],
  "status":"SOURCE_EXPLICIT_TEXT_CONFIRMED"},
 {"pattern_id":"PAT-013","name":"dowel_cam_pin_joinery_closed_box_fixed_shelf",
  "family":"open shelf / display cabinet","origin":"kaboodle AU (premium joinery option)","frame":"frameless",
  "definition":"Same box topology as PAT-002 but joined by cam-and-pin + 40mm dowels + glue (8mm dowel holes; pins screwed into side panels; cams seated in horizontal panels) leaving NO visible fixings. Doc also permits plain 50mm screw assembly only if installed between cabinets/walls. Solid overlay back screwed on.",
  "key_roles":["side x2","top","bottom","fixed_shelf","back_panel"],
  "instances":["W-77932 open shelf fixed shelves"],
  "evidence":["SRC-D-0022 render p2"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-014","name":"mortice_and_tenon_flatpack_rafix",
  "family":"generic cabinet","origin":"Custom Flatpack Australia","frame":"frameless",
  "definition":"Panel edges carry integral tenons locating into mortices in the mating panel (self-aligning carcase); Rafix/concealed connectors + Euro screws + chipboard screws; cabinet connectors between adjacent carcasses; adjustable legs + scribed kickboards; hanging rail brackets for wall cabs; end panels fixed from inside with 28mm screws; wall cabs fixed to studs 75mm screws.",
  "key_roles":["side","top","bottom","back (per product)","kick_board","end_decor_panel","legs","hanging rail bracket"],
  "instances":["Custom Flatpack AU kitchen/wardrobe flatpacks"],
  "evidence":["SRC-D-0029"],
  "status":"SOURCE_EXPLICIT_TEXT_CONFIRMED (no exploded diagram captured)"},
 {"pattern_id":"PAT-015","name":"full_height_sides_inset_top_bottom_cam_dowel_groove_thin_back_suspension_rail",
  "family":"wall cabinet (European 32mm system)","origin":"IKEA METOD (global, sold in AU)","frame":"frameless",
  "definition":"Sides full H with full pre-drilled 32mm-system hole grids on inner faces. Top & bottom between sides, joined by cam shaft (112996) + cam housing (113434) + dowels (101351) — no through-face screws. Thin flexible back panel (ships folded) slides into grooves milled in top/bottom/side inner faces = floating_capture back. Metal suspension-rail brackets inside top rear corners (rail mounting, not direct screw-through).",
  "key_roles":["side x2","top","bottom","back_panel(thin, grooved)","suspension bracket x2","adj shelf pins"],
  "instances":["METOD wall 30/40/60/80cm"],
  "evidence":["SRC-D-0030 renders p7-p9"],
  "status":"SOURCE_EXPLICIT_VISUAL_CONFIRMED"},
 {"pattern_id":"PAT-016","name":"training_guide_generic_floor_cabinet_back_variants",
  "family":"generic AU cabinetmaking reference","origin":"Commonwealth/Workspace Training AU","frame":"frameless modular",
  "definition":"Reference structure: back + base + 2 ends + 2 rails (front rail may be on-edge for sink clearance). Documents FOUR back methods as AU practice: (a) external overlay back full W x H; (b) internal back cut to inside width fixed through sides; (c) rebated back into grooves; (d) rail-and-panel (thin board in grooves + rear rail). Corner unit = same topology doubled: two backs + two front rails.",
  "key_roles":["ends x2","base","rails x2","back (4 methods)"],
  "instances":["generic teaching model"],
  "evidence":["SRC-D-0028 pp44-45"],
  "status":"SOURCE_EXPLICIT_TEXT_CONFIRMED"},
]
w('04_ASSEMBLY_PATTERNS.jsonl', PATTERNS)

# ---------------- ASSEMBLY INSTANCES ----------------
I = [
 ("AU-KAB-001","AU","kaboodle","600mm base cabinet W-51605","C01","PAT-001",{"W":600,"D":560,"H":720,"unit":"mm","dimension_basis":"carcass_only(720H excl legs; 560D excl door)"},["SRC-D-0003"],"SOURCE_EXPLICIT","sides full H; bottom inset; overlay back; front top rail; 4 legs 145mm; adj shelf"),
 ("AU-KAB-002","AU","kaboodle","base cabinet family 150-900mm (W-51600/01/02/03/04/06, 450 1dr1door, pullout bases)","C01/C02","PAT-001",{"W":"150-900","D":560,"H":720,"unit":"mm","dimension_basis":"carcass_only"},["SRC-D-0032"],"SOURCE_EXPLICIT","width variants of PAT-001; pullout bases = same carcass + basket hardware"),
 ("AU-KAB-003","AU","kaboodle","200mm wall cabinet W-51620","C03","PAT-002",{"W":200,"D":300,"H":720,"unit":"mm","dimension_basis":"carcass_only"},["SRC-D-0004"],"SOURCE_EXPLICIT","sides full H; top+bottom inset; overlay back; 1 adj shelf"),
 ("AU-KAB-004","AU","kaboodle","wall cabinet family (300/400/450/600/800/900; deep 400D; slimline; medium; fingerpull)","C03","PAT-002",{"W":"300-900","D":"300/400/slim","H":720,"unit":"mm","dimension_basis":"carcass_only; fingerpull box 20mm shorter + rebate"},["SRC-D-0005","SRC-D-0032"],"SOURCE_EXPLICIT","same topology; dimensional variants"),
 ("AU-KAB-005","AU","kaboodle","900mm corner base cabinet W-51608","C08","PAT-003",{"W":900,"D":560,"H":720,"unit":"mm","dimension_basis":"L-plan 900x900x560"},"SRC-D-0006".split(),"SOURCE_EXPLICIT","L-bottom, 2 backs, 2 sides overhanging backs, inner-top flat bracket, 5 legs, L shelf"),
 ("AU-KAB-006","AU","kaboodle","600mm corner wall cabinet W-51627 (+W-51908 fingerpull)","C08","PAT-004",{"W":600,"D":300,"H":720,"unit":"mm","dimension_basis":"L-plan"},"SRC-D-0007".split(),"SOURCE_EXPLICIT","L-top+L-bottom, 2 backs, 2 sides, L shelf"),
 ("AU-KAB-007","AU","kaboodle","600mm pantry W-51633 / 450 pantry W-51632","C04","PAT-005",{"W":600,"D":560,"H":"~2000","unit":"mm","dimension_basis":"carcass_only"},["SRC-D-0011"],"SOURCE_EXPLICIT","single tall carcass; fixed mid shelf; overlay back; legs; adj shelves"),
 ("AU-KAB-008","AU","kaboodle","tall pantry family W-51866(450)/W-51890(600)/W-51893(900) 2345H","C04","PAT-005",{"W":"450-900","D":560,"H":2345,"unit":"mm","dimension_basis":"carcass_only"},["SRC-D-0013"],"SOURCE_EXPLICIT","2345H single carcass"),
 ("AU-KAB-009","AU","kaboodle","corner pantry (base unit 865 + top unit 1335)","C04/C08","PAT-006",{"W":"corner","H":2200,"unit":"mm","dimension_basis":"two stacked carcasses"},["SRC-D-0012"],"SOURCE_EXPLICIT","two-piece stack; adj shelf must go in before last side panel; 20mm rear void after end panels; >=8 wall fixings"),
 ("AU-KAB-010","AU","kaboodle","890mm-high oven tower / 600mm NZ oven tower","C09/C11","PAT-006",{"W":600,"H":"890/tall","unit":"mm","dimension_basis":"stacked boxes between 2 end panels"},["SRC-D-0018","SRC-D-0019"],"SOURCE_EXPLICIT","2 drawer cabs + MW box + slimline cab sandwiched between full-height end panels; box front setback 18/20mm by door type; MW box 360mm from top"),
 ("AU-KAB-011","AU","kaboodle","600mm oven cabinet W-51609 / 900mm W-51610","C09","PAT-007",{"W":600,"D":560,"H":720,"unit":"mm","dimension_basis":"carcass_only"},["SRC-D-0009","SRC-D-0010"],"SOURCE_EXPLICIT","no back, no top; 2 support panels; legs; oven cleats"),
 ("AU-KAB-012","AU","kaboodle","600mm farmhouse sink cabinet W-79959","C06/C01","PAT-008",{"W":600,"D":560,"H":460,"unit":"mm","dimension_basis":"carcass_only"},["SRC-D-0026"],"SOURCE_EXPLICIT","open top; front apron rails; overlay back; 6 legs"),
 ("AU-KAB-013","AU","kaboodle","600mm microwave box","C09","PAT-009",{"W":600,"unit":"mm","dimension_basis":"box"},["SRC-D-0020"],"SOURCE_EXPLICIT","closed box; stacks on 1-drawer cab with 18/20mm front offset"),
 ("AU-KAB-014","AU","kaboodle","600mm slideout rangehood cabinet W-51628 (+51888/51636/51889)","C09","PAT-010",{"W":600,"D":300,"H":"~350-450","unit":"mm"},["SRC-D-0021"],"SOURCE_EXPLICIT","open bottom; site-positioned middle shelf"),
 ("AU-KAB-015","AU","kaboodle","timber drawer box (inside W-51611-51616 drawer bases)","C02-sub","PAT-011",{"unit":"mm","dimension_basis":"drawer box"},["SRC-D-0008"],"SOURCE_EXPLICIT","walls stand on full bottom; screws through sides into front/back ends + up through bottom"),
 ("AU-KAB-016","NZ","kaboodle NZ","1000mm blind corner base W-70106","C08","PAT-001",{"W":1000,"D":560,"H":720,"unit":"mm"},["SRC-D-0014"],"SOURCE_EXPLICIT","identical carcass to straight base; 'blind' by placement, not internal structure"),
 ("AU-KAB-017","AU/NZ","kaboodle","1000mm blind corner pantry W-70116","C08/C04","PAT-012",{"W":1000,"H":"~2000+","unit":"mm"},["SRC-D-0015"],"SOURCE_EXPLICIT","tube: sides/top/bottom/fixed shelf(cam+pin x8); NO back panel; 6 legs"),
 ("AU-KAB-018","AU","kaboodle","open shelf fixed-shelf cabinet W-77932","C10","PAT-013",{"unit":"mm","dimension_basis":"box"},["SRC-D-0022"],"SOURCE_EXPLICIT","cam+pin+dowel+glue option OR face screws; overlay back"),
 ("AU-KAB-019","AU","kaboodle","CTM customisable cabinets","C01/C03","PAT-001/PAT-002",{"unit":"mm"},["SRC-D-0023"],"SOURCE_EXPLICIT","customisable line uses same base/wall carcass patterns"),
 ("AU-KAB-020","AU","kaboodle","600mm 1-drawer base W-51611 (290H) / NZ metal-side drawer variant","C02","PAT-001+PAT-011",{"W":600,"D":560,"H":290,"unit":"mm"},["SRC-D-0016","SRC-D-0017"],"SOURCE_EXPLICIT","short carcass + 1 drawer; NZ doc uses metal-sided drawer runners"),
 ("AU-KAB-021","AU","kaboodle","kickboard/plinth subsystem","C01-attach","(applies PAT-001/003/005)",{"unit":"mm"},["SRC-D-0024"],"SOURCE_EXPLICIT","kickboard screwed to leg backs 28mm; setback 50mm from cabinet front (70mm on pantries); scribed to floor"),
 ("AU-CFP-001","AU","Custom Flatpack Australia","flatpack cabinets (kitchen/wardrobe)","C01-C05","PAT-014",{"unit":"mm"},["SRC-D-0029"],"SOURCE_EXPLICIT","mortice-and-tenon self-aligning panels; Rafix; hanging rail brackets; scribed kickboards to legs; wall cabs to studs 75mm screws"),
 ("SE-IKE-001","SE/global","IKEA","METOD wall cabinet 30/40/60/80cm","C03","PAT-015",{"W":"300-800","unit":"mm"},["SRC-D-0030"],"SOURCE_EXPLICIT","cam+dowel; grooved thin back; suspension rail brackets; 32mm hole grid in sides"),
 ("AU-KBG-001","AU","Commonwealth/Workspace Training","generic modular floor cabinet + 4 back methods","C01-ref","PAT-016",{"unit":"mm"},["SRC-D-0028"],"SOURCE_EXPLICIT","teaching reference for back variants incl. internal/rebated/rail-and-panel"),
]

w('03_CABINET_INSTANCES.jsonl', [
 {"assembly_id":a,"region":r,"manufacturer":m,"product":p,"category":c,"structure_pattern":pat,
  "dimensions":d,"source_ids":s,"evidence_status":e,"notes":n}
 for (a,r,m,p,c,pat,d,s,e,n) in I])

# ---------------- PARTS (representative assemblies only) ----------------
# helper for compact part dicts
def P(pid,asm,role,q,t,dims,pos,axes,status,src,notes=""):
    return {"part_id":pid,"assembly_id":asm,"role":role,"quantity":q,"material_ref":"16mm HMR/melamine PB (kaboodle)" if 'KAB' in asm else "per source",
            "thickness_mm":t,"dimensions_xyz":dims,"position_min_xyz":pos,"local_axes":axes,
            "position_basis":"derived_from_topology+render","evidence_status":status,"source_ids":src,"notes":notes}

parts=[]
# AU-KAB-001 600 base (W=600 D=560 H=720 t=16 legs=145)
A="AU-KAB-001"; s3=["SRC-D-0003"]
parts+= [
 P("P-SID-L",A,"side_left",1,16,{"x":16,"y":560,"z":720},{"x":0,"y":0,"z":0},{"length":"+Z","width":"+Y","thickness":"+X"},"SOURCE_EXPLICIT",s3,"full-height full-depth; shelf-pin hole rows on inner face"),
 P("P-SID-R",A,"side_right",1,16,{"x":16,"y":560,"z":720},{"x":584,"y":0,"z":0},{"length":"+Z","width":"+Y","thickness":"+X"},"SOURCE_EXPLICIT",s3,""),
 P("P-BTM",A,"bottom_panel",1,16,{"x":568,"y":560,"z":16},{"x":16,"y":0,"z":0},{"length":"+X","width":"+Y","thickness":"+Z"},"SOURCE_EXPLICIT",s3,"between sides, front edge flush with side fronts"),
 P("P-BCK",A,"back_panel",1,16,{"x":600,"y":16,"z":720},{"x":0,"y":560,"z":0},{"length":"+Z","width":"+X","thickness":"+Y"},"SOURCE_EXPLICIT",s3,"external overlay covering full rear; screwed through its face into rear edges of sides+bottom"),
 P("P-STR",A,"stretcher_rail",1,16,{"x":568,"y":"~100-150 UNKNOWN","z":"~100-150 UNKNOWN"},{"x":16,"y":0,"z":"top-front band"},{"length":"+X","width":"+Y","thickness":"+Z"},"SOURCE_EXPLICIT",s3,"single front top rail between sides; exact rail depth/height not dimensioned in doc"),
 P("P-LEG",A,"leg_plinth_panel",4,None,{"x":"n/a","y":"n/a","z":145},{"x":"corners under bottom"},{"length":"+Z"},"SOURCE_EXPLICIT",s3,"adjustable legs 145mm set; >4 legs on wide units (5-6)"),
 P("P-SHF-A",A,"adjustable_shelf",1,16,{"x":"W-tL-tR-clearance (~566)","y":"<560 partial depth","z":16},{"x":17,"y":"~inset from front","z":"user-set on pins"},{"length":"+X","width":"+Y","thickness":"+Z"},"SOURCE_EXPLICIT",s3,"partial-depth shelf on metal pins; exact shelf depth not stated"),
]
# AU-KAB-003 200 wall
A="AU-KAB-003"; s4=["SRC-D-0004"]
parts+= [
 P("P-SID-L",A,"side_left",1,16,{"x":16,"y":300,"z":720},{"x":0,"y":0,"z":0},{"length":"+Z"},"SOURCE_EXPLICIT",s4,""),
 P("P-SID-R",A,"side_right",1,16,{"x":16,"y":300,"z":720},{"x":184,"y":0,"z":0},{"length":"+Z"},"SOURCE_EXPLICIT",s4,""),
 P("P-TOP",A,"top_panel",1,16,{"x":168,"y":300,"z":16},{"x":16,"y":0,"z":704},{"length":"+X","width":"+Y","thickness":"+Z"},"SOURCE_EXPLICIT",s4,"inset between sides"),
 P("P-BTM",A,"bottom_panel",1,16,{"x":168,"y":300,"z":16},{"x":16,"y":0,"z":0},{"length":"+X"},"SOURCE_EXPLICIT",s4,""),
 P("P-BCK",A,"back_panel",1,16,{"x":200,"y":16,"z":720},{"x":0,"y":300,"z":0},{"thickness":"+Y"},"SOURCE_EXPLICIT",s4,"external overlay full rear"),
 P("P-SHF-A",A,"adjustable_shelf",1,16,{"x":168,"y":"<300","z":16},{"x":16,"y":"inset","z":"on pins"},"SOURCE_EXPLICIT",s4,""),
]
# AU-KAB-007 oven cab
A="AU-KAB-011"; s9=["SRC-D-0009"]
parts+= [
 P("P-SID-L",A,"side_left",1,16,{"x":16,"y":560,"z":720},{"x":0,"y":0,"z":0},{"length":"+Z"},"SOURCE_EXPLICIT",s9,"heat deflector fitted"),
 P("P-SID-R",A,"side_right",1,16,{"x":16,"y":560,"z":720},{"x":584,"y":0,"z":0},{"length":"+Z"},"SOURCE_EXPLICIT",s9,""),
 P("P-BTM",A,"bottom_panel",1,16,{"x":568,"y":560,"z":16},{"x":16,"y":0,"z":0},{},"SOURCE_EXPLICIT",s9,""),
 P("P-SUP-1",A,"stretcher_rail",2,16,{"x":568,"y":560,"z":16},{"x":16,"y":0,"z":"mid & upper (oven opening positions)"},{"length":"+X","width":"+Y","thickness":"+Z"},"SOURCE_EXPLICIT",s9,"TWO full-width support panels between sides forming oven opening; positions fixed by appliance spec"),
 P("P-BCK",A,"back_panel",0,None,None,None,{},"SOURCE_EXPLICIT",s9,"ABSENT_CONFIRMED - open rear for ventilation"),
 P("P-TOP",A,"top_panel",0,None,None,None,{},"SOURCE_EXPLICIT",s9,"ABSENT_CONFIRMED"),
]
# AU-KAB-005 corner base (simplified L model)
A="AU-KAB-005"; s6=["SRC-D-0006"]
parts+= [
 P("P-BTM",A,"bottom_panel",1,16,{"outline":"L-shape 900x900 footprint (leg depth 560)","z":16},{"x":0,"y":0,"z":0},{},"SOURCE_EXPLICIT",s6,"L-shaped single piece"),
 P("P-BCK-1",A,"back_panel",2,16,{"x":"leg length","y":16,"z":720},{"x":"rear of each L leg","z":0},{},"SOURCE_EXPLICIT",s6,"two overlay backs, one per L leg"),
 P("P-SID",A,"side_left/side_right",2,16,{"x":16,"y":560,"z":720},{"x":"outer end of each L leg","y":"overhangs past back"},{},"SOURCE_EXPLICIT",s6,"sides overhang past backs = built-in wall rebate"),
 P("P-BRK",A,"other",1,None,{"desc":"flat metal bracket inner top corner"},{} ,{},"SOURCE_EXPLICIT",s6,"ties inner corner top"),
 P("P-LEG",A,"leg_plinth_panel",5,None,{"z":145},{},{},"SOURCE_EXPLICIT",s6,"5-6 legs incl inner corner"),
 P("P-SHF-A",A,"adjustable_shelf",1,16,{"outline":"L-shape"},{},{},"SOURCE_EXPLICIT",s6,"L-shaped shelf on pins"),
]
# AU-KAB-009 two-piece corner pantry
A="AU-KAB-009"; s12=["SRC-D-0012"]
parts+= [
 P("P-BASE-UNIT",A,"other",1,None,{"desc":"lower carcass box H=865"},{} ,{},"SOURCE_EXPLICIT",s12,"separate base component"),
 P("P-TOP-UNIT",A,"other",1,None,{"desc":"upper carcass box H=1335"},{} ,{},"SOURCE_EXPLICIT",s12,"stacked on base"),
 P("P-END-DEC",A,"end_decor_panel",2,16,{"z":"~full column"},{},{"thickness":"+X"},"SOURCE_EXPLICIT",s12,"end panels protrude 14mm past cabinet front; create 20mm rear void needing packing before wall fix"),
]
# drawer box AU-KAB-015
A="AU-KAB-015"; s8=["SRC-D-0008"]
parts+= [
 P("P-DWR-BTM",A,"drawer_bottom",1,16,{"x":"full drawer width","y":"full drawer depth","z":16},{},{'thickness':'+Z'},"SOURCE_EXPLICIT",s8,"full footprint floor; 4 walls stand ON it"),
 P("P-DWR-F",A,"drawer_front(inner)",1,16,{},{"z":"stands on bottom"},{'length':'+X'},"SOURCE_EXPLICIT",s8,"inner front (decorative front separate)"),
 P("P-DWR-B",A,"drawer_back",1,16,{},{},{'length':'+X'},"SOURCE_EXPLICIT",s8,""),
 P("P-DWR-S",A,"drawer_side",2,16,{"x":16,"y":"full depth","z":"wall height"},{},{'thickness':'+X'},"SOURCE_EXPLICIT",s8,"sides overlap ends of front/back panels"),
]
# METOD wall
A="SE-IKE-001"; s30=["SRC-D-0030"]
parts+= [
 P("P-SID-L",A,"side_left",1,18,{"x":18,"y":None,"z":None},{},{'length':'+Z'},"VISUAL_ONLY",s30,"full-height; dense 32mm predrilled hole grid on inner face; thickness ~18mm typical IKEA (NOT confirmed in doc)"),
 P("P-TOP",A,"top_panel",1,18,{},{},{'length':'+X'},"VISUAL_ONLY",s30,"between sides; groove on inner face for back"),
 P("P-BTM",A,"bottom_panel",1,18,{},{},{'length':'+X'},"VISUAL_ONLY",s30,""),
 P("P-BCK",A,"back_panel",1,"~3-4 thin",{},{"position":"in grooves"},{'thickness':'+Y'},"VISUAL_ONLY",s30,"thin flexible panel (ships folded) slides into grooves = floating_capture; NOT overlay"),
 P("P-HGR",A,"hanger_rail",2,None,{},{"position":"inside top rear corners"},{}, "VISUAL_ONLY",s30,"metal suspension-rail brackets 10049571; cabinet hangs on rail"),
 P("P-CAM",A,"other","4+4",None,{"desc":"cam shaft 112996 + housing 113434 + dowel 101351"},{},{}, "SOURCE_EXPLICIT",s30,"cam+dowel knock-down joinery, no through-face screws"),
]
w('05_PARTS.jsonl', parts)

# ---------------- JOINTS ----------------
def J(jid,asm,a,b,topo,conn,fa,fb,hw,mach,dirn,src,st,notes=""):
    return {"joint_id":jid,"assembly_id":asm,"part_a":a,"part_b":b,"joint_topology":topo,
            "connection_type":conn,"contact_face_a":fa,"contact_face_b":fb,"hardware_refs":hw,
            "machining_features":mach,"assembly_direction":dirn,"source_ids":src,"evidence_status":st,"notes":notes}
JTS=[]
# base cabinet
A="AU-KAB-001"; s=["SRC-D-0003"]
JTS+= [
 J(f"J-{A}-01",A,"P-SID-L","P-BTM","end_into_face","fixed_confirmed","inner_face","left_end",["50mm wood screw"],"countersunk through-holes on outer face","from outside +X",[s[0]],"SOURCE_EXPLICIT","visible countersunk screw through side face"),
 J(f"J-{A}-02",A,"P-SID-R","P-BTM","end_into_face","fixed_confirmed","inner_face","right_end",["50mm wood screw"],"countersunk through-holes","from outside -X",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-03",A,"P-BCK","P-SID-L","overlay_face","fixed_confirmed","inner_face","rear_edge",["50mm wood screw"],"through back face into panel rear edge","-Y",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-04",A,"P-BCK","P-SID-R","overlay_face","fixed_confirmed","inner_face","rear_edge",["50mm wood screw"],"","-Y",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-05",A,"P-BCK","P-BTM","overlay_face","fixed_confirmed","inner_face","rear_edge",["50mm wood screw"],"","-Y",s,"SOURCE_EXPLICIT","back screws to bottom rear edge too"),
 J(f"J-{A}-06",A,"P-STR","P-SID-L","end_into_face","fixed_confirmed","left_end","inner_face",["28mm screw"],"","+X",s,"SOURCE_EXPLICIT","front top rail between sides"),
 J(f"J-{A}-07",A,"P-STR","P-SID-R","end_into_face","fixed_confirmed","right_end","inner_face",["28mm screw"],"","-X",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-08",A,"P-LEG","P-BTM","overlay_face","fixed_confirmed","top","bottom_face",["28mm screw"],"","-Z",s,"SOURCE_EXPLICIT","legs screwed to bottom underside"),
 J(f"J-{A}-09",A,"P-SHF-A","P-SID-L/R","other:pin_supported","removable","side faces","pin holes",["metal shelf pins"],"pre-drilled hole rows inner faces","+Z adjust",s,"SOURCE_EXPLICIT","adjustable positions"),
 J(f"J-{A}-10",A,"P-KCK","P-LEG","overlay_face","fixed_confirmed","rear face","leg front",["28mm screw"],"","-Y",["SRC-D-0024"],"SOURCE_EXPLICIT","kickboard 50mm setback (70mm pantry); scribed to floor"),
]
# wall cab
A="AU-KAB-003"; s=["SRC-D-0004"]
JTS+= [
 J(f"J-{A}-01",A,"P-SID-L","P-TOP","end_into_face","fixed_confirmed","inner_face","left_end",["50mm wood screw"],"countersunk","",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-02",A,"P-SID-L","P-BTM","end_into_face","fixed_confirmed","inner_face","left_end",["50mm wood screw"],"","",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-03",A,"P-BCK","P-SID-L","overlay_face","fixed_confirmed","inner_face","rear_edge",["50mm wood screw"],"","-Y",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-04",A,"P-BCK","P-TOP","overlay_face","fixed_confirmed","inner_face","rear_edge",["50mm wood screw"],"","-Y",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-05",A,"P-BCK","P-BTM","overlay_face","fixed_confirmed","inner_face","rear_edge",["50mm wood screw"],"","-Y",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-06",A,"carcass","wall","other:screw_through_back_to_stud","fixed_confirmed","back face","wall",["min 8g 65mm timber screw into studs"],"","-Y",s,"SOURCE_EXPLICIT",""),
]
# oven cab
A="AU-KAB-011"; s=["SRC-D-0009"]
JTS+= [
 J(f"J-{A}-01",A,"P-SID-L","P-BTM","end_into_face","fixed_confirmed","inner_face","left_end",["50mm wood screw"],"","",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-02",A,"P-SID-L","P-SUP-1","end_into_face","fixed_confirmed","inner_face","left_end",["50mm wood screw"],"","",s,"SOURCE_EXPLICIT","2 support panels between sides"),
]
# corner base
A="AU-KAB-005"; s=["SRC-D-0006"]
JTS+= [
 J(f"J-{A}-01",A,"P-BCK-1","P-BTM","overlay_face/end_into_face","fixed_confirmed","","rear edge / bottom edge",["50mm wood screw"],"","",s,"SOURCE_EXPLICIT",""),
 J(f"J-{A}-02",A,"P-SID","P-BCK-1","end_into_face","fixed_confirmed","inner_face","back end edge",["50mm wood screw"],"","",s,"SOURCE_EXPLICIT","sides overhang past backs"),
 J(f"J-{A}-03",A,"P-BRK","inner corner tops","overlay_face","fixed_confirmed","","",["flat bracket","28mm screws"],"","",s,"SOURCE_EXPLICIT",""),
]
# drawer box
A="AU-KAB-015"; s=["SRC-D-0008"]
JTS+= [
 J(f"J-{A}-01",A,"P-DWR-S","P-DWR-F","end_into_face","fixed_confirmed","inner_face","front_end",["50mm wood screw"],"","+X/-X",s,"SOURCE_EXPLICIT","sides overlap front/back ends"),
 J(f"J-{A}-02",A,"P-DWR-BTM","P-DWR-F","overlay_face","fixed_confirmed","top_face","bottom_edge",["50mm screw through bottom"],"","+Z",s,"SOURCE_EXPLICIT","walls stand on bottom; screws up through bottom"),
]
# PAT-006 oven tower
A="AU-KAB-010"; s=["SRC-D-0018"]
JTS+= [
 J(f"J-{A}-01",A,"end_panel","stacked_box_side","overlay_face","fixed_confirmed","inner_face","side outer face",["28mm screws"],"pre-drill","+X/-X",s,"SOURCE_EXPLICIT","boxes sandwiched between shared full-height end panels"),
 J(f"J-{A}-02",A,"mw_box","lower_drawer_cab","overlay_face","fixed_confirmed","bottom","top",["28mm screws"],"","+Z stack",["SRC-D-0020"],"SOURCE_EXPLICIT","front offset 18mm melamine/20mm thermoformed"),
]
# open shelf joinery
A="AU-KAB-018"; s=["SRC-D-0022"]
JTS+= [
 J(f"J-{A}-01",A,"P-SID","P-TOP/BTM/SHELF","end_into_face","removable","inner_face","ends",["cam+pin","40mm dowels + glue"],"8mm dowel holes; cam seats in horizontals; pins screw into sides","axial",s,"SOURCE_EXPLICIT","dowel assembly = no visible fixings; screw assembly only between cabs/walls"),
]
# METOD
A="SE-IKE-001"; s=["SRC-D-0030"]
JTS+= [
 J(f"J-{A}-01",A,"P-SID","P-TOP/BTM","end_into_face","removable","inner_face","ends",["cam shaft 112996","cam housing 113434","dowel 101351"],"predrilled 32mm-system holes","axial+cam rotate",s,"SOURCE_EXPLICIT","knock-down cam+dowel"),
 J(f"J-{A}-02",A,"P-BCK","P-SID/TOP/BTM","floating_capture","adjacent_unfixed","panel edge","groove",["none - groove"],"groove in panel inner faces","slide -Y",s,"VISUAL_ONLY","thin back slides into grooves"),
 J(f"J-{A}-03",A,"P-HGR","carcass/wall","other:suspension_rail","removable","bracket","rail",["rail bracket 10049571"],"","hang",s,"SOURCE_EXPLICIT","hangs on wall-mounted suspension rail"),
 J(f"J-{A}-04",A,"carcass","wall","other:anti_tip","fixed_confirmed","","",["anti-tip device supplied; wall screws/plugs to suit wall type - NOT included"],"","",s,"SOURCE_EXPLICIT","mandatory anti-tip"),
]
w('06_JOINTS.jsonl', JTS)

# ---------------- CONSTRAINTS ----------------
def C(cid,asm,subj,prop,rel,expr,dep,cond,der,src,notes=""):
    return {"constraint_id":cid,"assembly_id":asm,"subject":subj,"property":prop,"relation":rel,
            "value_or_expression":expr,"depends_on":dep,"conditions":cond,"derivation_status":der,"source_ids":src,"notes":notes}
CS=[
 C("C-PAT001-01","PAT-001","bottom_panel","dimensions_xyz.x","equals","W - tL - tR",["W","tL","tR"],["sides_full_height","bottom_between_sides"],"GEOMETRY_DERIVED",["SRC-D-0003"],"verified 600-16-16=568"),
 C("C-PAT001-02","PAT-001","back_panel","dimensions_xyz.x","equals","W",["W"],["external_overlay_back"],"GEOMETRY_DERIVED",["SRC-D-0003"],"overlay spans full rear face"),
 C("C-PAT001-03","PAT-001","back_panel","dimensions_xyz.z","equals","H",["H"],["external_overlay_back"],"GEOMETRY_DERIVED",["SRC-D-0003"],""),
 C("C-PAT001-04","PAT-001","side_left/right","dimensions_xyz.z","equals","H",["H"],["sides_full_height"],"SOURCE_EXPLICIT",["SRC-D-0003"],""),
 C("C-PAT001-05","PAT-001","front_rail","dimensions_xyz.x","equals","W - tL - tR",["W","tL","tR"],["rail_between_sides"],"GEOMETRY_DERIVED",["SRC-D-0003"],"rail spans inner width"),
 C("C-PAT001-06","PAT-001","cabinet","H_carcass","equals","720 (kaboodle standard; CTM/custom may vary)",["H"],["kaboodle_range"],"SOURCE_EXPLICIT",["SRC-D-0002"],"order guide"),
 C("C-PAT001-07","PAT-001","leg","set_height","equals","145 nominal (adjustable ~100-150 measured to floor)",["legH"],["adjustable_legs"],"SOURCE_EXPLICIT",["SRC-D-0003","SRC-D-0024"],""),
 C("C-PAT001-08","PAT-001","kickboard","front_setback","equals","50 (70 on pantries)",[],["kick_on_leg_backs"],"SOURCE_EXPLICIT",["SRC-D-0024"],"toe-space depth"),
 C("C-PAT001-09","PAT-001","cabinet","wall_fix","equals","min 8g x 65mm screws into timber studs",[],["stud_wall"],"SOURCE_EXPLICIT",["SRC-D-0003"],"other substrates = suitable anchors"),
 C("C-PAT002-01","PAT-002","top/bottom_panel","dimensions_xyz.x","equals","W - tL - tR",["W","tL","tR"],["inset_top_bottom"],"GEOMETRY_DERIVED",["SRC-D-0004"],""),
 C("C-PAT003-01","PAT-003","side_panel","depth","greater_than","back_panel y extent (sides overhang = built-in wall rebate)",[],["corner_unit"],"SOURCE_EXPLICIT",["SRC-D-0006"],"'side panels will overhang from the back panels'"),
 C("C-PAT005-01","PAT-005","fixed_shelf","dimensions_xyz.x","equals","W - tL - tR",["W","tL","tR"],["fixed_shelf_between_sides"],"GEOMETRY_DERIVED",["SRC-D-0011"],""),
 C("C-PAT006-01","PAT-006","box_front","setback_vs_end_panel_front","equals","18 (melamine doors) / 20 (thermoformed)",["door_type"],["stacked_between_end_panels"],"SOURCE_EXPLICIT",["SRC-D-0018","SRC-D-0020"],"front alignment rule"),
 C("C-PAT006-02","PAT-009","corner_pantry","component_heights","equals","base 865 + top 1335 = 2200",[],["two_piece_stack"],"SOURCE_EXPLICIT",["SRC-D-0012"],""),
 C("C-PAT006-03","PAT-006","end_decor_panel","front_protrusion","equals","14mm past cabinet front",[],["end_panels_fitted"],"SOURCE_EXPLICIT",["SRC-D-0012"],""),
 C("C-PAT006-04","PAT-006","rear_void","depth","equals","20mm after end panels - pack before wall fixing",[],["end_panels_fitted"],"SOURCE_EXPLICIT",["SRC-D-0012"],""),
 C("C-PAT010-01","PAT-010","middle_panel","z_position","equals","site-drilled per rangehood brand",["appliance"],["rangehood"],"SOURCE_EXPLICIT",["SRC-D-0021"],"NOT factory dimensioned"),
 C("C-MW-01","AU-KAB-013","mw_box_front","offset_vs_lower_cab","equals","18 melamine / 20 thermoformed",["door_type"],["stacked_on_drawer_cab"],"SOURCE_EXPLICIT",["SRC-D-0020"],""),
 C("C-HINGE-01","generic_AU","hinge_cup","diameter","equals","35mm cup; finished side gap ~1-2mm",[],["concealed_hinge"],"SOURCE_EXPLICIT",["SRC-D-0028"],"KB guide pp48-50"),
 C("C-DOOR-01","AU-KAB-*","door_front","dimensions_xyz.x","equals","W - 2*gap (full overlay, gap~1-2mm)",["W","gap"],["full_overlay"],"GEOMETRY_DERIVED",["SRC-D-0028"],"verify per product"),
 C("C-32MM-01","SE-IKE-001","side_hole_grid","system","equals","32mm-system predrilled rows full height",[],["metod"],"VISUAL_ONLY",["SRC-D-0030"],"row spacing consistent with 32mm; exact pitch not measured"),
]
w('07_CONSTRAINTS.jsonl', CS)

# ---------------- PARAMETER CANDIDATES ----------------
PC=[
 {"param_id":"PC-001","pattern_id":"PAT-001","input_vars":["W","D","H","tL","tR","tBtm","tBack","legH"],
  "computed":{"bottom.widthX":"W-tL-tR","back.widthX":"W","back.heightZ":"H","sides.heightZ":"H","rail.widthX":"W-tL-tR","shelf.widthX":"W-tL-tR-2*g","door.widthX":"W-2*gap (full overlay)"},
  "condition_branch":"solid_overlay_back + front_top_rail + legs","evidence":"MULTI_CASE_VERIFIED (W-51600..06, CTM, W-70106)","counter_cases":["PAT-007 oven (no back/top)","PAT-016 internal/rebated backs change back dims"],"golden_test_refs":["AU-KAB-001 W600: bottom=568, back=600x720"]},
 {"param_id":"PC-002","pattern_id":"PAT-002","input_vars":["W","D","H","t"],
  "computed":{"top.widthX":"W-2t","bottom.widthX":"W-2t","back.widthX":"W","back.heightZ":"H","shelf.widthX":"W-2t-2g"},
  "condition_branch":"closed box wall cab","evidence":"MULTI_CASE_VERIFIED (wall family 150-900, deep, slimline)","counter_cases":[],"golden_test_refs":["AU-KAB-003 W200: top=168"]},
 {"param_id":"PC-003","pattern_id":"PAT-005","input_vars":["W","D","H","t","fixed_shelf_z"],
  "computed":{"fixed_shelf.widthX":"W-2t","fixed_shelf.z":"per product (broom kit note: 1664mm up from inside base in 600 pantry)","stack":[]},
  "condition_branch":"single tall carcass","evidence":"SOURCE_EXPLICIT","counter_cases":["PAT-006 two-piece corner pantry has different stack"],"golden_test_refs":["W-51899 broom kit: divider at 1664mm up, 50/498mm back from front"]},
 {"param_id":"PC-004","pattern_id":"PAT-006","input_vars":["H_total","unit_heights[]","end_panel_t","door_type"],
  "computed":{"stack_order":"bottom-up list","box_front_offset":"18|20 by door_type","end_panel.height":"H_total"},
  "condition_branch":"shared end panels","evidence":"SOURCE_EXPLICIT","counter_cases":[],"golden_test_refs":["corner pantry 865+1335"]},
 {"param_id":"PC-005","pattern_id":"PAT-011","input_vars":["innerW","drawer_depth","t_drawer"],
  "computed":{"drawer_bottom.x":"innerW - 2*t_drawer (walls stand ON bottom: front/back between sides? NO - bottom is full footprint UNDER walls)","note":"bottom spans full drawer footprint; front/back/side widths independent of bottom capture"},
  "condition_branch":"timber 5-piece drawer","evidence":"SOURCE_EXPLICIT","counter_cases":["NZ metal-sided drawer = different params"],"golden_test_refs":[]},
 {"param_id":"PC-006","pattern_id":"PAT-015","input_vars":["W","D","H","t","back_t","groove_depth"],
  "computed":{"top.widthX":"W-2t (cam+dowel inset)","back.widthX":"~W-2t+2*groove_depth (inside grooves)","back.install":"floating_capture"},
  "condition_branch":"groove back + cam joinery","evidence":"VISUAL_ONLY (needs dimensional confirmation)","counter_cases":[],"golden_test_refs":[]},
]
w('08_PARAMETER_CANDIDATES.jsonl', PC)

# ---------------- EVIDENCE INDEX ----------------
EV=[
 ("EV-0001","SRC-D-0003","W-51605 PDF p2 'assembling cabinet'","base carcass = bottom+back+2sides+front rail+legs+adj shelf; screw-through-face joinery","a_storyblok_com__0e4dc19e1e1c6a83_p2.png","manufacturer_doc"),
 ("EV-0002","SRC-D-0004","W-51620 PDF p2","wall cab = 2sides+top+bottom+overlay back+adj shelf","a_storyblok_com__f1939afbad8b45d6_p2.png","manufacturer_doc"),
 ("EV-0003","SRC-D-0006","W-51608 PDF p2","corner base = L bottom + 2 backs + 2 sides(overhang) + bracket + 5 legs","a_storyblok_com__089e1dcfb8ccd4f3_p2.png","manufacturer_doc"),
 ("EV-0004","SRC-D-0007","W-51627 PDF p2","corner wall = L top + L bottom + 2 backs + 2 sides + L shelf","a_storyblok_com__5265e75adfc462d4_p2.png","manufacturer_doc"),
 ("EV-0005","SRC-D-0009","W-51609 PDF p2","oven cab = sides+bottom+2 support panels; NO back, NO top","a_storyblok_com__2c5f1ba312d9f91d_p2.png","manufacturer_doc"),
 ("EV-0006","SRC-D-0011","W-51633 PDF p2","600 pantry = tall single carcass, fixed shelf, overlay back","a_storyblok_com__4d53d00b3722ac85_p2.png","manufacturer_doc"),
 ("EV-0007","SRC-D-0018","oven tower PDF p2","tower = stacked boxes between 2 full-height end panels; 28mm screws box->end; 18/20mm front offset; MW box 360mm from top","a_storyblok_com__8dbd9653d03d0169_p2.png","manufacturer_doc"),
 ("EV-0008","SRC-D-0008","W-51615 PDF p2","drawer box = bottom floor + 4 walls standing on it; screws through sides into ends","a_storyblok_com__907f2c4e26d5816d_p2.png","manufacturer_doc"),
 ("EV-0009","SRC-D-0020","MW box PDF p2","closed 5-panel box; stacks on drawer cab, 18/20mm front offset","a_storyblok_com__a01495b7068d4467_p2.png","manufacturer_doc"),
 ("EV-0010","SRC-D-0021","W-51628 PDF p2","rangehood cab = open bottom, site-drilled middle panel","a_storyblok_com__361d1727a0131b1c_p2.png","manufacturer_doc"),
 ("EV-0011","SRC-D-0026","W-79959 PDF p2","farmhouse sink cab = open top, front apron rails, overlay back, 6 legs","a_storyblok_com__7107b2402339c42d_p2.png","manufacturer_doc"),
 ("EV-0012","SRC-D-0022","W-77932 PDF p2","open shelf: cam+pin+dowel+glue OR screw assembly; overlay back","a_storyblok_com__1705924f67895dec_p2.png","manufacturer_doc"),
 ("EV-0013","SRC-D-0024","kickboards PDF p2","kickboard 50mm setback (70 pantry), screwed to leg backs, scribed to floor","a_storyblok_com__ef29e6646d5a5e18_p2.png","manufacturer_doc"),
 ("EV-0014","SRC-D-0015","W-70116 PDF p2 + text","blind corner pantry = tube construction, cam+pin x8, NO back panel","a_storyblok_com__34ef7bab3bc6354c_p2.png","manufacturer_doc"),
 ("EV-0015","SRC-D-0023","CTM PDF p2","customisable cabs share base/wall carcass patterns","a_storyblok_com__972555fb523d6a0b_p2.png","manufacturer_doc"),
 ("EV-0016","SRC-D-0030","METOD PDF p7-p9","METOD: cam shaft+housing+dowel; 32mm hole grid; folded thin back->grooves; suspension brackets","www_ikea_com__9a2ff823d34641d0_p7-9.png","manufacturer_doc"),
 ("EV-0017","SRC-D-0028","KB guide pp44-45","generic floor cab: back+base+2ends+2rails; 4 back methods; corner=2 backs+2 front rails","text p44-45","training_authority"),
 ("EV-0018","SRC-D-0029","CFP 16pp","mortice-tenon panels, Rafix, hanging rail brackets, scribed kickboards","customflatpack text","manufacturer_doc"),
 ("EV-0019","SRC-D-0002","order guide pp","dimension matrix: base 720x560; wall 720x300/400; fingerpull -20mm; corner base 900x900x560; blind 984mm","text","manufacturer_doc"),
 ("EV-0020","SRC-D-0012","corner pantry PDF","two-piece 865+1335 stack; 14mm end protrusion; 20mm rear void; hinge hole refs 132/222,116/227","text","manufacturer_doc"),
]
w('09_EVIDENCE_INDEX.jsonl',[
 {"evidence_id":e,"source_id":s,"locator":l,"what_it_proves":w_,"visual_ref":v,"reliability":r,"accessed_at":"2026-10-13"}
 for (e,s,l,w_,v,r) in EV])

print('done')
