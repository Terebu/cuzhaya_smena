# -*- coding: utf-8 -*-
# Also repair the visual state of older saves made while a gallery card was open.
init 30 python:
    def cs_focus_loaded_gallery():
        if renpy.get_screen("cs_instagram_post") is not None:
            for cs_tag in ("cs_dasha_winter", "cs_darya", "cs_dasha"):
                renpy.hide(cs_tag)
    config.after_load_callbacks.append(cs_focus_loaded_gallery)
