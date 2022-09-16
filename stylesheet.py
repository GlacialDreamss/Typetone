import pygame as pgm

class font:
    pgm.font.init()
    text_interface = pgm.font.Font("comic.ttf", 10)
    text_typing = ()

class colour:
    interface = (100,100,100)
    brush = (200, 70, 10)
    text_interface = (250, 106, 79)
    text_typing = ()

class language:
    print

class interface:
    screen_height = 800
    screen_width = 800
    brush_size = 1

class toolbar:
    section_list = ["File", "Edit", "View", "Custom"]
    section_num = 4
    rect_width = interface.screen_width/section_num

class textbox:
    section_list = ["Input","Language: "+languages[1]+"Output","Language: "+languages[1]]
    languanges = ["zh"]
