import math as maths
import pygame as pgm
import stylesheet
import tesseract

from input import Input


class Game():
    #Constructor
    def __init__(e):
        
        #Screen Definitions    
        e.screen = pgm.display.set_mode((stylesheet.interface.screen_width, stylesheet.interface.screen_height))
        e.image_rect = pgm.Rect(0,20,stylesheet.interface.screen_width,((stylesheet.interface.screen_height*stylesheet.ui_sections.translate_screen_percent)-(stylesheet.interface.screen_height*stylesheet.ui_sections.toolbar_screen_percent))) #Rectangle that represents the area of the screen that can be drawn on
        e.fps = 144 #Greater fps, greater smoothness
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
            if stylesheet.interface.screen_height*stylesheet.ui_sections.toolbar_screen_percent < e.mousePos[1] < stylesheet.interface.screen_height*stylesheet.ui_sections.translate_screen_percent: # If in the designated area for drawing
                if e.mouse[0] and e.mousePos not in e.posList: #If the mouse has been clicked and the position is not in the position list
                    e.posList.append(e.mousePos) #The position is appended to the position list
                    
                    if e.prevMouse[0]: # Checks if mouse button held down last frame
                        if e.mousePos[0] < e.prevMousePos[0]:
                            e.drawLine(e.mousePos, e.prevMousePos)
                        else:
                            e.drawLine(e.prevMousePos, e.mousePos)
                        e.screen_state = e.screen.copy
                        e.screenshot() #When line is drawn screenshot is taken


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
                

    def drawLine(e, p1, p2): #Bug time: vertical lines cut, I think because the triangle formed between points is so small pixels can't be filled in. 2 If this is the case why doesn't the same happen horizontally

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

    def ui_sections(e):
        for num in range(0, stylesheet.ui_sections.toolbar_section_num): #Toolbar parameters
            e.rect = pgm.draw.rect(e.screen, stylesheet.colour.interface, (stylesheet.ui_sections.toolbar_rect_width*num, 0, stylesheet.ui_sections.toolbar_rect_width, (stylesheet.interface.screen_height*stylesheet.ui_sections.toolbar_screen_percent)), 1, 0, -1, -1, -1, -1) # *percent is for what percentage of the screen is used for the rectangle, hence modularity for different aspect ratios
            e.screen.blit(stylesheet.font.text_interface.render(stylesheet.ui_sections.toolbar_section_list[num], True, stylesheet.colour.interface),((stylesheet.ui_sections.toolbar_rect_width*num),3)) # 3 is so the text isn't overlaid on the line
        
        for num in range(0, stylesheet.ui_sections.translate_section_num): # Textbox parameters
            e.rect = pgm.draw.rect(e.screen, stylesheet.colour.interface, (stylesheet.ui_sections.translate_rect_width*num, stylesheet.interface.screen_height-(0.4*stylesheet.interface.screen_height), stylesheet.ui_sections.translate_rect_width, (0.4*stylesheet.interface.screen_height)), 1, 0, -1, -1, -1, -1)
            e.screen.blit(stylesheet.font.text_interface.render(stylesheet.ui_sections.translate_section_list[num], True, stylesheet.colour.interface),(((stylesheet.ui_sections.translate_rect_width*num)),(stylesheet.ui_sections.translate_screen_percent*stylesheet.interface.screen_height)+3))

    #def ui_sections(e,): #Make the above stuff modular
    #    for num in range(0, len(sectionListType)):
    #        e.rect = pgm.draw.rect(e.screen, stylesheet.colour.interface, (stylesheet.ui_sections.toolbar_rect_width*num, 0, stylesheet.ui_sections.toolbar_rect_width, 20), 1, 0, -1, -1, -1, -1)
    #        e.screen.blit(stylesheet.font.text_interface.render(stylesheet.ui_sections.toolbar_section_list[num], True, stylesheet.colour.interface),((stylesheet.ui_sections.toolbar_rect_width*num)+80,3))
    
    def textbox(e):
        print

    def screenshot(e): # Works but doesn't work, need to make it take a screenshot from the rectangle that text is blit onto 
        e.image = e.screen.subsurface(e.image_rect)
        pgm.image.save(e.image,"screenshot.png")
        translation = tesseract.tess.text
        print(translation)

    #Loop function
    def scourge(e):
        e.icon = pgm.image.load("icon.png").convert()
        pgm.display.set_caption("Typetone")
        pgm.display.set_icon(e.icon)

        e.clock.tick(e.fps)
        
        
        e.ui_sections()

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