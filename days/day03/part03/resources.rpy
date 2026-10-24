# -*- coding: utf-8 -*-
default cs_day03_part03_done = False
default cs_mz_book_requested_day3 = False
default cs_mz_day3_book_awarded = False
default cs_day03_library_visit_time = None
default cs_day03_mz_breakfast_together = False
default cs_day03_semen_breakfast_joined = False
default cs_day03_at_dining_door = False
init -9 python:
    cs_state_defaults.update(cs_day03_part03_done=False, cs_mz_book_requested_day3=False,
        cs_mz_day3_book_awarded=False, cs_day03_library_visit_time=None,
        cs_day03_mz_breakfast_together=False, cs_day03_semen_breakfast_joined=False,
        cs_day03_at_dining_door=False)
    def cs_day03_p3_breakfast_cast():
        return ["cs_zhenya", "cs_darya"] if cs_day03_mz_breakfast_together else ["cs_darya"]

transform cs_day03_p3_actor_enter(x=0.25):
    xpos x
    xanchor 0.5
    ypos 1.60
    yanchor 1.0
    zoom 1.0
    alpha 0.0
    linear 0.28 alpha 1.0
