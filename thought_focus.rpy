# -*- coding: utf-8 -*-
# Lena's attention narrows during a long stretch of inner monologue: the people
# around her fade out, and return as soon as someone speaks or the scene moves
# on. A couple of passing thoughts never trigger it. Authored POV shots stay
# in charge; this only ends a shot that it started itself.
default cs_thought_run = 0
default cs_thought_gap = 0
default cs_thought_key = None
default cs_auto_pov = False
default cs_auto_thought_focus = True

init -3 python:
    cs_thought_min_lines = 5     # consecutive thoughts before people fade
    cs_thought_gap_limit = 3     # narration lines in a row that end the monologue

    def cs_thought_reset():
        store.cs_thought_run = 0
        store.cs_thought_gap = 0

    def cs_thought_release():
        if store.cs_auto_pov:
            store.cs_auto_pov = False
            if store.cs_reflective_shot:
                cs_pov_end()
                renpy.transition(cs_sprite_enter)
        cs_thought_reset()

    def cs_thought_focus_at_line(event, **kwargs):
        if event != "begin" or not getattr(store, "cs_active", False):
            return
        if not getattr(store, "cs_auto_thought_focus", True):
            return
        # A scene change or an authored end already restored/cleared the shot.
        if store.cs_auto_pov and (not store.cs_reflective_shot or store.cs_thought_key != store.cs_director_location_key):
            store.cs_auto_pov = False
            cs_thought_reset()
        if store.cs_thought_key != store.cs_director_location_key:
            store.cs_thought_key = store.cs_director_location_key
            cs_thought_reset()
        who = getattr(store, "_last_say_who", None)
        if who == "cs_th":
            store.cs_thought_run += 1
            store.cs_thought_gap = 0
            if (store.cs_thought_run >= cs_thought_min_lines and not store.cs_reflective_shot
                    and any(renpy.showing(t) for t in cs_presence_tags)
                    and not cs_full_frame_cg_showing()):
                cs_pov_begin()
                store.cs_auto_pov = True
                renpy.transition(cs_sprite_leave)
        elif who == "cs_narrator":
            store.cs_thought_gap += 1
            if store.cs_thought_gap >= cs_thought_gap_limit:
                cs_thought_release()
        else:
            cs_thought_release()

init 41 python:
    config.all_character_callbacks.append(cs_thought_focus_at_line)
