# -*- coding: utf-8 -*-
# Marker-based resource root; works with loose files and Ren'Py archives.
init -1000 python:
    import os as cs_path_os
    cs_asset_marker = "cs_assets_5ea2d086_9903_4ff8_a659.identity"
    cs_asset_roots = set()
    for cs_directory, cs_filename in renpy.loader.listdirfiles():
        if cs_filename.replace("\\", "/").split("/")[-1] == cs_asset_marker:
            if cs_directory is None:
                cs_asset_roots.add((None, cs_filename.rsplit(cs_asset_marker, 1)[0]))
            else:
                cs_physical = cs_path_os.path.normpath(cs_path_os.path.join(cs_directory, cs_path_os.path.dirname(cs_filename)))
                cs_asset_roots.add((cs_path_os.path.normcase(cs_path_os.path.abspath(cs_physical)), None))
    if len(cs_asset_roots) != 1:
        raise Exception("Chuzhaya Smena: expected one asset marker, found %d. Keep one installed copy." % len(cs_asset_roots))
    cs_physical_root, cs_archive_prefix = next(iter(cs_asset_roots))
    if cs_physical_root is not None:
        # Relative to the game's primary loader root, never the process CWD.
        cs_asset_prefix = cs_path_os.path.relpath(cs_physical_root, config.gamedir).replace("\\", "/") + "/"
    else:
        cs_asset_prefix = cs_archive_prefix

    def cs_resolve_asset(path):
        path = path.replace("\\", "/")
        if cs_asset_prefix and path.startswith(cs_asset_prefix):
            return path
        # Compatibility with old save-state strings and generated metadata.
        legacy = "mods/" + "chuzaya_smena/"
        if path.startswith(legacy):
            path = path[len(legacy):]
        if path.startswith("/") or ":" in path or ".." in path.split("/"):
            raise Exception("Invalid mod-relative asset path: %r" % path)
        return cs_asset_prefix + path

    cs_japanese_font = cs_resolve_asset("fonts/NotoSansCJKjp-Regular.otf")

    cs_root = cs_asset_prefix
    def cs_path(path):
        return cs_resolve_asset(path)
