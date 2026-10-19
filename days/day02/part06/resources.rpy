# -*- coding: utf-8 -*-
default cs_se_road_day2_awarded = False
default cs_trusted_se_road_day2 = False
default cs_road_loop_observations = 0
default cs_road_notes_written = False
default cs_day02_part06_complete = False
default cs_part06_cast = []
default cs_part06_live = False
default cs_road_visual_trace = []

image cs_road_powerlines_day = im.Scale(cs_root + "bg/road/road_powerlines_day.png", 1920, 1080)
image cs_road_right_bend_day = im.Scale(cs_root + "bg/road/road_right_bend_day.png", 1920, 1080)
# Match the script's right-hand control point without modifying the PNG.
image cs_road_marked_verge_day = im.Flip(im.Scale(cs_root + "bg/road/road_marked_verge_day.png", 1920, 1080), horizontal=True)
image cs_road_left_bend_day = im.Scale(cs_root + "bg/road/road_left_bend_day.png", 1920, 1080)
