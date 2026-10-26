# -*- coding: utf-8 -*-
default cs_friend_da = 0
default cs_day03_part10_done = False
default cs_da_day3_music_talk = False
default cs_da_day3_shared_silence = False
default cs_da_day3_choice_done = False
default cs_da_day3_music_awarded = False
default cs_da_cheek_kiss_day3 = False
default cs_day03_dinner_horn_played = False
default cs_day03_dinner_arrived = False
default cs_day03_sketchbook_location = None
init -9 python:
    cs_state_defaults.update(cs_friend_da=0, cs_day03_part10_done=False, cs_da_day3_music_talk=False, cs_da_day3_shared_silence=False, cs_da_day3_choice_done=False, cs_da_day3_music_awarded=False, cs_da_cheek_kiss_day3=False, cs_day03_dinner_horn_played=False, cs_day03_dinner_arrived=False, cs_day03_sketchbook_location=None)
