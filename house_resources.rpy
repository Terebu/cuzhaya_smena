# -*- coding: utf-8 -*-
init 25 python:
    cs_day_sfx_knock = "sound/sfx/knocking_door_outside.ogg"

image cs_house_lena_darya_int_day = im.Scale("mods/chuzaya_smena/bg/house/int_house_lena_darya_day.png", 1920, 1080)
image cs_house_lena_darya_int_sunset = im.Scale("mods/chuzaya_smena/bg/house/int_house_lena_darya_sunset.png", 1920, 1080)
image cs_house_lena_darya_int_night = im.Scale("mods/chuzaya_smena/bg/house/int_house_lena_darya_night.png", 1920, 1080)
image cs_house_lena_darya_ext_day = im.Scale("mods/chuzaya_smena/bg/house/ext_house_lena_darya_day.png", 1920, 1080)
image cs_house_lena_darya_ext_sunset = im.Scale("mods/chuzaya_smena/bg/house/ext_house_lena_darya_sunset.png", 1920, 1080)
image cs_house_lena_darya_ext_night = im.Scale("mods/chuzaya_smena/bg/house/ext_house_lena_darya_night.png", 1920, 1080)

transform cs_semen_far_left:
    xalign 0.03
    yanchor 1.0
    ypos 1.35

# Full-room dialogue camera. Never inherit the reading desk's close view.
transform cs_house_full_frame:
    zoom 1.0
    xalign 0.5
    yalign 0.5

init 30 python:
    def cs_restore_house_full_frame():
        for tag in ("cs_house_lena_darya_int_day", "cs_house_lena_darya_int_night", "cs_house_lena_darya_ext_day", "cs_house_lena_darya_ext_sunset", "cs_house_lena_darya_ext_night"):
            if not renpy.showing(tag):
                continue
            bounds = renpy.get_image_bounds(tag)
            if bounds and abs(bounds[0]) < 1 and abs(bounds[1]) < 1 and abs(bounds[2]-1920) < 1 and abs(bounds[3]-1080) < 1:
                continue
            # Drop the saved background ATL state; actors are untouched.
            renpy.hide(tag)
            renpy.show(tag, zorder=-100, at_list=[Transform(zoom=1.0, xzoom=1.0, yzoom=1.0, xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5)])
    def cs_house_camera_after_load():
        if cs_restore_house_full_frame not in config.interact_callbacks:
            config.interact_callbacks.append(cs_restore_house_full_frame)
        cs_restore_house_full_frame()
    config.after_load_callbacks.append(cs_house_camera_after_load)
    config.interact_callbacks.append(cs_restore_house_full_frame)
