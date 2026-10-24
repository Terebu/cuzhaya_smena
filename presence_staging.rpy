# -*- coding: utf-8 -*-
# Explicit authored frames. Never decide visibility from the type of dialogue.
default cs_presence_location = None
default cs_presence_saved = []
default cs_director_location_key = None
default cs_director_people = {}
default cs_director_states = {}
default cs_reflective_shot = False
default cs_pov_return_cast = []
default cs_pov_return_location = None
init -9 python:
    cs_state_defaults.update(cs_pov_return_cast=[], cs_pov_return_location=None)
init -10 python:
    import re
    cs_presence_tags = ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer", "cs_dasha_full", "cs_dasha", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
    cs_director_defaults = {
        "cs_darya": ("cs_darya shrug pioneer normal", "cs_darya_normal_center"),
        "cs_dasha_winter": ("cs_dasha_winter neutral normal", "cs_darya_normal_center"),
        "cs_semen": ("cs_semen neutral pioneer normal", "cs_semen_normal_right"),
        "cs_zhenya": ("cs_zhenya normal pioneer normal", "cs_darya_normal_left"),
        "cs": ("cs custom serious medical normal", "cs_viola_normal_left"),
        "un": ("un normal pioneer", "cs_actor_left"),
        "sl": ("sl normal pioneer", "cs_actor_left"),
        "mt": ("mt normal pioneer", "cs_actor_left"),
        "mi": ("mi normal pioneer", "cs_actor_left"),
        "dv": ("dv normal pioneer", "cs_actor_left"),
        "us": ("us normal pioneer", "cs_actor_left"),
        "sh": ("sh normal pioneer", "cs_actor_left"),
        "el": ("el normal pioneer", "cs_actor_right")}

    def cs_director_remember():
        for tag in cs_presence_tags:
            if renpy.showing(tag):
                # A plain emotion show inherits the live placement but clears
                # get_at_list(). Cache resolved placement, not that empty list.
                current = renpy.game.context().scene_lists.get_displayable_by_tag("master", tag)
                placement = current.get_placement()
                state = getattr(current, "state", None)
                positions = [Transform(alpha=1.0, xpos=placement[0], ypos=placement[1],
                    xanchor=placement[2], yanchor=placement[3],
                    xoffset=placement[4], yoffset=placement[5],
                    zoom=getattr(state, "zoom", 1.0),
                    xzoom=getattr(state, "xzoom", 1.0),
                    yzoom=getattr(state, "yzoom", 1.0))]
                store.cs_director_people[tag] = ((tag,) + tuple(renpy.get_attributes(tag) or ()), positions)
                store.cs_director_states[tag] = "PRESENT_ONSCREEN"

    def cs_full_frame_cg_showing():
        return any(t.startswith("cs_cg_") or t in ("cs_sleep_winter", "cs_sleep_summer", "cs_lena_pioneer_mirror") for t in renpy.get_showing_tags())

    def cs_clear_cg_portraits():
        if not cs_full_frame_cg_showing():
            return False
        cs_director_remember()
        for tag in cs_presence_tags:
            if renpy.showing(tag):
                renpy.hide(tag)
                store.cs_director_states[tag] = "PRESENT_OFFSCREEN"
        return True

    def cs_presence_stage():
        # A later emotion show must not put a standing actor over an illustration.
        if cs_clear_cg_portraits():
            return
        for preferred, old in (("cs_darya", "cs_dasha_winter"), ("cs_darya", "cs_dasha_pioneer"), ("cs_zhenya", "mz")):
            if renpy.showing(preferred) and renpy.showing(old):
                renpy.hide(old)
                store.cs_director_people.pop(old, None)
                store.cs_director_states[old] = "ABSENT"
        tags = [t for t in cs_presence_tags if renpy.showing(t)]
        tags.sort(key=lambda t: (t in ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer"), cs_presence_tags.index(t)))
        n = len(tags)
        if n >= 1:
            for i, tag in enumerate(tags):
                name = (tag,) + tuple(renpy.get_attributes(tag) or ())
                x = 0.5 if n == 1 else ((0.25, 0.75)[i] if n == 2 else (0.18 + 0.64 * i / float(n-1) if n == 3 else 0.14 + 0.72 * i / float(n-1)))
                current = renpy.game.context().scene_lists.get_displayable_by_tag("master", tag)
                placement = current.get_placement()
                state = getattr(current, "state", None)
                # Positioning replaces ATL; do not freeze a half-finished fade.
                # Authored entry/change transitions supply the dissolve.
                renpy.show(name, at_list=[Transform(alpha=1.0, xpos=x, xanchor=0.5,
                    ypos=placement[1], yanchor=placement[3], yoffset=placement[5],
                    zoom=getattr(state, "zoom", 1.0),
                    xzoom=getattr(state, "xzoom", 1.0), yzoom=getattr(state, "yzoom", 1.0))])
        cs_director_remember()

    def cs_frame_focus(tags):
        store.cs_reflective_shot = False
        # A full-frame illustration is already the authored view of the cast.
        # An inherited entry plan must never add standing portraits over it.
        if cs_full_frame_cg_showing():
            tags = []
        cs_director_remember()
        for tag in cs_presence_tags:
            if renpy.showing(tag) and tag not in tags:
                renpy.hide(tag)
                store.cs_director_states[tag] = "PRESENT_OFFSCREEN"
        for tag in tags:
            if renpy.showing(tag):
                continue
            if tag in cs_director_people:
                name, positions = cs_director_people[tag]
            else:
                name, position = cs_director_defaults[tag]
                name = tuple(name.split())
                positions = [getattr(store, position)]
                if not renpy.has_image(name):
                    raise Exception("Missing authored frame image: %r" % (name,))
            renpy.show(name, at_list=positions)
        cs_presence_stage()

    def cs_reflective_focus():
        cs_frame_focus([])
        store.cs_reflective_shot = True

    def cs_pov_begin():
        # An authored inward-looking beat, not an automatic response to narration.
        store.cs_pov_return_cast = [t for t in cs_presence_tags if renpy.showing(t)]
        store.cs_pov_return_location = cs_director_location_key
        cs_reflective_focus()

    def cs_pov_end():
        # A save from an older script may resume after the new begin cue.
        if not cs_pov_return_cast:
            return
        tags = [t for t in cs_pov_return_cast if cs_director_states.get(t) != "ABSENT"]
        if cs_pov_return_location == cs_director_location_key:
            cs_frame_focus(tags)
        store.cs_pov_return_cast = []
        store.cs_pov_return_location = None

    def cs_actor_exit(tags):
        for tag in tags:
            renpy.hide(tag)
            store.cs_director_people.pop(tag, None)
            store.cs_director_states[tag] = "ABSENT"
        cs_presence_stage()

    def cs_director_scene(image):
        store.cs_reflective_shot = False
        store.cs_pov_return_cast = []
        store.cs_pov_return_location = None
        cs_director_remember()
        key = re.sub(r"_(day|sunset|night)$", "", image)
        cg = image.startswith("cs_cg_") or image in ("cs_sleep_winter", "cs_sleep_summer", "cs_lena_pioneer_mirror")
        if image == "black" or (not cg and key != cs_director_location_key):
            store.cs_director_people = {}
            store.cs_director_states = {}
        else:
            for tag in list(cs_director_people):
                store.cs_director_states[tag] = "PRESENT_OFFSCREEN"
        if not cg:
            store.cs_director_location_key = key

    # Legacy script/save entry points: no automatic resurrection of old casts.
    def cs_presence_snapshot(image):
        cs_director_scene(image)
        return []
    def cs_presence_restore(saved):
        return

init 40 python:
    # Repair old CG overlays and center every lone actor after loading saves.
    # Stage preserves the existing vertical placement and scale.
    config.after_load_callbacks.append(cs_presence_stage)
