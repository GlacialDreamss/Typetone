import pygame

#Window Variables
background_Colour = (32,64,128)
(width, height) = (300, 200)

#Window properties being assigned
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Deez")
screen.fill(background_Colour)

#Window running, main loop
pygame.display.flip() #Flip displays the display
running = True #Flag for whether or not the program should close
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


  
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            screen.fill((255,255,255))
            pygame.display.flip()