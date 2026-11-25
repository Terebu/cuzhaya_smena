# -*- coding: utf-8 -*-
default cs_d7_started = False
default cs_d7_voice_shared = False
default cs_d7_book_returned = False
default cs_d7_records_collected = False
default cs_d7_departed = False
default cs_ep_found_dasha = False
default cs_ep_found_semen = False
default cs_ep_room_clean = False
default cs_ep_guest_mode = None
default cs_ep_guest = None
default cs_ep_guest_ties = ()
default cs_ep_contact_page = 0
default cs_ep_romance = False
default cs_ep_ending = None
default persistent.cs_ep_seen_endings = set()

image cs_bg_epi_lena_kitchen = cs_path("bg/moscow/lena_kitchen_winter.png")
image cs_bg_epi_metro_platform = cs_path("bg/moscow/metro_platform.png")
image cs_epilogue_travel = cs_path("bg/moscow/metro_wagon.png")
image cs_bg_epi_metro_escalator = cs_path("bg/moscow/metro_escalator.png")
image cs_bg_epi_metro_exit = cs_path("bg/moscow/metro_exit_winter.png")
image cs_epilogue_coffee = cs_path("bg/moscow/metro_coffee.png")
image cs_cg_epi_semen_cleanup_zhenya = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_cleanup_zhenya.png"), 1920, 1080)
image cs_cg_epi_semen_door = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_door.png"), 1920, 1080)
image cs_cg_epi_darya_coffee = im.Scale(cs_path("cg/epilogue_new/cg_epi_darya_coffee.png"), 1920, 1080)
image cs_cg_epi_semen_tea_zhenya = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_tea_zhenya.png"), 1920, 1080)
image cs_cg_epi_semen_tea_slavya = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_tea_slavya.png"), 1920, 1080)
image cs_cg_epi_semen_tea_miku = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_tea_miku.png"), 1920, 1080)
image cs_cg_epi_semen_tea_tikhonova = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_tea_tikhonova.png"), 1920, 1080)
image cs_cg_epi_semen_tea_trio = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_tea_trio.png"), 1920, 1080)
image cs_cg_epi_semen_cleanup_zhenya_dusting = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_cleanup_zhenya_dusting.png"), 1920, 1080)
image cs_cg_epi_semen_cleanup_zhenya_finishing = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_cleanup_zhenya_finishing.png"), 1920, 1080)
image cs_cg_epi_semen_cleanup_alisa = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_cleanup_alisa.png"), 1920, 1080)
image cs_cg_epi_semen_cleanup_trio = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_cleanup_trio.png"), 1920, 1080)
image cs_cg_epi_semen_cleanup_slavya = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_cleanup_slavya.png"), 1920, 1080)
image cs_cg_epi_semen_cleanup_group = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_cleanup_group.png"), 1920, 1080)
image cs_cg_epi_semen_cleanup_miku = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_cleanup_miku.png"), 1920, 1080)
image cs_cg_epi_semen_cleanup_tikhonova = im.Scale(cs_path("cg/epilogue_new/cg_epi_semen_cleanup_tikhonova.png"), 1920, 1080)
image cs_epilogue_kitchen = cs_path("bg/moscow/semen_kitchen_winter.png")
image cs_bg_epi_semen_yard_day = cs_path("bg/moscow/semen_yard_day.png")
image cs_bg_epi_semen_yard_evening = cs_path("bg/moscow/semen_yard_evening.png")
image cs_bg_epi_morning_street = cs_path("bg/moscow/moscow_street_morning.png")
image cs_cg_epi_metro_reflection = cs_path("cg/epilogue_new/cg_epi_metro_reflection.png")
image cs_cg_epi_metro_reunion_friend = cs_path("cg/epilogue_new/cg_epi_metro_reunion_friend.png")
image cs_cg_epi_metro_reunion_romance = cs_path("cg/epilogue_new/cg_epi_metro_reunion_romance.png")

init -9 python:
    cs_state_defaults.update(cs_d7_started=False, cs_d7_voice_shared=False,
        cs_d7_book_returned=False, cs_d7_records_collected=False, cs_d7_departed=False,
        cs_ep_found_dasha=False, cs_ep_found_semen=False, cs_ep_room_clean=False,
        cs_ep_guest_mode=None, cs_ep_guest=None, cs_ep_guest_ties=(),
        cs_ep_contact_page=0, cs_ep_romance=False, cs_ep_ending=None)

init 60 python:
    cs_lena_apartment_ambience = cs_path("audio/ambience/lena_apartment_winter_loop.ogg")

    cs_ep_guest_thresholds = (("sl", 3), ("dv", 3), ("mi", 2), ("mz", 4), ("un", 3))

    def cs_ep_guest_result(scores, helped, contacts):
        ranks = [(k, scores[k])
                 for k, threshold in cs_ep_guest_thresholds if scores[k] >= threshold]
        if not ranks:
            return ("none", None, ())
        best = max(rank for k, rank in ranks)
        ties = tuple(k for k, rank in ranks if rank == best)
        if helped in ties:
            return ("single", helped, ())
        known = tuple(k for k in ties if k in contacts)
        if known:
            ties = known
        if len(ties) == 1:
            return ("single", ties[0], ())
        return ("choose", None, ties)

    def cs_ep_lock_route():
        if cs_ep_guest_mode not in (None, "all"):
            return
        scores = {k: getattr(store, "cs_friend_" + k) for k, _ in cs_ep_guest_thresholds}
        contacts = tuple(key for key, confirmed in (
            ("sl", cs_d6_sl_badge_received),
            ("dv", cs_d6_dv_pick_received),
            ("mi", cs_d6_mi_music_received),
            ("mz", cs_d6_mz_address_received),
            ("un", cs_d6_sketch_done or cs_d6_un_sketch_received or cs_d5_lena_respected),
        ) if confirmed)
        store.cs_ep_guest_mode, store.cs_ep_guest, store.cs_ep_guest_ties = cs_ep_guest_result(scores, cs_d6_help, contacts)
        store.cs_ep_romance = cs_da_shared_bed_day3 and cs_da_love_confession_day3

    def cs_ep_restore_winter_ui():
        if cs_active and cs_ep_guest_mode is not None:
            cs_rev_time("prolog")

    config.after_load_callbacks.append(cs_ep_restore_winter_ui)

    def cs_ep_choose_guest(guest):
        if cs_ep_guest_mode != "choose" or guest not in cs_ep_guest_ties:
            raise ValueError("Invalid epilogue guest: " + guest)
        store.cs_ep_guest = guest
        store.cs_ep_guest_mode = "single"

    def cs_ep_record_ending(ending):
        store.cs_ep_ending = ending

    def cs_d7_hide_portraits():
        for tag in cs_presence_tags:
            if renpy.showing(tag):
                renpy.hide(tag)

    def cs_d7_scene(image):
        cs_director_scene(image, location_audio=False)
        cs_thought_reset()
        store.cs_auto_pov = False

    def cs_d7_ambience(track, volume=0.23):
        renpy.music.set_volume(volume, channel="ambience", delay=0.65)
        queued = renpy.audio.audio.get_channel("ambience").context.last_filenames
        if tuple(queued or ()) != (track,):
            renpy.music.play(track, channel="ambience", loop=True, fadein=0.8, fadeout=0.8)

    def cs_d7_restore_aidpost_ambience():
        if cs_active and cs_d7_started and renpy.showing("bg int_aidpost_day"):
            cs_d7_ambience(cs_forest, 0.06)

    config.after_load_callbacks.append(cs_d7_restore_aidpost_ambience)

label cs_epilogue_credits:
    window hide dissolve
    $ persistent.cs_ep_seen_endings.add((cs_ep_ending, cs_ep_guest))
    $ renpy.save_persistent()
    $ cs_rev_music([cs_music_purrple_calm_waters, cs_music_purrple_gentle_breeze], 0.20, 2.0)
    call screen cs_epilogue_end_screen
    stop music fadeout 1.2
    $ cs_bus_cue("silence")
    $ cs_restore_audio()
    $ cs_active = False
    $ day_time()
    $ set_mode_adv()
    return
