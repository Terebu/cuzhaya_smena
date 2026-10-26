# -*- coding: utf-8 -*-
default cs_day03_part11_done = False
default cs_mz_dinner_friend_on_arrival = None
default cs_mz_hug_allowed_day3 = False
default cs_day03_dinner_greeting_done = False
default cs_mz_evening_help_day3 = False
default cs_mz_evening_help_completed_day3 = False
default cs_mz_evening_choice_done = False
default cs_mz_evening_help_awarded = False
default cs_day03_dinner_finished = False
default cs_mi_followup_target_day = None
default cs_dv_followup_target_day = None
init -9 python:
    cs_state_defaults.update(cs_day03_part11_done=False, cs_mz_dinner_friend_on_arrival=None, cs_mz_hug_allowed_day3=False, cs_day03_dinner_greeting_done=False, cs_mz_evening_help_day3=False, cs_mz_evening_help_completed_day3=False, cs_mz_evening_choice_done=False, cs_mz_evening_help_awarded=False, cs_day03_dinner_finished=False, cs_mi_followup_target_day=None, cs_dv_followup_target_day=None)

image cs_library_interior_evening = LiveComposite((1920,1080), (0,0), "bg int_library_day", (0,0), Solid("#17213d40"))
