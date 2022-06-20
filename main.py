import pygame as pgm
from input import Input

class Game():
    #Constructor
    def __init__(e):
        
        #Screen Definitions
        e.screen_width, e.screen_height = 192,108
        e.screen = pgm.display.set_mode((e.screen_width, e.screen_height))
        e.fps = 24
        e.clock = pgm.time.Clock()
        e.screen.fill((255, 255, 255))       

        #Keyboard Definitions
        e.keys = pgm.key.get_pressed()
        e.prevKeys = e.keys

        #Mouse Definitions
        e.mouse = pgm.mouse.get_pressed()
        e.mousePos = pgm.mouse.get_pos()

        e.posList = []

    #Main function
    def main(e):
        while True:
            e.scourge()
            if e.mouse[0] and e.mousePos not in e.posList: e.posList.append(e.mousePos)
            for pixel in e.posList: 
                #e.screen.set_at(pixel, (0, 0, 0))
                pgm.draw.aaline(pgm.display,(0, 0, 0),pixel,pixel,int = 1)

    #Loop function
    def scourge(e):
        pgm.display.set_caption("Typetone")
        e.clock.tick(e.fps)
        pgm.display.update()
        e.screen.fill((255, 255, 255))

        for event in pgm.event.get():
            if event == pgm.QUIT:
                exit()

        e.mouse = pgm.mouse.get_pressed()
        e.mousePos = pgm.mouse.get_pos()

        e.prevKeys = e.keys
        e.keys = pgm.key.get_pressed()
 
#Execution
game = Game()
game.main()