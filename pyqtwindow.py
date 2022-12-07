from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import sys

from stylesheet import *


def paint(e):
        painter = QPainter(e)
        pic = QPixmap("icon.png")
        painter.drawPixmap(e.rect(), pic)
        colour = QColor
        colour.setRed() #Where I stopped, assigning values for all 3 in rgb
        painter.setPen(colour)
        painter.drawRect(40, 40, 400, 200)

class Window(QWidget):
    def __init__(e):
        QWidget.__init__(e)
        layout = QGridLayout()
        e.setLayout(layout)
        e.setWindowTitle("Typetone")
        screen_width, screen_height = 400, 400
        e.setGeometry(10, 150, screen_width, screen_height)
        e.setWindowIcon(QIcon("icon.png"))

        # create menu
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        for num in range(0, len(ui_sections.toolbar_section_list)):
            toolbar_section = menubar.addMenu(ui_sections.toolbar_section_list[num])
            
            for num2 in range(0, len(ui_sections.toolbar_dropdown_list[num])): 
                toolbar_section.addAction(ui_sections.toolbar_dropdown_list[num][num2])
            
            toolbar_section.addSeparator

        # add textbox
        # tbox = QPlainTextEdit()
        # layout.addWidget(tbox, 1, 0)
        # layout.addWidget(tbox, 1, 1)
        paint(e)


        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec())