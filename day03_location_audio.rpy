# -*- coding: utf-8 -*-
# Ambient beds follow actual rooms. CGs and inward shots retain the room.
default cs_day03_audio_location = None
init -9 python:
    cs_state_defaults.update(cs_day03_audio_location=None)
    def cs_day03_audio_target(image):
        if image.startswith("cs_cg_") or image in ("cs_sleep_winter", "cs_sleep_summer", "cs_lena_pioneer_mirror"):
            return False
        if image == "black":
            return None
        if image.startswith("bg int_dining_hall"):
            return "sound/ambiences/dining_hall_full.ogg"
        if image.startswith("cs_house_lena_darya_int"):
            return "sound/ambiences/int_cabin_day.ogg"
        if image.startswith("bg int_aidpost"):
            return "sound/ambiences/medstation_inside_day.ogg"
        if image.startswith(("bg int_library", "bg int_musclub", "cs_int_administration", "cs_library_interior")):
            return None
        if image.startswith(("bg ext_", "cs_camp_path_", "cs_ext_administration_", "cs_house_lena_darya_ext_", "cs_library_exterior_")):
            if image.endswith("night"):
                return "sound/ambiences/camp_center_night.ogg"
            return "sound/ambiences/camp_center_evening.ogg" if image.endswith(("sunset", "night")) else "sound/ambiences/camp_center_day.ogg"
        return False
    def cs_day03_location_audio(image):
        if not getattr(store,"cs_active",False) or not getattr(store,"cs_day03_started",False):
            return
        target = cs_day03_audio_target(image)
        if target is False:
            return
        store.cs_day03_audio_location = image
        current = renpy.music.get_playing(channel="ambience")
        if target is None:
            if current:
                renpy.music.stop(channel="ambience", fadeout=0.8)
        elif current != target:
            renpy.music.play(target, channel="ambience", loop=True, fadeout=0.8, fadein=0.8)
        renpy.music.set_volume(0.16 if target else 0.0, channel="ambience", delay=0.5)
    def cs_day03_audio_after_load():
        if not getattr(store,"cs_active",False) or not getattr(store,"cs_day03_started",False):
            return
        # Prefer the frame in the save; the remembered room may predate this fix.
        for tag in renpy.get_showing_tags():
            name = " ".join((tag,) + tuple(renpy.get_attributes(tag) or ()))
            if cs_day03_audio_target(name) is not False:
                if cs_day03_audio_location != name or renpy.music.get_playing(channel="ambience") != cs_day03_audio_target(name):
                    cs_day03_location_audio(name)
                return
        if cs_day03_audio_location:
            cs_day03_location_audio(cs_day03_audio_location)
    config.after_load_callbacks.append(cs_day03_audio_after_load)
    # A loaded interaction can restore its scene after the early load hook.
    # This is idempotent: unchanged rooms never restart the playing bed.
    config.interact_callbacks.append(cs_day03_audio_after_load)
# Verified old breakfast-exit dialogue resume addresses.
# Add aliases only for absent IDs in this byte-identical mod script.
init 40 python:
    cs_day03_audio_legacy_says = {('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24373): 29, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24370): 25, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24369): 24, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24368): 23, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24367): 22, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24366): 21, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24365): 20, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24364): 19, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24357): 12, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24356): 11, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24355): 10, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24354): 9, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24353): 8, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24352): 7, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24351): 6, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24350): 5, ('game/mods/chuzaya_smena/cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy', 1792933293, 24349): 4}
    cs_day03_audio_current_says = {}
    for _cs_audio_node in list(renpy.game.script.namemap.values()):
        if type(_cs_audio_node).__name__ == "Say" and str(getattr(_cs_audio_node,"filename","")).replace("\\","/").rstrip("c").endswith("cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy"):
            cs_day03_audio_current_says[_cs_audio_node.linenumber] = _cs_audio_node
    for _cs_audio_old, _cs_audio_line in cs_day03_audio_legacy_says.items():
        if _cs_audio_old not in renpy.game.script.namemap and _cs_audio_line in cs_day03_audio_current_says:
            renpy.game.script.namemap[_cs_audio_old] = cs_day03_audio_current_says[_cs_audio_line]
