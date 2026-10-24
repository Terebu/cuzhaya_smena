# -*- coding: utf-8 -*-
default cs_day03_part06_done = False
default cs_day03_part06_started = False
default cs_mz_catalog_checked_day3 = False
default cs_mi_day3_arrangement_help = False
default cs_dv_music_talk_day3 = False
default cs_un_day3_art_talk = False
default cs_un_sketch_invite_day3 = False
default cs_mi_day3_awarded = False
default cs_dv_day3_awarded = False
default cs_un_day3_awarded = False
default cs_day03_lunch_horn_played = False
default cs_day03_lunch_arrived = False
init -9 python:
    cs_state_defaults.update(cs_day03_part06_done=False, cs_day03_part06_started=False, cs_mz_catalog_checked_day3=False, cs_mi_day3_arrangement_help=False, cs_dv_music_talk_day3=False, cs_un_day3_art_talk=False, cs_un_sketch_invite_day3=False, cs_mi_day3_awarded=False, cs_dv_day3_awarded=False, cs_un_day3_awarded=False, cs_day03_lunch_horn_played=False, cs_day03_lunch_arrived=False)
