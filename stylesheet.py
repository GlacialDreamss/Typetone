import pygame as pgm

class font:
    pgm.font.init()
    text_interface = pgm.font.Font("comic.ttf", 10)
    text_typing = ()

class colour:
    interface = (100,100,100)
    ui = (200, 130, 140)
    brush = (250, 165, 175)

    text_interface = (250, 106, 79)
    text_typing = ()

class language:
    list = ["zh","en"]
    input = 1
    output = 2

class interface:
    screen_height = 800
    screen_width = 1500
    brush_size = 1

class ui_sections: #How can I do modular stuff, make a loop that goes through each section and uses parameters for a standardised structure
    toolbar_section_list = ["File", "Edit", "View", "Custom"]
    toolbar_section_num = len(toolbar_section_list) # On a scale of 1 to 10 how much do I need this and the line below?
    toolbar_rect_width = interface.screen_width/toolbar_section_num

    translate_section_list = ["Input language: "+language.list[0],"Output language: "+language.list[1]]
    translate_section_num = len(translate_section_list)
    translate_rect_width = interface.screen_width/translate_section_num

    total_section_num = 3
