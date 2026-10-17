# -*- coding: utf-8 -*-
label cs_day_title(day_number):
    hide screen cs_phone
    hide screen cs_instagram_post
    stop music fadeout 1.5
    stop ambience fadeout 1.5
    stop sound fadeout 0.5
    window hide dissolve
    scene black with Dissolve(1.0)
    show screen cs_day_title_screen(day_number)
    with Dissolve(0.6)
    label cs_check_day_title:
    $ renpy.pause(2.2, hard=True)
    hide screen cs_day_title_screen
    with Dissolve(0.6)
    return

screen cs_day_title_screen(day_number):
    text (u"День %d" % day_number):
        align (0.5, 0.5)
        size 64
        color "#ffffff"
        font "fonts/corbel.ttf"

transform cs_early_morning:
    matrixcolor TintMatrix("#bdcbe2") * BrightnessMatrix(-0.12)
