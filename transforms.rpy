# -*- coding: utf-8 -*-
transform cs_dasha_seated:
    xalign 0.5
    yanchor 1.0
    ypos 1.60

transform cs_gate_approach:
    xalign 0.5
    yalign 0.45
    zoom 1.0
    ease 5.0 zoom 1.12

transform cs_bus_ride:
    align (0.5, 0.5)
    zoom 1.01
    xoffset 0
    yoffset 0
    ease 1.8 xoffset -3 yoffset 2
    ease 2.2 xoffset 2 yoffset -1
    ease 1.6 xoffset 0 yoffset 0
    repeat

transform cs_snow_drift:
    alpha 0.7
    yoffset -3
    linear 3.0 yoffset 3 alpha 1.0
    linear 3.0 yoffset -3 alpha 0.7
    repeat
