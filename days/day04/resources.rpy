# -*- coding: utf-8 -*-
default cs_d4_choice_01_done = False
default cs_d4_choice_04_done = False
default cs_d4_choice_06_done = False
default cs_d4_choice_07_done = False
default cs_d4_choice_08_done = False
default cs_d4_choice_09_done = False
default cs_d4_choice_12_done = False
default cs_d4_da_quiet_evening = False
default cs_d4_da_talked_about_fear = False
default cs_d4_dream_notes_location = None
default cs_d4_dream_phrase_second = False
default cs_d4_dv_mi_compromise = False
default cs_d4_dv_mi_self_decide = False
default cs_d4_elbow_bandage_removed = False
default cs_d4_found_1971_records = False
default cs_d4_heard_unknown_voice = False
default cs_d4_left_note = False
default cs_d4_mz_direct_dream_question = False
default cs_d4_mz_dream_record_written = False
default cs_d4_mz_friend_before_choice = None
default cs_d4_mz_gentle_dream_talk = False
default cs_d4_mz_has_1971_photo = False
default cs_d4_mz_hug_09 = False
default cs_d4_mz_hug_12 = False
default cs_d4_new_book_location = None
default cs_d4_od_direct_question = False
default cs_d4_od_trust_approach = False
default cs_d4_olga_has_undated_photo = False
default cs_d4_photo1971_location = None
default cs_d4_roster_location = None
default cs_d4_scene_cast = []
default cs_d4_se_honest_fear = False
default cs_d4_se_joke_after_bunker = False
default cs_d4_shared_bed = False
default cs_d4_sl_notice_deferred = False
default cs_d4_undated_photo_location = None
default cs_d4_unknown_girl_seen = False
default cs_d4_viola_full_trust = False
default cs_d4_viola_partial_disclosure = False
default cs_day04_done = False
default cs_day04_started = False
init -9 python:
    cs_state_defaults.update(cs_d4_choice_01_done=False, cs_d4_choice_04_done=False, cs_d4_choice_06_done=False, cs_d4_choice_07_done=False, cs_d4_choice_08_done=False, cs_d4_choice_09_done=False, cs_d4_choice_12_done=False, cs_d4_da_quiet_evening=False, cs_d4_da_talked_about_fear=False, cs_d4_dream_notes_location=None, cs_d4_dream_phrase_second=False, cs_d4_dv_mi_compromise=False, cs_d4_dv_mi_self_decide=False, cs_d4_elbow_bandage_removed=False, cs_d4_found_1971_records=False, cs_d4_heard_unknown_voice=False, cs_d4_left_note=False, cs_d4_mz_direct_dream_question=False, cs_d4_mz_dream_record_written=False, cs_d4_mz_friend_before_choice=None, cs_d4_mz_gentle_dream_talk=False, cs_d4_mz_has_1971_photo=False, cs_d4_mz_hug_09=False, cs_d4_mz_hug_12=False, cs_d4_new_book_location=None, cs_d4_od_direct_question=False, cs_d4_od_trust_approach=False, cs_d4_olga_has_undated_photo=False, cs_d4_photo1971_location=None, cs_d4_roster_location=None, cs_d4_scene_cast=[], cs_d4_se_honest_fear=False, cs_d4_se_joke_after_bunker=False, cs_d4_shared_bed=False, cs_d4_sl_notice_deferred=False, cs_d4_undated_photo_location=None, cs_d4_unknown_girl_seen=False, cs_d4_viola_full_trust=False, cs_d4_viola_partial_disclosure=False, cs_day04_done=False, cs_day04_started=False)
init 20 python:
    cs_d4_unknown_girl = Character(u"???", color="#b8a8d8", what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
    cs_d4_voice = Character(None, what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")
image cs_d4_old_ext = im.Scale(cs_resolve_asset("bg/old_camp/old_camp_exterior_morning.png"),1920,1080)
image cs_d4_old_foyer = im.Scale(cs_resolve_asset("bg/old_camp/old_camp_foyer_morning.png"),1920,1080)
image cs_d4_old_corridor = im.Scale(cs_resolve_asset("bg/old_camp/old_camp_corridor_right_turn.png"),1920,1080)
image cs_d4_old_stairs = im.Scale(cs_resolve_asset("bg/old_camp/old_camp_stairwell_down.png"),1920,1080)
image cs_d4_old_door = im.Scale(cs_resolve_asset("bg/old_camp/old_camp_rust_metal_door.png"),1920,1080)
image cs_cg_lena_darya_bunker_reunion = im.Scale(cs_resolve_asset("cg/lena_n_dasha/cg_lena_darya_bunker_reunion_morning.png"),1920,1080)
