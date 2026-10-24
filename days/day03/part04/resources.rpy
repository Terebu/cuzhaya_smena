# -*- coding: utf-8 -*-
default cs_day03_part04_done = False
default cs_viola_friend_before_day3 = None
default cs_viola_day3_awarded = False
default cs_helped_viola_day3 = False
default cs_viola_day3_bonus_seen = False
default cs_day03_viola_check_done = False
default cs_day03_part05_route = None
init -9 python:
    cs_state_defaults.update(cs_day03_part04_done=False,cs_viola_friend_before_day3=None,
        cs_viola_day3_awarded=False,cs_helped_viola_day3=False,
        cs_viola_day3_bonus_seen=False,cs_day03_viola_check_done=False,
        cs_day03_part05_route=None)
image cs_cg_lena_darya_medical_inventory_day = im.Scale(cs_root + "cg/viola/cg_lena_darya_medical_inventory_day.png",1920,1080)

default cs_dv_medpoint_day3 = False
default cs_day03_medpoint_revision_done = False
init -9 python:
    cs_state_defaults.update(cs_dv_medpoint_day3=False,cs_day03_medpoint_revision_done=False)
