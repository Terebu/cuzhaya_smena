# -*- coding: utf-8 -*-
init 35 python:
    def cs_silence_menu_audio(*args, **kwargs):
        if not cs_active or getattr(store, "main_menu", False) or getattr(store, "_main_menu", False):
            return
        menu_track = config.main_menu_music
        if not menu_track:
            return
        for channel in ("music", "ambience"):
            if renpy.music.get_playing(channel=channel) == menu_track:
                renpy.music.stop(channel=channel, fadeout=0.0)
    def cs_menu_audio_at_line(event, **kwargs):
        if event == "begin":
            cs_silence_menu_audio()
    config.all_character_callbacks.append(cs_menu_audio_at_line)
    config.after_load_callbacks.append(cs_silence_menu_audio)
