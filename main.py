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

    #Main function
    def main(e):
        while True:
            e.scourge()

            e.prevKeys = e.keys
            e.keys = pgm.key.get_pressed()

    #Loop function
    def scourge(e):
        while True:
            pgm.display.set_caption("Deez")
            e.clock.tick(e.fps)
            pgm.display.update()

            for event in pgm.event.get():
                if event == pgm.QUIT:
                    exit()
                
                #Somehow need to be able to see line progression and fill in the line. Can see line progression if the pixels are set outside the loop
                if event.type == pgm.MOUSEBUTTONDOWN:
                    print(e.mousePos)
                    print(e.mouse)
                    e.mousePosDown = pgm.mouse.get_pos()
                    e.screen.set_at([e.mousePos[0], e.mousePos[1]], (0, 0, 0))

                if event.type == pgm.MOUSEBUTTONUP:
                    e.mousePosUp = pgm.mouse.get_pos()
                    while e.mousePosUp != e.mousePosDown:
                        e.screen.set_at([e.mousePos[0], e.mousePos[1]], (0, 0, 0))

#Execution
game = Game()
game.main()