import pygame as pg

class Screen: #Calls the refresh method using parameters to determine its size
    width = 1920
    height =1080
    refresh(width, height)

def refresh(width, height):
    fps = 60
    while True:
        for num in range(0,fps):
            Screen.fill((0,0,0))

