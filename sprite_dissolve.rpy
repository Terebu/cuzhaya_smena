# -*- coding: utf-8 -*-
# Shared scene, CG and portrait dissolves for every day, including Python directors.
# Only master is blended: the dialogue window stays visible and unchanged.
init 200 python:
    renpy.cs_sprite_last_frame = None
    renpy.cs_sprite_fade_count = 0
    renpy.cs_cg_fade_count = 0
    renpy.cs_background_fade_count = 0
    renpy.cs_sprite_skip_loaded = False
    def cs_sprite_fade_reset():
        renpy.cs_sprite_last_frame = None
        renpy.cs_sprite_skip_loaded = False

    def cs_cg_frame_signature():
        return tuple(sorted((tag, tuple(renpy.get_attributes(tag) or ()))
            for tag in renpy.get_showing_tags()
            if tag.startswith('cs_cg_') or tag in
                ('cs_sleep_winter', 'cs_sleep_summer', 'cs_lena_pioneer_mirror')))

    def cs_sprite_fade_schedule(cg_transition=None):
        if not getattr(store,'cs_active',False):
            cs_sprite_fade_reset()
            return
        cs_presence_stage()
        backgrounds=tuple(sorted((tag,tuple(renpy.get_attributes(tag) or ()))
            for tag in renpy.get_showing_tags() if tag not in cs_presence_tags and tag not in ('cs_snow', 'cs_windshield')))
        actors=[]
        for tag in cs_presence_tags:
            if renpy.showing(tag):
                displayable=renpy.game.context().scene_lists.get_displayable_by_tag('master',tag)
                actors.append((tag,tuple(renpy.get_attributes(tag) or ()),tuple(displayable.get_placement())))
        cgs=cs_cg_frame_signature()
        frame=(backgrounds,tuple(actors),cgs)
        previous=renpy.cs_sprite_last_frame
        renpy.cs_sprite_last_frame=frame
        if renpy.cs_sprite_skip_loaded:
            renpy.cs_sprite_skip_loaded=False
            return
        previous_cgs=previous[2] if previous is not None else ()
        if previous_cgs != cgs:
            # Blend the illustration itself, including a CG-to-CG change or
            # the return to a room with no portraits. Keep authored long fades.
            duration=max(0.7, getattr(cg_transition, 'time', 0.0))
            renpy.transition(Dissolve(duration), layer='master', always=True)
            renpy.cs_cg_fade_count+=1
            return
        if cgs:return
        previous_backgrounds=previous[0] if previous is not None else ()
        if previous_backgrounds != backgrounds:
            # Includes attributes of the stock bg tag, custom locations,
            # disappearance to an empty scene and either side of black.
            duration=max(0.7, getattr(cg_transition, 'time', 0.0))
            renpy.transition(Dissolve(duration), layer='master', always=True)
            renpy.cs_background_fade_count+=1
            return
        previous_actors=previous[1] if previous is not None else ()
        if previous_actors!=frame[1]:
            renpy.transition(Dissolve(0.35),layer='master',always=True)
            renpy.cs_sprite_fade_count+=1
    def cs_sprite_fade_at_line(event, **kwargs):
        if event == 'begin':cs_sprite_fade_schedule()
    config.all_character_callbacks.append(cs_sprite_fade_at_line)
    # Runs before Ren'Py consumes pending transitions, unlike interact_callbacks.
    # Covers a plain scene/show/hide followed by a pause or a menu, with no Say.
    def cs_scene_fade_before_interact():
        if (getattr(store, 'cs_active', False)
                and not getattr(store, 'main_menu', False)
                and not getattr(store, '_main_menu', False)
                and not renpy.config.skipping):
            cs_sprite_fade_schedule()
    config.start_interact_callbacks.append(cs_scene_fade_before_interact)

    # Python frame directors can execute with None (or a disabled explicit
    # transition) before the next Say callback. Queue the master dissolve
    # before with_none commits that new frame as its own transition source.
    # A pending layer transition keeps master out of with_none's snapshot.
    cs_sprite_previous_with_callback = config.with_callback
    def cs_sprite_fade_at_with(trans, paired):
        if cs_sprite_previous_with_callback:
            trans = cs_sprite_previous_with_callback(trans, paired)
        if (getattr(store, 'cs_active', False)
                and not getattr(store, "main_menu", False)
                and not getattr(store, "_main_menu", False)
                and not renpy.config.skipping):
            cs_sprite_fade_schedule(cg_transition=trans)
        return trans
    config.with_callback = cs_sprite_fade_at_with
    def cs_sprite_fade_after_load():
        cs_sprite_fade_reset()
        renpy.cs_sprite_skip_loaded=True
    config.after_load_callbacks.append(cs_sprite_fade_after_load)
    config.start_callbacks.append(cs_sprite_fade_reset)
