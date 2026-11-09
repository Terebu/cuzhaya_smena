# -*- coding: utf-8 -*-
# 8 November: deterministic sprite layout.
# The previous staging copied the vertical position from the live sprite.
# Right after a show with an ATL transform that placement is still empty, so
# sprites landed at the screen edge (cropped) or at a wrong height. Every actor
# now gets an explicit slot and the baseline of its own sprite set.
default cs_sprite_time_mirror = None

init 45 python:
    # Baselines (ypos with yanchor 1.0) used by the mod's own transforms.
    cs_layout_y = {
        "cs_darya": {"far": 1.35, "normal": 1.60, "close": 1.84},
        "cs_dasha_winter": {"far": 1.35, "normal": 1.60, "close": 1.84},
        "cs_dasha_pioneer": {"far": 1.35, "normal": 1.60, "close": 1.84},
        "cs_dasha_full": {"far": 1.35, "normal": 1.60, "close": 1.84},
        "cs_dasha": {"far": 1.35, "normal": 1.60, "close": 1.84},
        "cs_semen": {"far": 1.35, "normal": 1.60, "close": 1.84},
        "cs_zhenya": {"far": 1.35, "normal": 1.60, "close": 1.84},
        "cs": {"far": 1.31, "normal": 1.48, "close": 1.72},
    }
    # Original Everlasting Summer sprites stand on the bottom edge, as in the game.

    def cs_layout_baseline(tag, attrs):
        table = cs_layout_y.get(tag)
        if not table:
            return 1.0
        size = "far" if "far" in attrs else ("close" if "close" in attrs else "normal")
        return table[size]

    def cs_layout_slots(n):
        if n == 1:
            return [0.5]
        if n == 2:
            return [0.3, 0.7]
        if n == 3:
            return [0.2, 0.5, 0.8]
        return [0.12 + 0.76 * i / float(n - 1) for i in range(n)]

    def cs_presence_stage():
        if not getattr(store, "cs_active", False):
            return
        if cs_clear_cg_portraits():
            return
        for preferred, old in (("cs_darya", "cs_dasha_winter"), ("cs_darya", "cs_dasha_pioneer"), ("cs_zhenya", "mz")):
            if renpy.showing(preferred) and renpy.showing(old):
                renpy.hide(old)
                store.cs_director_people.pop(old, None)
                store.cs_director_states[old] = "ABSENT"
        tags = [t for t in cs_presence_tags if renpy.showing(t)]
        tags.sort(key=lambda t: (t in ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer"), cs_presence_tags.index(t)))
        for x, tag in zip(cs_layout_slots(len(tags)), tags):
            attrs = tuple(renpy.get_attributes(tag) or ())
            y = cs_layout_baseline(tag, attrs)
            current = renpy.game.context().scene_lists.get_displayable_by_tag("master", tag)
            placement = current.get_placement() if current is not None else (None,) * 7
            if (placement[0] == x and placement[2] == 0.5 and placement[1] == y
                    and placement[3] == 1.0 and not placement[4] and not placement[5]):
                continue
            renpy.show((tag,) + attrs, at_list=[Transform(alpha=1.0, xpos=x, xanchor=0.5, ypos=y, yanchor=1.0)])
        cs_director_remember()

    # The interaction hook stored the old function object; point it here.
    config.interact_callbacks[:] = [cs_presence_stage if getattr(f, "__name__", "") == "cs_presence_stage" else f for f in config.interact_callbacks]
    config.after_load_callbacks[:] = [cs_presence_stage if getattr(f, "__name__", "") == "cs_presence_stage" else f for f in config.after_load_callbacks]

    # Newly entering actors appear directly in their final slot: no entry at
    # the left edge followed by a slide to the centre.
    def cs_frame_focus(tags):
        store.cs_reflective_shot = False
        if cs_full_frame_cg_showing():
            tags = []
        cs_director_remember()
        for tag in cs_presence_tags:
            if renpy.showing(tag) and tag not in tags:
                renpy.hide(tag)
                store.cs_director_states[tag] = "PRESENT_OFFSCREEN"
        final = [t for t in cs_presence_tags if t in tags]
        final.sort(key=lambda t: (t in ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer"), cs_presence_tags.index(t)))
        for x, tag in zip(cs_layout_slots(len(final)), final):
            if renpy.showing(tag):
                continue
            if tag in cs_director_people:
                name = tuple(cs_director_people[tag][0])
            else:
                name = tuple(cs_director_defaults[tag][0].split())
                if not renpy.has_image(name):
                    raise Exception("Missing authored frame image: %r" % (name,))
            y = cs_layout_baseline(tag, name[1:])
            renpy.show(name, at_list=[Transform(alpha=1.0, xpos=x, xanchor=0.5, ypos=y, yanchor=1.0)])
        cs_presence_stage()

    # Sprite lighting (day / sunset / night) lives in persistent data, which a
    # save does not carry. Mirror it into the save and restore it on load, so a
    # daytime save never comes back with night-tinted sprites.
    def cs_sprite_time_track():
        if getattr(store, "cs_active", False):
            store.cs_sprite_time_mirror = persistent.sprite_time
    def cs_sprite_time_restore():
        if getattr(store, "cs_active", False) and store.cs_sprite_time_mirror:
            persistent.sprite_time = store.cs_sprite_time_mirror
    config.interact_callbacks.append(cs_sprite_time_track)
    config.after_load_callbacks.insert(0, cs_sprite_time_restore)
