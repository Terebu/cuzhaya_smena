# -*- coding: utf-8 -*-
# Custom and original Viola share the existing cs tag. Original names stay valid.
init -2 python:
    with renpy.file(cs_root + "sp/viola/metadata.json") as cs_vfile:
        cs_vmeta = json.load(cs_vfile)
    for cs_ventry in cs_vmeta:
        for cs_vdistance in ("normal", "far", "close"):
            renpy.image("cs custom " + cs_ventry["pose"] + " medical " + cs_vdistance, cs_dasha_image(cs_ventry, cs_vdistance, 1560.0))

transform cs_viola_normal_left:
    xalign 0.03
    yanchor 1.0
    ypos 1.48

transform cs_viola_far_left:
    xalign 0.03
    yanchor 1.0
    ypos 1.31

transform cs_viola_close_left:
    xalign 0.03
    yanchor 1.0
    ypos 1.72

image cs_cg_lena_darya_help_viola_day = im.Scale(cs_root + "cg/viola/cg_lena_darya_help_viola_day.png", 1920, 1080)

transform cs_viola_normal_right:
    xalign 0.97
    yanchor 1.0
    ypos 1.48

transform cs_viola_normal_center:
    xalign 0.5
    yanchor 1.0
    ypos 1.48

transform cs_viola_far_right:
    xalign 0.97
    yanchor 1.0
    ypos 1.31

transform cs_viola_far_center:
    xalign 0.5
    yanchor 1.0
    ypos 1.31

transform cs_viola_close_right:
    xalign 0.97
    yanchor 1.0
    ypos 1.72

transform cs_viola_close_center:
    xalign 0.5
    yanchor 1.0
    ypos 1.72
