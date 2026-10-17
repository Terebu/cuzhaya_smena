# -*- coding: utf-8 -*-
default cs_mz_quiet_visit_seen = False
default cs_mz_reading_invite = False
default cs_reading_book_id = None
default cs_reading_book_location = "library_shelf"
default cs_reading_book_borrowed = False
default cs_reading_live = False
default cs_reading_cast = []

# Legacy alias: the house always stays at its standard scale.
transform cs_reading_desk_focus:
    zoom 1.0
    xalign 0.5
    yalign 0.5
