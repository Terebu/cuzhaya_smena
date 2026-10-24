# -*- coding: utf-8 -*-
# Small, non-modal overlay: stock dialogue/save/history controls remain available.
screen cs_instagram_post(photo):
    zorder 11
    frame:
        xpos 900
        ypos 25
        xsize 528
        background Solid("#141a23f2")
        padding (24, 18)
        vbox:
            spacing 10
            text "Lena Sokolova · Instagram" size 26 color "#ffffff" font "fonts/calibri.ttf"
            add photo
            text "Комментарии   ·   Сохранить" size 23 color "#d2d5df" font "fonts/calibri.ttf"

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
    if mode == "off":
        use cs_powered_off_phone(phone_x, phone_width)
    else:
        frame:
            xpos phone_x
            ypos 100
            xsize phone_width
            ysize (490 if mode == "profile" else 245)
            background Solid("#141a23f2")
            padding (24,24)
            vbox:
                spacing 16
                hbox:
                    spacing 90
                    text "SAMSUNG" size 21 color "#aab4c0" font "fonts/calibri.ttf"
                    text ("%d%%" % charge) size 26 color "#ee968b" font "fonts/calibri.ttf"
                if mode == "profile":
                    text "Instagram" size 31 color "#ffffff" font "fonts/calibri.ttf"
                    null height 12
                    text "Lena Sokolova" size 29 color "#dfc9f4" font "fonts/calibri.ttf"
                    text "247 813" size 46 color "#ffffff" font "fonts/calibri.ttf"
                    text "подписчиков" size 23 color "#aab4c0" font "fonts/calibri.ttf"
                    null height 15
                    text "Фотография · рисунок\nГород · мастерская · лес" size 23 color "#d2d5df" font "fonts/calibri.ttf"
                elif charge == 2:
                    text "Карты" size 29 color "#ffffff" font "fonts/calibri.ttf"
                    add Solid("#6d737b") xysize (320,85)
                else:
                    text "Низкий заряд батареи" size 26 color "#ffffff" font "fonts/calibri.ttf"
                    text "410 · Маршрут" size 23 color "#aab4c0" font "fonts/calibri.ttf"
