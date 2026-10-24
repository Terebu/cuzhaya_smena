# -*- coding: utf-8 -*-
# Shared friendship counter; existing MI/UN counters retain their declarations.
default cs_friend_dv = 0
init -9 python:
    cs_state_defaults.update(cs_friend_dv=0)
