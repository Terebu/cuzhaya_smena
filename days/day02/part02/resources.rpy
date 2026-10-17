# -*- coding: utf-8 -*-
default cs_met_mi = False
default cs_mi_name_known = False
default cs_day02_miku_listened = None
default cs_part02_cast = []
default cs_part02_cg = False
default cs_part02_live = False

init 25 python:
    renpy.music.register_channel("cs_piano", mixer="music", loop=False)
    cs_mi = DynamicCharacter("u'Мику' if cs_mi_name_known else u'Девушка'", color="#00deff", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
    cs_darya_piano_track = "mods/chuzaya_smena/audio/music/music_club/The_Unfinished_Lullaby.mp3"
    cs_miku_piano_track = "sound/music/miku_song_voice.ogg"

image cs_cg_darya_piano_day = im.Scale("mods/chuzaya_smena/cg/music_club/cg_darya_piano_day.png", 1920, 1080)
image cs_cg_miku_piano_day = im.Scale("mods/chuzaya_smena/cg/music_club/cg_miku_piano_day.png", 1920, 1080)
