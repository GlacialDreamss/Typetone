import pretty_errors
from PyQt6.QtWidgets import QWidget
from textbox import *
from toolbar import *

class Window(QWidget):
    def __init__(e):
        super().__init__()
        e.setWindowTitle("Typetone")
        e.screen_width, e.screen_height = 400, 400
        e.setGeometry(10, 150, e.screen_width, e.screen_height)
        #e.setWindowIcon("icon.png")

        e.create_textbox
        e.create_toolbar
        
