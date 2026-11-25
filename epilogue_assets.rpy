# -*- coding: utf-8 -*-
# v2: one physical pose, winter + indoor. Replaces the previous art-pack loader.
# Depends on the mod's cs_root, cs_path and cs_dasha_image (init -4).
init -2 python:
    import json
    with renpy.file(cs_root + 'epilogue_assets.json') as cs_ep_asset_file:
        cs_ep_assets = json.load(cs_ep_asset_file)
    for cs_ep_entry in cs_ep_assets['images']:
        cs_ep_art = cs_path(cs_ep_entry['path'])
        if cs_ep_entry['dimensions'] != [1920, 1080]:
            cs_ep_art = im.Scale(cs_ep_art, 1920, 1080)
        renpy.image(cs_ep_entry['id'], cs_ep_art)
    cs_presence_tags += tuple(sorted(set(entry['tag'] for entry in cs_ep_assets['sprites'])))
    for cs_ep_entry in cs_ep_assets['sprites']:
        cs_ep_height = 1560.0
        if cs_ep_entry['character'] == 'sokolova':
            cs_ep_height *= 162.0 / 168.0
        elif cs_ep_entry['character'] == 'semen':
            cs_ep_height = 1580.0
        elif cs_ep_entry['character'] == 'ulyana':
            cs_ep_height *= 0.82
        cs_ep_costume_names = ('winter',) if cs_ep_entry['outfit'] == 'winter' else ('indoor', 'casual', 'home')
        for cs_ep_distance in ('far', 'normal', 'close'):
            cs_ep_displayable = cs_dasha_image(cs_ep_entry, cs_ep_distance, cs_ep_height)
            for cs_ep_costume_name in cs_ep_costume_names:
                cs_ep_name = '%s %s %s' % (cs_ep_entry['tag'], cs_ep_entry['emotion'], cs_ep_costume_name)
                renpy.image(cs_ep_name + ' idle ' + cs_ep_distance, cs_ep_displayable)
                renpy.image(cs_ep_name + ' ' + cs_ep_distance, cs_ep_displayable)
                if cs_ep_distance == 'normal':
                    renpy.image(cs_ep_name + ' idle', cs_ep_displayable)
                    renpy.image(cs_ep_name, cs_ep_displayable)

init 46 python:
    # City portraits share the camp portrait crop; full-height PNGs need
    # an explicit baseline in the common layout director.
    for cs_ep_tag in cs_presence_tags:
        if cs_ep_tag.startswith("cs_epi_"):
            cs_layout_y[cs_ep_tag] = cs_layout_y["cs_darya"]

transform cs_ep_actor_left:
    xalign 0.12
    yanchor 1.0
    ypos 1.60
transform cs_ep_actor_center:
    xalign 0.5
    yanchor 1.0
    ypos 1.60
transform cs_ep_actor_right:
    xalign 0.88
    yanchor 1.0
    ypos 1.60

# Optional: complete 9:16 sprite on a 1920x1080 scene, without portrait cropping.
transform cs_ep_complete_figure:
    xalign 0.5
    yalign 1.0
    zoom 0.56
