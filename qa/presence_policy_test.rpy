# -*- coding: utf-8 -*-
label cs_qa_presence_fixture:
    $ cs_active = True
    stop music
    stop ambience
    $ cs_presence_location = None
    $ cs_presence_saved = cs_presence_snapshot("bg int_library_day")
    scene bg int_library_day
    $ cs_presence_restore(cs_presence_saved)
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    cs_narrator "Камера библиотеки."
    label cs_check_presence_seated:
    cs_narrator "Они сели рядом."
    $ cs_presence_saved = cs_presence_snapshot("bg int_library_day")
    scene bg int_library_day
    $ cs_presence_restore(cs_presence_saved)
    label cs_check_presence_same_room:
    cs_narrator "Пауза в разговоре."
    show cs_semen smile pioneer normal at cs_semen_normal_right
    show un smile pioneer at cs_actor_left
    show mi happy pioneer at cs_actor_right
    $ cs_presence_stage()
    label cs_check_presence_group:
    cs_narrator "Общий ракурс."
    $ cs_presence_saved = cs_presence_snapshot("bg ext_square_day")
    scene bg ext_square_day
    $ cs_presence_restore(cs_presence_saved)
    label cs_check_presence_new_location:
    cs_narrator "Другая локация."
    return

testcase cs_presence_policy:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    run Start("cs_qa_presence_fixture")
    click until label cs_check_presence_seated
    pause 1.0
    assert renpy.showing("cs_darya") and renpy.showing("cs_zhenya")
    $ cs_qa_presence_before = renpy.get_image_bounds("cs_darya")
    $ cs_qa_capture("presence_seated")
    click until label cs_check_presence_same_room
    pause 1.0
    assert renpy.showing("cs_darya") and renpy.showing("cs_zhenya")
    $ renpy.take_screenshot()
    $ renpy.save("cs_presence_same_room")
    $ renpy.load("cs_presence_same_room")
    pause 0.6
    assert renpy.showing("cs_darya") and renpy.showing("cs_zhenya")
    click until label cs_check_presence_group
    pause 1.0
    assert len([t for t in cs_presence_tags if renpy.showing(t)]) == 5
    $ cs_qa_presence_after = renpy.get_image_bounds("cs_darya")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/presence_bounds.json", "w").write(json.dumps(dict(before=cs_qa_presence_before, after=cs_qa_presence_after)))
    assert cs_qa_presence_before[1] == cs_qa_presence_after[1] and cs_qa_presence_before[3] == cs_qa_presence_after[3]
    $ cs_qa_capture("presence_group_five")
    click until label cs_check_presence_new_location
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_presence_policy_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_night_camera_fixture:
    $ cs_active = True
    stop music
    stop ambience
    scene cs_house_lena_darya_int_night at cs_reading_desk_focus
    call cs_day02_71
    call cs_day02_72
    call cs_day02_73
    call cs_day02_74
    label cs_check_night_camera_end:
    pause
    return

testcase cs_night_camera:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    run Start("cs_qa_night_camera_fixture")
    click until label cs_check_finale_72
    pause 1.0
    $ cs_qa_capture("night_full_room_fixed")
    assert renpy.showing("cs_darya")
    click until label cs_check_night_camera_end
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("night_bedtime_portrait_kept")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_night_camera_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_old_house_camera:
    $ cs_active = True
    stop music
    stop ambience
    cs_narrator "Подготовка старого сохранения."
    scene cs_house_lena_darya_int_day at Transform(zoom=2.2, xalign=0.5, yalign=0.8)
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    # Save before the next interaction: simulate an old slot without mutating
    # the updated runtime's callback configuration.
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/house_camera_old_bounds.json", "w").write(json.dumps(renpy.get_image_bounds("cs_house_lena_darya_int_day")))
    $ renpy.take_screenshot()
    $ renpy.save("cs_house_old_camera")
    label cs_check_house_old_slot_ready:
    pause
    return

testcase cs_house_camera_load:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/main_menu_audio.json", "w").write(json.dumps(dict(config_music=config.main_menu_music, music=renpy.music.get_playing(), ambience=renpy.music.get_playing(channel="ambience"))))
    run Start("cs_qa_old_house_camera")
    click until label cs_check_house_old_slot_ready
    run Function(renpy.load, "cs_house_old_camera")
    pause 1.0
    $ cs_qa_house_bounds = renpy.get_image_bounds("cs_house_lena_darya_int_day")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/house_camera_bounds.json", "w").write(json.dumps(cs_qa_house_bounds))
    assert abs(cs_qa_house_bounds[2] - 1920) < 1 and abs(cs_qa_house_bounds[3] - 1080) < 1
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("house_standard_after_old_save")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_house_camera_load_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_menu_audio_guard:
    $ cs_active = True
    $ main_menu = False
    $ _main_menu = False
    $ renpy.music.play(config.main_menu_music, channel="music")
    $ renpy.music.play(config.main_menu_music, channel="ambience")
    $ cs_silence_menu_audio()
    cs_narrator "Без звука главного меню."
    pause
    return

testcase cs_menu_audio_guard:
    pause 1.0
    run Start("cs_qa_menu_audio_guard")
    pause 1.0
    assert renpy.music.get_playing() != config.main_menu_music
    assert renpy.music.get_playing(channel="ambience") != config.main_menu_music
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_menu_audio_guard_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
