# -*- coding: utf-8 -*-
default cs_day03_part02_done = False
default cs_se_day3_morning_awarded = False
init -9 python:
    cs_state_defaults.update(cs_day03_part02_done=False, cs_se_day3_morning_awarded=False)

# Fade only the entering actor; the whole-scene transition must not reuse
# a transient placement of the newly rendered full-height image.
transform cs_day03_darya_enter:
    xpos 0.5
    xanchor 0.5
    ypos 1.60
    yanchor 1.0
    zoom 1.0
    xoffset 0
    yoffset 0
    alpha 0.0
    linear 0.28 alpha 1.0
