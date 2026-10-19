# -*- coding: utf-8 -*-
init 25 python:
    cs_day_music_think = "sound/music/just_think.ogg"
    cs_day_music_unknown = "sound/music/into_the_unknown.ogg"
    # Dictionary entry exists, but this installation omits the actual file.
    cs_day_music_doubt = music_list.get("doubt_everyone", "") if renpy.loadable(music_list.get("doubt_everyone", "")) else "sound/music/waltz_of_doubts.ogg"
    cs_day_music_home = "sound/music/a_promise_from_distant_days.ogg"
    cs_day_music_mystery = "sound/music/mystery_girl.ogg"
    cs_day_music_friends = "sound/music/lets_be_friends.ogg"
    cs_day_music_daily = "sound/music/my_daily_life.ogg"
    cs_day_camp_center = "sound/ambiences/camp_center_day.ogg"
    cs_day_music_play = "sound/music/i_want_to_play.ogg"
    cs_day_music_everyday = "sound/music/feeling_good.ogg"
    cs_day_cabin = "sound/ambiences/int_cabin_day.ogg"
    cs_day_sfx_bed = "sound/sfx/bed_squeak1.ogg"
    cs_day_sfx_door = "sound/sfx/open_door_1.ogg"
    cs_day_sfx_horn = "sound/sfx/dinner_horn_processed.ogg"
    cs_day_dining_full = "sound/ambiences/dining_hall_full.ogg"

image cs_lena_pioneer_mirror = im.Scale(cs_root + "cg/cg_lena_pioneer_mirror.png", 1920, 1080)

transform cs_day_dasha_right:
    xalign 0.9
    yanchor 1.0
    ypos 1.60
