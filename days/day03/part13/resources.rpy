# -*- coding: utf-8 -*-
default cs_day03_part13_started = False
default cs_day03_part13_done = False
default cs_mz_book_finished_day3 = False
default cs_mz_day3_final_discussion = False
default cs_da_day3_fear_of_getting_used_to_camp = False
default cs_da_day3_quiet_walk = False
default cs_da_day3_night_choice_done = False
default cs_da_day3_night_trust_awarded = False
default cs_da_waiting_outside_library_day3 = False
init -9 python:
    cs_state_defaults.update(cs_day03_part13_started=False, cs_day03_part13_done=False, cs_mz_book_finished_day3=False, cs_mz_day3_final_discussion=False, cs_da_day3_fear_of_getting_used_to_camp=False, cs_da_day3_quiet_walk=False, cs_da_day3_night_choice_done=False, cs_da_day3_night_trust_awarded=False, cs_da_waiting_outside_library_day3=False)

image cs_library_interior_night = LiveComposite((1920,1080), (0,0), "bg int_library_day", (0,0), Solid("#16203965"))
