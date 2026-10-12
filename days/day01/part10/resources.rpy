# -*- coding: utf-8 -*-
default cs_friend_mz = 0
default cs_met_mz = False
default cs_part10_choice = None
default cs_day01_part10_done = False

image cs_library_exterior_sunset = im.Scale("mods/chuzaya_smena/bg/lib/library_exterior_sunset.png", 1920, 1080)
image cs_library_exterior_night = im.Scale("mods/chuzaya_smena/bg/lib/library_exterior_night.png", 1920, 1080)

init 20 python:
    cs_mz = Character(u"Женя", color="#d6baff", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")

label cs_day01_dinner_bridge:
    $ save_name = u"Чужая смена — День 1: Ужин"
    scene bg ext_dining_hall_near_sunset with Dissolve(1.0)
    cs_narrator "У дверей столовой уже собирались пионеры. Мы с Дарьей присоединились к ним."
    scene bg int_dining_hall_sunset with Dissolve(1.0)
    play ambience cs_day_dining_full fadeout 1.0 fadein 1.5
    cs_narrator "Мы взяли подносы и нашли свободный стол. После всех разговоров за день обычный ужин оказался удивительно приятной паузой."
    window hide dissolve
    pause 0.8
    window show dissolve
    return
