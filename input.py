import pygame as pgm
#import pygame.locals as pl

class Input():
    def __init__(e):
        e.close = pgm.K_ESCAPE
        e.ctrl= pgm.K_LCTRL
        e.shift = pgm.K_LSHIFT
        e.undo = pgm.K_z