# -*- coding: utf-8 -*-
# Resolves the mod folder at runtime, so the mod works from game/mods/chuzaya_smena
# as well as from a Steam Workshop folder (the workshop uses its own directory name).
init -100 python:
    import os

    cs_probe = "bg/bus_stop.png"
    cs_candidates = []

    # Folder this script was loaded from (works for .rpy and .rpyc alike).
    try:
        cs_here = renpy.get_filename_line()[0].replace("\\", "/")
        cs_candidates.append(cs_here.rsplit("/", 1)[0] + "/" if "/" in cs_here else "")
    except Exception:
        pass

    cs_candidates.append("mods/chuzaya_smena/")

    # Last resort: find the marker file anywhere in the search path.
    try:
        for cs_f in renpy.list_files():
            if cs_f.replace("\\", "/").endswith("/" + cs_probe):
                cs_candidates.append(cs_f.replace("\\", "/")[:-len(cs_probe)])
                break
    except Exception:
        pass

    cs_root = cs_candidates[1]
    for cs_c in cs_candidates:
        if renpy.loadable(cs_c + cs_probe):
            cs_root = cs_c
            break

    def cs_path(p):
        """Re-base a path stored in metadata JSON onto the real mod folder."""
        p = p.replace("\\", "/")
        for prefix in ("mods/chuzaya_smena/",):
            if p.startswith(prefix):
                return cs_root + p[len(prefix):]
        return p
