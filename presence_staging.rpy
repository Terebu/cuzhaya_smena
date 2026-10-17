# -*- coding: utf-8 -*-
# Explicit authored frames. Never decide visibility from the type of dialogue.
default cs_presence_location = None
default cs_presence_saved = []
default cs_director_location_key = None
default cs_director_people = {}
default cs_director_states = {}
default cs_reflective_shot = False
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
                positions = [Transform(xpos=placement[0], ypos=placement[1],
                    xanchor=placement[2], yanchor=placement[3],
                    xoffset=placement[4], yoffset=placement[5],
                    zoom=getattr(state, "zoom", 1.0),
                    xzoom=getattr(state, "xzoom", 1.0),
                    yzoom=getattr(state, "yzoom", 1.0))]
                store.cs_director_people[tag] = ((tag,) + tuple(renpy.get_attributes(tag) or ()), positions)
                store.cs_director_states[tag] = "PRESENT_ONSCREEN"

    def cs_presence_stage():
        for preferred, old in (("cs_darya", "cs_dasha_winter"), ("cs_darya", "cs_dasha_pioneer"), ("cs_zhenya", "mz")):
            if renpy.showing(preferred) and renpy.showing(old):
                renpy.hide(old)
                store.cs_director_people.pop(old, None)
                store.cs_director_states[old] = "ABSENT"
        tags = [t for t in cs_presence_tags if renpy.showing(t)]
        tags.sort(key=lambda t: (t in ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer"), cs_presence_tags.index(t)))
        n = len(tags)
        if n >= 2:
            for i, tag in enumerate(tags):
                name = (tag,) + tuple(renpy.get_attributes(tag) or ())
                x = (0.25, 0.75)[i] if n == 2 else 0.14 + 0.72 * i / float(n-1)
                current = renpy.game.context().scene_lists.get_displayable_by_tag("master", tag)
                placement = current.get_placement()
                state = getattr(current, "state", None)
                renpy.show(name, at_list=[Transform(xpos=x, xanchor=0.5,
                    ypos=placement[1], yanchor=placement[3], yoffset=placement[5],
                    zoom=getattr(state, "zoom", 1.0),
                    xzoom=getattr(state, "xzoom", 1.0), yzoom=getattr(state, "yzoom", 1.0))])
        cs_director_remember()

    def cs_frame_focus(tags):
        store.cs_reflective_shot = False
        # A full-frame illustration is already the authored view of the cast.
        # An inherited entry plan must never add standing portraits over it.
        if any(t.startswith("cs_cg_") or t in ("cs_sleep_winter", "cs_sleep_summer", "cs_lena_pioneer_mirror") for t in renpy.get_showing_tags()):
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

    def cs_actor_exit(tags):
        for tag in tags:
            renpy.hide(tag)
            store.cs_director_people.pop(tag, None)
            store.cs_director_states[tag] = "ABSENT"
        cs_presence_stage()

    def cs_director_scene(image):
        store.cs_reflective_shot = False
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
