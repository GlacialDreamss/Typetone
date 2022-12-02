import pygame as pgm

class font:
    pgm.font.init()
    text_interface = pgm.font.Font("comic.ttf", 20)
    text_typing = ()

class colour:
    interface = (100,100,100)
    background = (220, 210, 220)
    toolbar = (0, 0, 0)
    texbox = (0, 0, 0)
    
    ui = (200, 130, 140)
    brush = (200, 165, 175)

    text_interface = (0, 0, 0)
    text_typing = ()

class language:
    input = "en"
    output = "zh"

class interface:
    screen_height = 800
    screen_width = 1500
    brush_size = 1

class ui_sections: #How can I do modular stuff, make a loop that goes through each section and uses parameters for a standardised structure
    toolbar_section_list = ["File", "View", "History", "Custom"]
    toolbar_section_num = len(toolbar_section_list) # On a scale of 1 to 10 how much do I need this and the line below?
    toolbar_rect_width = interface.screen_width/toolbar_section_num
    toolbar_screen_percent = 0.022
    toolbar_dropdown_list = [["Import", "Export"], ["Fullscreen", "Windowed"], [], ["Colour", "Text", "Voice"]]
    toolbar_dropdown_listnum = [2, 3, 1, 3]

    translate_section_list = ["Input language: "+language.input,"Output language: "+language.output]
    translate_section_num = len(translate_section_list)
    translate_rect_width = interface.screen_width/translate_section_num
    translate_screen_percent = 0.6

    total_section_num = 3
