# -*- coding: utf-8 -*-
label cs_day02_dinner_branches:
    if cs_friend_mz >= 2:
        call cs_day02_64a
    elif cs_friend_mz == 1:
        call cs_day02_64b
    else:
        call cs_day02_64c
    label cs_check_part09_dinner:
    if cs_friend_mz >= 1:
        call cs_day02_64d
        if cs_friend_mz >= 2 and cs_mz_map_lead:
            call cs_day02_64d1
        elif cs_friend_mz == 1:
            call cs_day02_64d2
    call cs_day02_64e
    return
