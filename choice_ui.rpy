# -*- coding: utf-8 -*-
# Keep the original game's menus; improve contrast only while this mod is active.
init 55 python:
    cs_previous_menu_arguments = config.menu_arguments_callback
    def cs_menu_arguments(*args, **kwargs):
        if cs_previous_menu_arguments is not None:
            args, kwargs = cs_previous_menu_arguments(*args, **kwargs)
        if cs_active:
            kwargs["screen"] = "cs_mod_choice"
        return args, kwargs
    config.menu_arguments_callback = cs_menu_arguments

screen cs_mod_choice(items):
    modal True
    frame:
        xalign 0.5
        yalign 0.48
        xmaximum 1500
        padding (25, 20)
        background Solid("#0c1928e8")
        vbox:
            spacing 12
            for item in items:
                if item.action is not None:
                    textbutton item.caption:
                        action item.action
                        xfill True
                        padding (25, 18)
                        background None
                        hover_background Solid("#294852")
                        text_size 32
                        text_color "#ffe39a"
                        text_hover_color "#ffffff"
                        text_outlines [(1, "#000000", 0, 1)]
                else:
                    text item.caption color "#ffe39a" size 32
