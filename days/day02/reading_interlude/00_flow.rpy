# -*- coding: utf-8 -*-
label cs_day02_reading_interlude:
    call cs_day02_reading_01
    call cs_day02_reading_02
    call cs_day02_reading_03
    if cs_friend_mz >= 2:
        call cs_day02_reading_04c
    elif cs_friend_mz == 1:
        call cs_day02_reading_04b
    else:
        call cs_day02_reading_04a
    call cs_day02_reading_05
    call cs_day02_reading_06
    if cs_friend_mz >= 2:
        call cs_day02_reading_07c
    elif cs_friend_mz == 1:
        call cs_day02_reading_07b
    else:
        call cs_day02_reading_07a
    call cs_day02_reading_08
    call cs_day02_reading_09
    call cs_day02_reading_book_drop
    $ cs_reading_live = False
    return
