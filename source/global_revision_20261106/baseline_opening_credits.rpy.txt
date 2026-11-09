# -*- coding: utf-8 -*-
# Small timed credits over the opening room. No modal/full-screen panel.
transform cs_credit_title_timing:
    alpha 0.0
    linear 0.6 alpha 1.0
    pause 6.0
    linear 0.65 alpha 0.0
transform cs_credit_ai_timing:
    alpha 0.0
    pause 2.0
    linear 0.6 alpha 1.0
    pause 5.8
    linear 0.65 alpha 0.0
transform cs_credit_music_timing:
    alpha 0.0
    pause 4.0
    linear 0.6 alpha 1.0
    pause 5.6
    linear 0.65 alpha 0.0

transform cs_credit_panel_timing:
    alpha 0.0
    linear 0.35 alpha 1.0
    pause 10.45
    linear 0.35 alpha 0.0

screen cs_opening_credits_screen():
    zorder 20
    # Non-modal overlay: dialogue and player input continue underneath.
    if renpy.showing("cs_room"):
        frame:
            xpos 80
            ypos 155
            xysize (650, 220)
            background Solid("#101a29df")
            at cs_credit_panel_timing
        text "Чужая смена" id "cs_credit_title":
            xpos 105
            ypos 185
            size 64
            color "#fff2d7"
            outlines [(1, "#000000aa", 0, 0)]
            at cs_credit_title_timing
        text "Created with AI assistance" id "cs_credit_ai":
            xpos 108
            ypos 274
            size 29
            color "#ffffff"
            outlines [(1, "#000000aa", 0, 0)]
            at cs_credit_ai_timing
        text "Music by Purrple Cat · FreeLofi" id "cs_credit_music":
            xpos 108
            ypos 321
            size 29
            color "#e5edf6"
            outlines [(1, "#000000aa", 0, 0)]
            at cs_credit_music_timing
    timer 11.2 action Hide("cs_opening_credits_screen")

label cs_opening_credits:
    show screen cs_opening_credits_screen
    return
