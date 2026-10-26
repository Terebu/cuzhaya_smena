# -*- coding: utf-8 -*-
default cs_day03_part08_started = False
default cs_day03_part08_done = False
default cs_mz_friend_on_arrival_day3 = None
default cs_mz_day3_honest_book_talk = False
default cs_mz_book_talk_awarded_day3 = False
default cs_mz_book_borrowed_day3 = False
default cs_mz_open_library_invitation_day3 = False
default cs_day03_novel_selected = False
default cs_day03_library_legacy_bridge = False
init -9 python:
    cs_state_defaults.update(cs_day03_part08_started=False, cs_day03_part08_done=False, cs_mz_friend_on_arrival_day3=None, cs_mz_day3_honest_book_talk=False, cs_mz_book_talk_awarded_day3=False, cs_mz_book_borrowed_day3=False, cs_mz_open_library_invitation_day3=False, cs_day03_novel_selected=False, cs_day03_library_legacy_bridge=False)
