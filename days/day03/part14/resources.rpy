# -*- coding: utf-8 -*-
default cs_day03_part14_started = False
default cs_day03_part14_done = False
default cs_day03_completed = False
default cs_da_friend_before_night = None
default cs_da_bed_request_day3 = False
default cs_da_respected_space_day3 = False
default cs_da_shared_bed_day3 = False
default cs_da_love_confession_day3 = False
default cs_da_unspoken_feelings_day3 = False
default cs_da_bed_choice_done_day3 = False
default cs_da_shared_bed_awarded_day3 = False
default cs_da_confession_choice_done_day3 = False
default cs_da_shared_sleep_cg_seen_day3 = False
init -9 python:
    cs_state_defaults.update(cs_day03_part14_started=False, cs_day03_part14_done=False, cs_day03_completed=False, cs_da_friend_before_night=None, cs_da_bed_request_day3=False, cs_da_respected_space_day3=False, cs_da_shared_bed_day3=False, cs_da_love_confession_day3=False, cs_da_unspoken_feelings_day3=False, cs_da_bed_choice_done_day3=False, cs_da_shared_bed_awarded_day3=False, cs_da_confession_choice_done_day3=False, cs_da_shared_sleep_cg_seen_day3=False)
image cs_house_lena_darya_int_sleep_night = LiveComposite((1920,1080), (0,0), "cs_house_lena_darya_int_night", (0,0), Solid("#10152660"))
image cs_cg_lena_darya_shared_sleep_night = im.Scale(cs_resolve_asset("cg/lena_n_dasha/cg_lena_darya_shared_sleep_night.png"),1920,1080)
