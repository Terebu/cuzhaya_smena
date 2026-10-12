# -*- coding: utf-8 -*-
# User-supplied full PNGs. Same proportional distance system as Darya.
init -3 python:
    with renpy.file("mods/chuzaya_smena/sp/semen_metadata.json") as cs_semen_file:
        cs_semen_metadata = json.load(cs_semen_file)
    for cs_entry in cs_semen_metadata:
        for cs_distance in ("far", "normal", "close"):
            cs_image = cs_dasha_image(cs_entry, cs_distance, 1580.0)
            cs_base = "cs_semen " + cs_entry["pose"] + " pioneer"
            renpy.image(cs_base + " " + cs_distance, cs_image)
            if cs_distance == "normal": renpy.image(cs_base, cs_image)

transform cs_semen_far_center:
    xalign 0.5
    yanchor 1.0
    ypos 1.35

transform cs_semen_normal_left:
    xalign 0.08
    yanchor 1.0
    ypos 1.60
