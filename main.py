import pygame as pgm
from input import Input
import math as maths

class Game():
    #Constructor
    def __init__(e):
        
        #Screen Definitions
        e.screen_width, e.screen_height = 800,600
        e.screen = pgm.display.set_mode((e.screen_width, e.screen_height))
        e.fps = 1
        e.clock = pgm.time.Clock()
        e.screen.fill((255, 255, 255))       

        #Keyboard Definitions
        e.keys = pgm.key.get_pressed()
        e.prevKeys = e.keys

        #Mouse Definitions
        e.mouse = pgm.mouse.get_pressed()
        e.prevMouse = e.mouse
        e.mousePos = pgm.mouse.get_pos()
        e.prevMousePos = e.mousePos
        e.mouseMove = pgm.MOUSEMOTION

        e.posList = []

    #Main function
    def main(e):
        while True:
            e.scourge()

            if e.mouse[0] and e.mousePos not in e.posList: #If the mouse has been clicked and the position is not in the position list
                
                e.posList.append(e.mousePos) #The position is appended to the position list
                
                if e.prevMouse[0]: # Checks if mouse button held down last frame
                    if e.mousePos[0] < e.prevMousePos[0]:
                        e.drawLine(e.mousePos, e.prevMousePos)
                    else:
                        e.drawLine(e.prevMousePos, e.mousePos)

            for pixel in e.posList: 
                e.screen.set_at(pixel, (0, 0, 0))

    def drawLine(e, p1, p2):
        x = p2[0] - p1[0] # difference in x-values
        y = p2[1] - p1[1] # difference in y-values
        
        hyp = maths.sqrt((x*x)+(y*y)) # pythagoras thorem to calculate distance between two points
        unit = [(x/hyp),(y/hyp)] # unit vector (vector divided by magnitude of vector)
        
        v = [p1[0], p1[1]] # set initial position to the first point

        while v[0] < p2[0]: # go down the line by a unit vector until you get to the second point
            v[0] += unit[0] # move along line by one unit vector
            v[1] += unit[1] # same thing but for the y-vlues, you have to do them separately

            rV = [int(v[0]), int(v[1])]
            if rV not in e.posList: e.posList.append(rV)

    #Loop function
    def scourge(e):
        e.first = False
        pgm.display.set_caption("Typetone")
        e.clock.tick(e.fps)
        pgm.display.update()
        e.screen.fill((255, 255, 255))

        for event in pgm.event.get():
            if event == pgm.QUIT:
                exit()
        
        #Values reset after every frame
        e.prevMouse = e.mouse
        e.mouse = pgm.mouse.get_pressed()
        e.prevMousePos = e.mousePos
        e.mousePos = pgm.mouse.get_pos()

        e.prevKeys = e.keys
        e.keys = pgm.key.get_pressed()
 
#Execution
game = Game()
game.main()