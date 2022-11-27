import math as maths
import pygame as pgm
import pytesseract as pyt
from PIL import Image

from input import Input
from stylesheet import *
from translation import translation

class Game():
    #Constructor
    def __init__(e):
        
        #Screen Definitions    
        e.screen = pgm.display.set_mode((interface.screen_width, interface.screen_height))
        e.image_rect = pgm.Rect(0,20,interface.screen_width,((interface.screen_height*ui_sections.translate_screen_percent)-(interface.screen_height*ui_sections.toolbar_screen_percent))) #Rectangle that represents the area of the screen that can be drawn on
        e.fps = 60 #Greater fps, greater smoothness
        e.clock = pgm.time.Clock()
        e.screen.fill(colour.background)
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

            for pixel in e.posList: 
                #e.screen.set_at(pixel, (0, 0, 0))
                pgm.draw.circle(e.screen,colour.brush,pixel,interface.brush_size)

            if interface.screen_height*ui_sections.toolbar_screen_percent < e.mousePos[1] < interface.screen_height*ui_sections.translate_screen_percent: # If in the designated area for drawing
                if e.mouse[0] and e.mousePos not in e.posList: #If the mouse has been clicked and the position is not in the position list
                    e.posList.append(e.mousePos) #The position is appended to the position list
                    
                    if e.prevMouse[0]: # Checks if mouse button held down last frame
                        if e.mousePos[0] < e.prevMousePos[0]:
                            e.drawLine(e.mousePos, e.prevMousePos)
                        else:
                            e.drawLine(e.prevMousePos, e.mousePos)
                        e.screen_state = e.screen.copy
            
                e.screenshot() #When line is drawn screenshot is taken

    def keyBinds(e):
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

    def drawLine(e, p1, p2): #Bug time: vertical lines cut, I think because the triangle formed between points is so small pixels can't be filled in. 2 If this is the case why doesn't the same happen horizontally 3 Defo here, doesn't make sense to be anywhere else

        x = p2[0] - p1[0] # difference in x-values
        y = p2[1] - p1[1] # difference in y-values
        #if x < 0:
        #    y = 1
        
        
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

    def ui_sections(e):
        for num in range(0, ui_sections.toolbar_section_num): #Toolbar parameters
            e.draw_rect = pgm.draw.rect(e.screen, colour.interface, (ui_sections.toolbar_rect_width*num, 0, ui_sections.toolbar_rect_width, (interface.screen_height*ui_sections.toolbar_screen_percent)), 1, 0, -1, -1, -1, -1) # *percent is for what percentage of the screen is used for the rectangle, hence modularity for different aspect ratios
            e.screen.blit(font.text_interface.render(ui_sections.toolbar_section_list[num], True, colour.text_interface),((ui_sections.toolbar_rect_width*num+200),0)) # 200 is the x coord in a tuple so the text isn't overlaid on the left part of the rect
            for num2 in range(0, ui_sections.toolbar_dropdown_listnum[num]):
                pgm.draw.rect(e.screen, colour.interface, (ui_sections.toolbar_rect_width*num, interface.screen_height*ui_sections.toolbar_screen_percent*(num2+1), ui_sections.toolbar_rect_width, (interface.screen_height*ui_sections.toolbar_screen_percent)), 1, 0, -1, -1, -1, -1)
                #e.screen.blit(font.text_interface.render(ui_sections.toolbar_dropdown_list[num], True, colour.text_interface),((ui_sections.toolbar_rect_width*num+200),0))       
        
        for num in range(0, ui_sections.translate_section_num): # Textbox parameters
            e.draw_rect = pgm.draw.rect(e.screen, colour.interface, (ui_sections.translate_rect_width*num, interface.screen_height-(0.4*interface.screen_height), ui_sections.translate_rect_width, (0.4*interface.screen_height)), 1, 0, -1, -1, -1, -1)
            e.screen.blit(font.text_interface.render(ui_sections.translate_section_list[num], True, colour.text_interface),(((ui_sections.translate_rect_width*num)),(ui_sections.translate_screen_percent*interface.screen_height)+3))
            pgm.draw.rect

    def dropdown(e):
        print
    #def ui_sections(e,): #Make the above stuff modular
    #    for num in range(0, len(sectionListType)):
    #        e.rect = pgm.draw.rect(e.screen, colour.interface, (ui_sections.toolbar_rect_width*num, 0, ui_sections.toolbar_rect_width, 20), 1, 0, -1, -1, -1, -1)
    #        e.screen.blit(font.text_interface.render(ui_sections.toolbar_section_list[num], True, colour.interface),((ui_sections.toolbar_rect_width*num)+80,3))

    def screenshot(e): 
        if e.prevMouse[0] and not e.mouse[0]:
            e.image = e.screen.subsurface(e.image_rect)

            pgm.image.save(e.image,"screenshot.png")
            image = Image.open("screenshot.png")
            text = pyt.image_to_string(image)
            translation.lang_in = text
            image.close()

            print(text)

    #Loop function
    def scourge(e):
        e.icon = pgm.image.load("icon.png").convert()
        pgm.display.set_caption("Typetone")
        pgm.display.set_icon(e.icon)

        e.keyBinds()
        e.clock.tick(e.fps)
        
        
        e.ui_sections()

        pgm.display.update()
        
        e.screen.fill(colour.background)

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