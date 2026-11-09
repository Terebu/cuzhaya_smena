# -*- coding: utf-8 -*-
# A paced approach, independent engine bed, and a nonmusical uncanny soundscape.
default cs_bus_audio_revision = 0
default cs_bus_audio_mode = "natural"
default cs_bus_engine_phase = "off"
default cs_sports_level = 0.0
default cs_bus_mystery_active = False

init -9 python:
    cs_state_defaults.update(cs_bus_audio_revision=0,cs_bus_audio_mode="natural",cs_bus_engine_phase="off")
    cs_state_defaults.update(cs_sports_level=0.0)
    cs_state_defaults.update(cs_bus_mystery_active=False)

init 35 python:
    renpy.music.register_channel("cs_bus_engine",mixer="sfx",loop=True)
    renpy.music.register_channel("cs_bus_mystery",mixer="sfx",loop=True)
    cs_bus_knock_sting = cs_path("audio/sfx/bus/uncanny_knock_sting.ogg")
    cs_bus_distant = cs_path("audio/sfx/bus/engine_distant_loop.ogg")
    cs_bus_near = cs_path("audio/sfx/bus/engine_near_loop.ogg")
    cs_bus_brake = cs_path("audio/sfx/bus/air_brake_stop.ogg")
    cs_bus_door_open = cs_path("audio/sfx/bus/pneumatic_door_open.ogg")
    cs_bus_door_close = cs_path("audio/sfx/bus/pneumatic_door_close.ogg")
    cs_bus_departure = cs_path("audio/sfx/bus/departure_fading.ogg")
    cs_bus_drone = cs_path("audio/sfx/bus/uncanny_drone_loop.ogg")
    cs_bus_chuckle = cs_path("audio/sfx/bus/female_chuckle_behind.ogg")
    cs_bus_native_target = cs_day03_audio_target

    def cs_bus_location_target(image):
        original=cs_bus_native_target(image)
        if original is False:return False
        if cs_active and (getattr(store,"main_menu",False) or getattr(store,"_main_menu",False)):return None
        if cs_active and cs_d5_started:
            if cs_d5_quiet or cs_bus_audio_mode in ("silence","hushed"):return None
            if cs_bus_audio_mode == "ominous":return cs_bus_drone
            if image=="bg ext_no_bus" or image.startswith("cs_bus410_"):return "sound/ambiences/forest_day.ogg"
        return original
    cs_day03_audio_target = cs_bus_location_target

    def cs_bus_audio_ambient_volume(target):
        if not target:return 0.0
        return 0.22 if target == cs_bus_drone else 0.16

    def cs_bus_apply_bed():
        if cs_day03_audio_location:
            cs_day03_location_audio(cs_day03_audio_location)

    def cs_bus_engine(phase, restoring=False):
        store.cs_bus_engine_phase=phase
        if phase=="off":
            renpy.music.stop(channel="cs_bus_engine",fadeout=0.5)
            return
        track={"distant":cs_bus_distant,"cabin":cs_bus_distant,"near":cs_bus_near,"idle":cs_bus_near,"depart":cs_bus_departure}[phase]
        current=renpy.music.get_playing(channel="cs_bus_engine")
        if current!=track:
            renpy.music.play(track,channel="cs_bus_engine",loop=phase!="depart",fadeout=0.65,fadein=1.8 if phase=="cabin" else 0.8)
        if phase=="cabin":
            renpy.music.set_volume(0.03,channel="cs_bus_engine")
            renpy.music.set_volume(0.16,channel="cs_bus_engine",delay=4.0)
        elif phase=="distant":
            renpy.music.set_volume(0.025,channel="cs_bus_engine")
            renpy.music.set_volume(0.12,channel="cs_bus_engine",delay=6.0)
        elif phase=="near":
            renpy.music.set_volume(0.16,channel="cs_bus_engine")
            renpy.music.set_volume(0.30,channel="cs_bus_engine",delay=3.0)
        elif phase=="idle":renpy.music.set_volume(0.09,channel="cs_bus_engine",delay=0.8)
        else:renpy.music.set_volume(0.25,channel="cs_bus_engine",delay=0.25)

    def cs_bus_stock_sound(path,volume):
        if not renpy.loadable(path):raise Exception("Missing bus recording: "+path)
        renpy.music.set_volume(volume,channel="sound")
        renpy.music.play(path,channel="sound",loop=False)

    def cs_bus_cue(event):
        store.cs_bus_audio_revision=1
        if event in ("warning","uncanny"):
            store.cs_bus_audio_mode="ominous"
            renpy.music.stop(channel="music",fadeout=1.2)
            if event=="uncanny":renpy.music.set_volume(0.09,channel="cs_bus_engine",delay=1.0)
        elif event=="approach":
            store.cs_bus_audio_mode="hushed"
            cs_bus_engine("distant")
        elif event=="near":cs_bus_engine("near")
        elif event=="stop":
            cs_bus_engine("idle")
            cs_bus_stock_sound(cs_bus_brake,0.48)
        elif event=="open":cs_bus_stock_sound(cs_bus_door_open,0.48)
        elif event=="close":cs_bus_stock_sound(cs_bus_door_close,0.44)
        elif event=="chuckle":cs_bus_stock_sound(cs_bus_chuckle,0.34)
        elif event=="hush":store.cs_bus_audio_mode="hushed"
        elif event=="cabin_bus":cs_bus_engine("cabin")
        elif event=="cabin_bus_stop":
            renpy.music.stop(channel="cs_bus_engine",fadeout=1.0)
            store.cs_bus_engine_phase="off"
        elif event=="knock_warning":
            store.cs_bus_mystery_active=True
            renpy.music.set_volume(0.20,channel="cs_bus_mystery")
            if renpy.music.get_playing(channel="cs_bus_mystery")!=cs_bus_drone:
                renpy.music.play(cs_bus_drone,channel="cs_bus_mystery",loop=True,fadein=0.6)
        elif event=="mystery_end":
            store.cs_bus_mystery_active=False
            renpy.music.stop(channel="cs_bus_mystery",fadeout=1.0)
        elif event=="depart":cs_bus_engine("depart")
        elif event=="gone":
            renpy.music.set_volume(0.0,channel="cs_bus_engine",delay=3.0)
            renpy.music.stop(channel="cs_bus_engine",fadeout=3.0)
            store.cs_bus_engine_phase="off"
        elif event=="calm":
            store.cs_bus_mystery_active=False
            renpy.music.stop(channel="cs_bus_mystery",fadeout=0.8)
            store.cs_bus_audio_mode="natural"
            cs_bus_engine("off")
        elif event=="silence":
            store.cs_bus_mystery_active=False
            renpy.music.stop(channel="cs_bus_mystery",fadeout=0.8)
            store.cs_bus_audio_mode="silence"
            cs_bus_engine("off")
        else:raise Exception("Unknown bus audio cue: "+event)
        cs_bus_apply_bed()

    def cs_bus_scene_enter(number):
        # Scene 6 continues the arrival in 5. Other scenes start with their room tone.
        if number not in (5,6):cs_bus_cue("silence" if number==20 else "calm")
        else:store.cs_bus_audio_revision=1

    def cs_bus_audio_loaded():
        if not cs_active or not cs_d5_started:return
        if cs_bus_mystery_active:
            if renpy.music.get_playing(channel="cs_bus_mystery")!=cs_bus_drone:
                renpy.music.set_volume(0.20,channel="cs_bus_mystery")
                renpy.music.play(cs_bus_drone,channel="cs_bus_mystery",loop=True,fadein=0.6)
        if not cs_bus_audio_revision:
            # Old slots gain a bed, never a replayed braking/door one-shot.
            store.cs_bus_audio_revision=1
            old_sound=renpy.music.get_playing(channel="sound") or ""
            if cs_d5_scene in (5,6) and any(x in old_sound for x in ("bus_interior_moving","bus_stop","intro_bus_door_open","energy_door_bus","intro_bus_engine_start")):
                renpy.music.stop(channel="sound",fadeout=0.1)
            visible=any(renpy.showing(x) for x in ("cs_bus410_closed_day","cs_bus410_open_day","bg ext_bus"))
            store.cs_bus_audio_mode="silence" if cs_d5_quiet else ("ominous" if cs_d5_scene in (5,6) else "natural")
            store.cs_bus_engine_phase="idle" if visible else "off"
        cs_bus_apply_bed()
        if cs_bus_engine_phase in ("distant","cabin","near","idle"):
            track=cs_bus_distant if cs_bus_engine_phase in ("distant","cabin") else cs_bus_near
            if renpy.music.get_playing(channel="cs_bus_engine")!=track:cs_bus_engine(cs_bus_engine_phase,True)
        elif cs_bus_engine_phase=="off":renpy.music.stop(channel="cs_bus_engine",fadeout=0.2)

    def cs_bus_audio_watch():
        if not cs_active or getattr(store,"main_menu",False) or getattr(store,"_main_menu",False):
            if renpy.music.get_playing(channel="cs_bus_engine"):renpy.music.stop(channel="cs_bus_engine")
            if renpy.music.get_playing(channel="cs_bus_mystery"):renpy.music.stop(channel="cs_bus_mystery")
    config.after_load_callbacks.append(cs_bus_audio_loaded)
    config.interact_callbacks.append(cs_bus_audio_watch)

init 36 python:
    # A nearby game is a spatial layer over the camp bed, never an indoor sound.
    renpy.music.register_channel("cs_sports",mixer="sfx",loop=True)
    cs_sports_track=cs_path("audio/ambience/sports_court_day.ogg")
    def cs_sports_level_for(image):
        if not cs_active or not cs_d5_started or cs_d5_quiet or getattr(store,"main_menu",False) or getattr(store,"_main_menu",False):return 0.0
        # The early-morning running scene explicitly describes an empty court.
        if cs_d5_scene==7 and image=="cs_camp_path_day":return 0.065
        if cs_d5_scene==9:
            if image=="cs_camp_path_day":return 0.075
            if image=="bg ext_playground_day":return 0.16
        return 0.0
    def cs_sports_sync(image):
        level=cs_sports_level_for(image)
        current=renpy.music.get_playing(channel="cs_sports")
        if not level:
            if current:renpy.music.stop(channel="cs_sports",fadeout=1.5)
        elif current!=cs_sports_track:
            renpy.music.set_volume(level,channel="cs_sports")
            renpy.music.play(cs_sports_track,channel="cs_sports",loop=True,fadein=2.5)
        elif cs_sports_level!=level:
            renpy.music.set_volume(level,channel="cs_sports",delay=1.5)
        store.cs_sports_level=level
    cs_sports_base_location_audio=cs_day03_location_audio
    def cs_sports_location_audio(image):
        cs_sports_base_location_audio(image)
        if cs_day03_audio_target(image) is not False:cs_sports_sync(image)
    cs_day03_location_audio=cs_sports_location_audio
    def cs_sports_loaded():
        cs_sports_sync(cs_day03_audio_location)
    def cs_sports_watch():
        if not cs_active or cs_d5_quiet or getattr(store,"main_menu",False) or getattr(store,"_main_menu",False):
            cs_sports_sync(None)
    config.after_load_callbacks.append(cs_sports_loaded)
    config.interact_callbacks.append(cs_sports_watch)

init 90 python:
    cs_bus_base_restore=cs_restore_audio
    def cs_bus_restore_audio():
        store.cs_bus_mystery_active=False
        renpy.music.stop(channel="cs_bus_mystery")
        renpy.music.stop(channel="cs_bus_engine")
        renpy.music.stop(channel="cs_sports")
        store.cs_sports_level=0.0
        if renpy.music.get_playing(channel="ambience")==cs_bus_drone:renpy.music.stop(channel="ambience")
        store.cs_bus_engine_phase="off"
        store.cs_bus_audio_mode="natural"
        cs_bus_base_restore()
    cs_restore_audio=cs_bus_restore_audio
    cs_bus_base_reset=cs_reset_state
    def cs_bus_reset_state():
        renpy.music.stop(channel="cs_bus_mystery")
        renpy.music.stop(channel="cs_bus_engine")
        renpy.music.stop(channel="cs_sports")
        cs_bus_base_reset()
    cs_reset_state=cs_bus_reset_state
