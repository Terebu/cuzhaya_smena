# -*- coding: utf-8 -*-
default cs_day03_started = False
default cs_day03_part01_done = False
default cs_sl_poster_saved_day3 = False
default cs_day03_poster_location = None

init -9 python:
    # New-game reset must clear the new defaults as well as the older ones.
    cs_state_defaults.update(cs_day03_started=False, cs_day03_part01_done=False,
                             cs_sl_poster_saved_day3=False, cs_day03_poster_location=None)

image cs_cg_lena_sport_mirror_bandaged_morning = im.Scale(cs_resolve_asset("cg/lena_sokolova/cg_lena_sport_mirror_bandaged_morning.png"), 1920, 1080)

transform cs_day03_dawn:
    matrixcolor TintMatrix("#a5b6d4") * BrightnessMatrix(-0.18)
    zoom 1.0
    xalign 0.5
    yalign 0.5
