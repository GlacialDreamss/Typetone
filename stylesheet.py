import pygame as pgm

class font:
    pgm.font.init()
    text_interface = ()
    text_typing = pgm.font.Font("COMIC.TTF", 10)

class colour:
    interface = (100,100,100)
    brush = ()
    text_interface = (0, 0, 0)
    text_typing = ()

class language:
    print

class interface:
    screen_height = 800
    screen_width = 800