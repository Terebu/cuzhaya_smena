# -*- coding: utf-8 -*-
# Original game files are read directly from archive.rpa by Ren'Py.
init -5 python:
    cs_root = "mods/chuzaya_smena/"
    cs_music_calm = "mods/chuzaya_smena/audio/music/Cosmic Echoes.mp3"
    cs_music_410 = "mods/chuzaya_smena/audio/music/Lost Souls.mp3"
    cs_music_After_Hours= "mods/chuzaya_smena/audio/music/After Hours.mp3"
    cs_wind = "sound/ambiences/cold_wind_loop.ogg"
    cs_bus_idle = "sound/sfx/bus_idle.ogg"
    cs_bus_moving = "sound/sfx/bus_interior_moving.ogg"
    cs_bus_start = "sound/sfx/intro_bus_engine_start.ogg"
    cs_bus_stop = "sound/sfx/bus_stop.ogg"
    cs_bus_door = "sound/sfx/intro_bus_door_open.ogg"
    cs_phone_error = "sound/sfx/cellular_phone_error.ogg"
    cs_forest = "sound/ambiences/forest_day.ogg"
    cs_camp = "sound/ambiences/camp_entrance_day.ogg"



image cs_room = im.Scale("mods/chuzaya_smena/bg/cs_room_winter.png", 1920, 1080)
image cs_stop = im.Scale("mods/chuzaya_smena/bg/bus_stop.png", 1920, 1080)
image cs_street = im.Scale("mods/chuzaya_smena/bg/street.png", 1920, 1080)
image cs_bus_n_stop = im.Scale("mods/chuzaya_smena/bg/bus_n_stop.png", 1920,1080)
image cs_bus_winter = im.Scale("mods/chuzaya_smena/bg/cs_bus_winter.png", 1920,1080)
image cs_bus_city = im.Scale("mods/chuzaya_smena/bg/bus_city.png", 1920, 1080)
image cs_snow = "mods/chuzaya_smena/ui/snow.png"
image cs_sunlight = Solid("#fff5d7")
image cs_sleep_winter = im.Scale("mods/chuzaya_smena/cg/bus_sleep_d.png", 1920, 1080)
image cs_sleep_summer = im.Scale("mods/chuzaya_smena/cg/ikarus_sleep_d.png", 1920, 1080)
image cs_instagram_oni = im.FactorScale("mods/chuzaya_smena/cg/сп_ьфыл_oni.png", 480.0 / 1024.0)
image cs_instagram_studio = im.FactorScale("mods/chuzaya_smena/cg/cg_studio.png", 480.0 / 1024.0)
image cs_instagram_crush = im.FactorScale("mods/chuzaya_smena/cg/cg_crush.png", 480.0 / 1024.0)
image cs_instagram_evening = im.FactorScale("mods/chuzaya_smena/cg/cg_m_evneng.png", 480.0 / 1024.0)
image cs_instagram_daily = im.FactorScale("mods/chuzaya_smena/cg/cg_daily_life.png", 480.0 / 1024.0)

# A discreet windshield frame preserves the viewpoint inside the parked bus.
image cs_windshield = LiveComposite((1920,1080), (0,0), Solid("#0000"), (0,0), Solid("#28323ce0", xysize=(1920,60)), (0,0), Solid("#28323ce0", xysize=(60,1080)), (1860,0), Solid("#28323ce0", xysize=(60,1080)), (0,1020), Solid("#28323ce0", xysize=(1920,60)))
