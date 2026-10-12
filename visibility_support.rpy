# -*- coding: utf-8 -*-
# Old saves may contain the inherited off-screen anchor from the original left ATL.
init 30 python:
    def cs_repair_loaded_actor_anchor():
        for cs_tag in ("un", "mz"):
            if not renpy.showing(cs_tag):
                continue
            cs_bounds = renpy.get_image_bounds(cs_tag)
            if cs_bounds and (cs_bounds[1] >= config.screen_height or cs_bounds[1] + cs_bounds[3] <= 0):
                cs_attrs = renpy.get_attributes(cs_tag)
                cs_position = cs_actor_far_left if "far" in cs_attrs else cs_actor_left
                renpy.show(" ".join([cs_tag] + list(cs_attrs)), at_list=[cs_position], zorder=10)
    config.after_load_callbacks.append(cs_repair_loaded_actor_anchor)
