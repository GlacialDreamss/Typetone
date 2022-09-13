from ast import Mod
import math as maths
from operator import mod
import pygame as pgm
import stylesheet

from input import Input


class Game():
    #Constructor
    def __init__(e):
        
        #Screen Definitions    
        e.screen = pgm.display.set_mode((stylesheet.interface.screen_width, stylesheet.interface.screen_height))
        e.fps = 30
        e.clock = pgm.time.Clock()
        e.screen.fill((255, 255, 255))
        e.screen_state = e.screen
        e.prevScreen_state = e.screen_state

        #Keyboard Definitions
        e.kb = Input()
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
                    e.screen_state = e.screen.copy

            for pixel in e.posList: 
                #e.screen.set_at(pixel, (0, 0, 0))
                pgm.draw.circle(e.screen,stylesheet.colour.brush,pixel,stylesheet.interface.brush_size)
                
            
            #Keybinds Stuff
            if e.keys[e.kb.close]:
                exit()
            
            if e.keys[e.kb.ctrl]:
                if e.keys[e.kb.undo] and not e.prevKeys[e.kb.undo]:
                    print("Undo placeholder")
                    print(e.screen_state.get_size())
                    #e.screen_state.blit(e.screen,[0, 0])

            if e.keys[e.kb.shift]:
                if e.keys[e.kb.undo] and not e.prevKeys[e.kb.undo]:
                    print("Redo placeholder")
                

    def drawLine(e, p1, p2): 
        x = p2[0] - p1[0] # difference in x-values
        y = p2[1] - p1[1] # difference in y-values
        
        hyp = maths.sqrt((x*x)+(y*y)) # pythagoras thorem to calculate distance between two points
        unit = [(x/hyp),(y/hyp)] # unit vector (vector divided by magnitude of vector)
        
        v = [p1[0], p1[1]] # set initial position to the first point

        while v[0] < p2[0]: # go down the line by a unit vector until you get to the second point
            v[0] += unit[0] # move along line by one unit vector
            v[1] += unit[1] # same thing but for the y-values, you have to do them separately

            rV = [int(v[0]), int(v[1])] 
            if rV not in e.posList: e.posList.append(rV)

    def plans(e):
        print
        #Brainstorming how to undo, realised an entire function isn't necessary
            #Can't just remove previous points as they are already definite
            #Can't just white them out as they may overlap

            #If saving the state of the screen after the mouse is lifted is possible then it should hopefully be simple enough

            #Could instead save a prevPos list from when the mouse is lifted, updating the screen and redrawing what was last drawn using pixelcopy. But like no

            #Toolbar should be simple enough, use rectangles positioned from 0,0 to whatever. Getting dropdowns and the actual functions to work might be an issue

            #Must avoid joining the flying spaghetti code monster cult :)
        #Text boxes and toolbar
            #Main problem - they have to change size
            #Solution - percentage based dimensions
            #Issues - have to limit the dimensions of the program so there is no overflow (like how this line carried over)
    
    def toolbarSections(num):
        num = 10 #Number of toolbar sections
        textList = ["File", "Edit", "View", "Custom"] #List of the different sections of the toolbar
        rectValue = stylesheet.interface.screen_width / len(textList)
        #Make a function that collects parameters from a list and can be used in the toolbar function to print out the words for each section in the toolbar
        print

    def toolbar(e):
        #e.rect = pgm.draw.rect(e.screen, stylesheet.colour.interface, (0, 0, 200, 100), 1, 10, 10, 10, 10, 10)
        #e.screen.blit(stylesheet.font.text_interface.render("pleasework", True, stylesheet.colour.interface),(0,0))
        for num in range(0, e.toolbarSections(num)):
            e.rect = pgm.draw.rect(e.screen, stylesheet.colour.interface, (0, 0, 200, 100), 1, 10, 10, 10, 10, 10) #Make parameters increment to fill the width based on the number of toolbar sections
            e.screen.blit(stylesheet.font.text_interface.render(e.toolbarSections(), True, stylesheet.colour.interface),(0,0)) #Don't think you can reference variables in a separate function so uh stylesheet this stuff ig. Gl



    def textbox(e):
        print

    #Loop function
    def scourge(e):
        e.icon = pgm.image.load("icon.png").convert()
        pgm.display.set_caption("Typetone")
        pgm.display.set_icon(e.icon)

        e.clock.tick(e.fps)
        
        
        e.toolbar()

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

        e.prevScreen_state = e.screen_state
 
#Execution
game = Game()
game.main()