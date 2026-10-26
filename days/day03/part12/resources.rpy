# -*- coding: utf-8 -*-
default cs_day03_part12_started = False
default cs_day03_part12_done = False
default cs_sl_friend_before_evening_choice = None
default cs_sl_evening_schedule_help_day3 = False
default cs_sl_day4_notice_offer = False
default cs_sl_evening_choice_done = False
default cs_sl_evening_help_awarded = False
default cs_sl_evening_scene_done_day3 = False
default cs_sl_evening_destination_told_day3 = False
default cs_day03_evening_book_retrieved = False
default cs_day03_part12_legacy_entry = False
init -9 python:
    cs_state_defaults.update(cs_day03_part12_started=False, cs_day03_part12_done=False, cs_sl_friend_before_evening_choice=None, cs_sl_evening_schedule_help_day3=False, cs_sl_day4_notice_offer=False, cs_sl_evening_choice_done=False, cs_sl_evening_help_awarded=False, cs_sl_evening_scene_done_day3=False, cs_sl_evening_destination_told_day3=False, cs_day03_evening_book_retrieved=False, cs_day03_part12_legacy_entry=False)
