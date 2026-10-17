# -*- coding: utf-8 -*-
init 30 python:
    def cs_focus_loaded_gallery():
        if renpy.get_screen("cs_instagram_post") is not None:
            cs_frame_focus([])
    config.after_load_callbacks.append(cs_focus_loaded_gallery)
