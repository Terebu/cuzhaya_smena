# -*- coding: utf-8 -*-
# Small, non-modal overlay: stock dialogue/save/history controls remain available.
transform cs_phone_fade:
    on show:
        alpha 0.0
        linear 0.4 alpha 1.0
    on hide:
        linear 0.3 alpha 0.0
    on replace:
        alpha 1.0

screen cs_phone_status(charge, width):
    fixed:
        xysize (width, 34)
        add Solid("#1d2939")
        text "22:37" xpos 12 ypos 6 size 19 color "#e9eef5" font "fonts/calibri.ttf"
        text ("%d%%" % charge) xpos (width - 70) ypos 6 size 19 color "#ee968b" font "fonts/calibri.ttf"
        add Solid("#bbc7d5") xpos (width - 25) ypos 12 xysize (12, 9)

screen cs_instagram_post(photo, phone_x=100, phone_width=380):
    zorder 11
    $ cs_post_w = phone_width - 24
    $ cs_post_h = int(phone_width * 1.75) - 67
    fixed:
        at cs_phone_fade
        xpos (phone_x + 12)
        ypos 138
        xysize (cs_post_w, cs_post_h)
        clipping True
        add Solid("#111b28")
        use cs_phone_status(5, cs_post_w)
        text "Instagram" xpos 12 ypos 42 size 27 color "#ffffff" font "fonts/calibri.ttf"
        text "Lena Sokolova" xpos 12 ypos 78 size 21 color "#dfc9f4" font "fonts/calibri.ttf"
        add photo xpos 10 ypos 112 xysize (cs_post_w - 20, cs_post_h - 176) fit "contain"
        text "Комментарии · Сохранить" xpos 12 ypos (cs_post_h - 50) size 20 color "#d2d5df" font "fonts/calibri.ttf"
        add Solid("#aab5c6") xpos (cs_post_w // 2 - 28) ypos (cs_post_h - 13) xysize (56, 3)

screen cs_powered_off_phone(phone_x, phone_width):
    # A recognisable unlit handset rather than an empty square UI panel.
    $ cs_phone_height = int(phone_width * 1.75)
    frame:
        xpos phone_x
        ypos 100
        xysize (phone_width, cs_phone_height)
        padding (3, 3)
        background Solid("#68717d")
        fixed:
            add Solid("#161c25")
            add Solid("#05080c") xpos 9 ypos 35 xysize (phone_width - 24, cs_phone_height - 67)
            add Solid("#677280") xpos int(phone_width * 0.39) ypos 15 xysize (int(phone_width * 0.20), 4)
            add Solid("#394451") xpos int(phone_width * 0.40) ypos (cs_phone_height - 20) xysize (int(phone_width * 0.18), 4)

screen cs_phone(charge=7, mode="battery", phone_x=100, phone_width=380):
    zorder 10
    $ cs_phone_w = phone_width - 24
    $ cs_phone_h = int(phone_width * 1.75) - 67
    fixed:
        at cs_phone_fade
        use cs_powered_off_phone(phone_x, phone_width)
        if mode != "off":
            fixed:
                xpos (phone_x + 12)
                ypos 138
                xysize (cs_phone_w, cs_phone_h)
                clipping True
                add Solid("#111b28")
                use cs_phone_status(charge, cs_phone_w)
                if mode == "profile":
                    text "Instagram" xpos 16 ypos 48 size 30 color "#ffffff" font "fonts/calibri.ttf"
                    text "Lena Sokolova" xpos 16 ypos 116 size 27 color "#dfc9f4" font "fonts/calibri.ttf"
                    text "247 813" xpos 16 ypos 170 size 43 color "#ffffff" font "fonts/calibri.ttf"
                    text "подписчиков" xpos 16 ypos 225 size 23 color "#aab4c0" font "fonts/calibri.ttf"
                    text "Фотография · рисунок\nГород · мастерская · лес" xpos 16 ypos 298 xsize (cs_phone_w - 32) size 23 color "#d2d5df" font "fonts/calibri.ttf"
                elif charge == 2:
                    text "Карты" xpos 16 ypos 48 size 29 color "#ffffff" font "fonts/calibri.ttf"
                    fixed:
                        xpos 16
                        ypos 110
                        xysize (cs_phone_w - 32, 240)
                        clipping True
                        add Solid("#69727a")
                        add Solid("#929a9f") xpos 70 xysize (28, 240)
                        add Solid("#929a9f") ypos 104 xysize (cs_phone_w - 32, 24)
                        add Solid("#d6dadd") xpos 80 xysize (7, 240)
                        add Solid("#d6dadd") ypos 112 xysize (cs_phone_w - 32, 7)
                        add Solid("#d97171") xpos 76 ypos 104 xysize (16, 16)
                    text "410 · Маршрут" xpos 16 ypos 375 size 23 color "#c2cbd6" font "fonts/calibri.ttf"
                else:
                    add Solid("#bbc7d5") xpos (cs_phone_w // 2 - 56) ypos 115 xysize (112, 52)
                    add Solid("#111b28") xpos (cs_phone_w // 2 - 50) ypos 121 xysize (100, 40)
                    add Solid("#df8b88") xpos (cs_phone_w // 2 - 46) ypos 125 xysize (12, 32)
                    add Solid("#bbc7d5") xpos (cs_phone_w // 2 + 56) ypos 132 xysize (6, 18)
                    text "Низкий заряд батареи" xpos 16 ypos 205 xsize (cs_phone_w - 32) text_align 0.5 size 26 color "#ffffff" font "fonts/calibri.ttf"
                    text "410 · Маршрут" xpos 16 ypos 295 size 23 color "#aab4c0" font "fonts/calibri.ttf"
                add Solid("#aab5c6") xpos (cs_phone_w // 2 - 28) ypos (cs_phone_h - 13) xysize (56, 3)
