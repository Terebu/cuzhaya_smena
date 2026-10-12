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

screen cs_phone(charge=7, mode="battery", phone_x=100, phone_width=380):
    zorder 10
    frame:
        xpos phone_x
        ypos 100
        xsize phone_width
        ysize (490 if mode == "profile" else 245)
        background Solid("#06080df7" if mode == "off" else "#141a23f2")
        padding (24,24)
        vbox:
            spacing 16
            if mode != "off":
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
            elif mode == "off":
                null height 45
                text "" size 26
            elif charge == 2:
                text "Карты" size 29 color "#ffffff" font "fonts/calibri.ttf"
                add Solid("#6d737b") xysize (320,85)
            else:
                text "Низкий заряд батареи" size 26 color "#ffffff" font "fonts/calibri.ttf"
                text "410 · Маршрут" size 23 color "#aab4c0" font "fonts/calibri.ttf"
