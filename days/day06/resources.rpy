# -*- coding: utf-8 -*-
default cs_d5_missing_minute_done = False
default cs_d6_started = False
default cs_d6_done = False
default cs_d6_friend_on_arrival = {}
default cs_d6_choice_results = {}
default cs_d6_help = None
default cs_d6_outfit = 'pioneer'
default cs_d6_room_image = None
default cs_d6_cast = []
default cs_d6_allowed = []
default cs_d6_book_borrowed = False
default cs_d6_book_location = None
default cs_d6_library_key_location = 'olga'
default cs_d6_firstaid_location = 'viola'
default cs_d6_olga_copy = False
default cs_d6_mz_listened = False
default cs_d6_mz_independent = False
default cs_d6_un_independent = False
default cs_d6_un_private = False
default cs_d6_archive_guide = False
default cs_d6_archive_compared = False
default cs_d6_sketch_done = False
default cs_d6_mz_address_received = False
default cs_d6_se_address_offered = False
default cs_d6_se_address_received = False
default cs_d6_un_sketch_received = False
default cs_d6_sl_badge_received = False
default cs_d6_dv_pick_received = False
default cs_d6_mi_music_received = False
default cs_d6_mi_known_motif = False
default cs_d6_mi_motif_tried = False
default cs_d6_se_account_received = False
default cs_d6_se_agency = False
default cs_d6_place_recorded = False
default cs_d6_bus_departed = False
default cs_d6_towels_carried = False
default cs_d6_viola_documents_shared = False
default cs_d6_fifth_tray_locked = False
default cs_d6_items_packed = False
init -9 python:
    cs_state_defaults.update(cs_d5_missing_minute_done=False,cs_d6_started=False,cs_d6_done=False,cs_d6_friend_on_arrival={},cs_d6_choice_results={},cs_d6_help=None,cs_d6_outfit='pioneer',cs_d6_room_image=None,cs_d6_cast=[],cs_d6_allowed=[],cs_d6_book_borrowed=False,cs_d6_book_location=None,cs_d6_library_key_location='olga',cs_d6_firstaid_location='viola',cs_d6_olga_copy=False,cs_d6_mz_listened=False,cs_d6_mz_independent=False,cs_d6_un_independent=False,cs_d6_un_private=False,cs_d6_archive_guide=False,cs_d6_archive_compared=False,cs_d6_sketch_done=False,cs_d6_mz_address_received=False,cs_d6_se_address_offered=False,cs_d6_se_address_received=False,cs_d6_un_sketch_received=False,cs_d6_sl_badge_received=False,cs_d6_dv_pick_received=False,cs_d6_mi_music_received=False,cs_d6_mi_known_motif=False,cs_d6_mi_motif_tried=False,cs_d6_se_account_received=False,cs_d6_se_agency=False,cs_d6_place_recorded=False,cs_d6_bus_departed=False,cs_d6_towels_carried=False,cs_d6_viola_documents_shared=False,cs_d6_fifth_tray_locked=False,cs_d6_items_packed=False)
image cs_cg_day06_blank_pages_morning = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_blank_pages_morning.png"),1920,1080)
image cs_cg_day06_semen_farewell_day = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_semen_farewell_day.png"),1920,1080)
image cs_cg_day06_archive_comparison_day = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_archive_comparison_day.png"),1920,1080)
image cs_cg_day06_pier_evening = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_pier_evening.png"),1920,1080)
image cs_cg_day06_fifth_place_intact = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_fifth_place_intact.png"),1920,1080)
image cs_cg_day06_fifth_place_changed = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_fifth_place_changed.png"),1920,1080)
image cs_cg_day06_separate_beds_night = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_separate_beds_night.png"),1920,1080)
image cs_cg_day06_drawing_by_library = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_drawing_by_library.png"),1920,1080)
image cs_cg_day06_semen_bus_wave = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_semen_bus_wave.png"),1920,1080)
image cs_cg_day06_cards_four = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_cards_four.png"),1920,1080)
image cs_cg_day06_fifth_place_tray = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day06_fifth_place_tray.png"),1920,1080)
image cs_cg_day05_missing_minute = im.Scale(cs_resolve_asset("cg/day06_cg_fullhd/cg/cg_day05_missing_minute.png"),1920,1080)
# -*- coding: utf-8 -*-
# State belongs to the playthrough; replaying a checkpoint never awards twice.
# The lamp is off: no illuminated artwork remains visible behind the voices.
image cs_d6_lights_out = Solid("#000")
image cs_d6_pier_sunset = im.MatrixColor("images/bg/ext_boathouse_day.jpg", im.matrix.tint(1.0,0.83,0.70) * im.matrix.brightness(-0.08))
image cs_d6_washstand_night = im.MatrixColor("images/bg/ext_washstand_day.jpg", im.matrix.tint(0.65,0.72,0.90) * im.matrix.brightness(-0.28))
init 60 python:
    cs_d6_driver = Character(u"Пётр, водитель", color="#aebbc9", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
    cs_d6_tags = {'da':'cs_darya','sy':'cs_semen','mz':'cs_zhenya','un':'un','sl':'sl','dv':'dv','mi':'mi','mt':'mt','vi':'cs'}

    def cs_d6_begin():
        if not cs_d6_started:
            store.cs_d6_friend_on_arrival = {key:getattr(store,'cs_friend_'+key) for key in ('da','mz','se','un','sl','dv','mi','viola')}
        store.cs_d6_started = True
        store.cs_d5_quiet = False
        store.cs_d5_scene = 0
        store.cs_d5_dressed = True
        store.cs_day03_started = True
        store.cs_rev_active = False
        cs_bus_cue('calm')
        renpy.music.stop(channel='cs_sports',fadeout=0.5)
        for screen in ('cs_day05_end_screen','cs_d5_clock_face','cs_d5_insert','cs_d5_notes'):
            renpy.hide_screen(screen)

    def cs_d6_before(key):
        return cs_d6_friend_on_arrival.get(key,0)

    def cs_d6_choose(number, option):
        rewards = {1:('mz',None),2:('sl','dv','mi'),3:('se',None),4:('da',None)}
        ledger = dict(cs_d6_choice_results)
        old = ledger.get(number)
        if old != option:
            if old is not None and rewards[number][old]:
                name='cs_friend_'+rewards[number][old]
                setattr(store,name,getattr(store,name)-1)
            if rewards[number][option]:
                name='cs_friend_'+rewards[number][option]
                setattr(store,name,getattr(store,name)+1)
        ledger[number]=option
        store.cs_d6_choice_results=ledger
        if number==1: store.cs_d6_mz_listened=option==0
        elif number==2: store.cs_d6_help=('sl','dv','mi')[option]
        elif number==3: store.cs_d6_se_agency=option==0
        elif number==4: store.cs_d6_place_recorded=option==0

    def cs_d6_costume(costume):
        visible=renpy.showing('cs_darya') and costume!=cs_d6_outfit
        if visible:renpy.with_statement(None)
        store.cs_d6_outfit=costume
        cs_d5_costume(costume)
        if visible:renpy.with_statement(Dissolve(0.4))

    def cs_d6_room(image, allowed=None):
        if not renpy.has_image(tuple(image.split()),exact=True):
            raise Exception('Missing Day 6 image: '+image)
        if allowed is not None:
            store.cs_d6_allowed=list(allowed)
        renpy.with_statement(None)
        cs_director_scene(image)
        renpy.scene()
        renpy.show(image)
        store.cs_d6_room_image=image
        store.cs_d6_cast=[]
        cs_d6_costume(cs_d6_outfit)
        cs_d6_music_for_room(image)
        renpy.with_statement(Dissolve(0.55))

    def cs_d6_cg(image):
        if not renpy.has_image(tuple(image.split()),exact=True):
            raise Exception('Missing Day 6 CG: '+image)
        renpy.with_statement(None)
        cs_director_scene(image)
        renpy.scene()
        renpy.show(image)
        renpy.with_statement(Dissolve(0.7))

    def cs_d6_focus(speaker):
        if cs_full_frame_cg_showing(): return
        # Both girls are in bed; a voice in the dark has no standing portrait.
        if cs_d6_room_image=='cs_d6_lights_out':return
        if speaker=='driver':
            # The driver has no portrait. Do not leave a previous interlocutor
            # standing in for his offscreen voice.
            cs_d6_think()
            return
        tag=cs_d6_tags.get(speaker)
        if tag:
            if tag not in cs_d6_allowed:
                raise Exception('Absent Day 6 speaker: '+speaker+' in '+cs_d6_room_image)
            # Day 5 rule: current speaker first, then the preceding partner.
            # A new exchange after a background shot starts with one actor.
            previous=[t for t in cs_d6_cast if t in cs_d6_allowed]
            cast=[tag]
            if previous and previous[0]!=tag:cast.append(previous[0])
            store.cs_d6_cast=cast
        elif speaker!='ls': return
        cast=[t for t in cs_d6_cast if t in cs_d6_allowed]
        before=set(t for t in cs_presence_tags if renpy.showing(t))
        if before!=set(cast):renpy.with_statement(None)
        cs_frame_focus(cast)
        if before!=set(cast): renpy.with_statement(Dissolve(0.4))

    def cs_d6_think():
        # Physical presence is separate from Lena's current conversation.
        store.cs_d6_cast=[]
        if not cs_full_frame_cg_showing() and not cs_reflective_shot:
            renpy.with_statement(None)
            cs_pov_begin()
            renpy.with_statement(Dissolve(0.4))

    def cs_d6_music_for_room(image):
        # A brief look into the parked bus preserves its scene's score.
        # Lights out must not restart the music already fading before sleep.
        if image in ('bg int_bus','cs_d6_lights_out'):return
        # Change at dramatic/location boundaries; CGs retain their scene's cue.
        if image.startswith(('cs_d4_old_','bg int_catacombs')):
            renpy.music.stop(channel='music',fadeout=1.5)
            return
        if image.startswith('bg int_dining_hall') and cs_d6_bus_departed:
            renpy.music.stop(channel='music',fadeout=1.5)
            return
        if image.startswith('cs_house_lena_darya_int') and image.endswith('night'):track=cs_music_After_Hours
        elif image=='cs_d6_pier_sunset':track=cs_music_calm
        elif image.startswith('bg int_library'):track=cs_day_music_think
        elif image.startswith('bg ext_house_of_mt_sunset'):track=cs_day_music_home
        elif image in ('bg ext_bus','bg ext_no_bus'):track=cs_day_music_home
        elif image in ('cs_d6_washstand_night','bg ext_library_night'):return
        elif image=='bg int_musclub_day':
            renpy.music.stop(channel='music',fadeout=1.0)
            return
        else:track=cs_day_music_daily
        cs_rev_music(track,0.18,2.0)

    cs_d6_original_volume=cs_bus_audio_ambient_volume
    def cs_d6_ambient_volume(target):
        if cs_active and cs_d6_started and target and target!=cs_bus_drone:return 0.28
        return cs_d6_original_volume(target)
    cs_bus_audio_ambient_volume=cs_d6_ambient_volume

    cs_d6_original_audio_target=cs_day03_audio_target
    def cs_d6_audio_target(image):
        if cs_d6_started:
            if image=='cs_d6_lights_out':return 'sound/ambiences/int_cabin_night.ogg'
            if image.startswith('cs_house_lena_darya_int'):
                return 'sound/ambiences/int_cabin_night.ogg' if image.endswith('night') else 'sound/ambiences/int_cabin_day.ogg'
            if image.startswith('cs_cg_') and cs_d6_room_image=='cs_house_lena_darya_int_night':
                return 'sound/ambiences/int_cabin_night.ogg'
            if image=='cs_d6_pier_sunset':return 'sound/ambiences/lake_shore_evening.ogg'
            if image=='cs_d6_washstand_night':return 'sound/ambiences/forest_night.ogg'
            if image.startswith('cs_cg_'):return False
            if cs_d6_bus_departed:
                if image.startswith('bg int_dining_hall'):return None
                if image.startswith(('bg ext_','cs_camp_path_','cs_house_lena_darya_ext_','cs_library_exterior_')):
                    if image.startswith('bg ext_boathouse'):return 'sound/ambiences/lake_shore_evening.ogg'
                    return 'sound/ambiences/forest_night.ogg' if image.endswith('night') else 'sound/ambiences/forest_day.ogg'
        return cs_d6_original_audio_target(image)
    cs_day03_audio_target=cs_d6_audio_target

    def cs_d6_loaded():
        if not cs_active or not cs_d6_started:return
        store.cs_d5_quiet=False
        store.cs_d5_scene=0
        store.cs_bus_audio_mode='natural'
        renpy.music.stop(channel='cs_sports')
        if not cs_full_frame_cg_showing() and renpy.showing('cs_darya'):
            attrs=renpy.get_attributes('cs_darya') or ()
            if cs_d6_outfit not in attrs:cs_d6_costume(cs_d6_outfit)
    config.after_load_callbacks.append(cs_d6_loaded)

screen cs_day06_end_screen():
    modal True
    frame:
        align (0.5,0.5)
        padding (32,24)
        background Solid('#142821ed')
        vbox:
            spacing 16
            text 'Конец шестого дня' size 32
            text 'Продолжение следует' size 24
            textbutton 'Сохранить игру' action ShowMenu('save')
            textbutton 'Загрузить игру' action ShowMenu('load')
            textbutton 'Главное меню' action [Function(cs_restore_audio),MainMenu()]
