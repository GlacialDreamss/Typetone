from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import sys

from stylesheet import *

class Window(QWidget):
    def __init__(e):
        QWidget.__init__(e)

        e.layout = QGridLayout()
        e.setLayout(e.layout)
        e.setWindowTitle("Typetone")
        screen_width, screen_height = 400, 400
        e.setGeometry(10, 150, screen_width, screen_height)
        e.setWindowIcon(QIcon("icon.png"))


        # create menu
        menubar = QMenuBar()
        e.layout.addWidget(menubar, 0, 0)
        for num in range(0, len(ui_sections.toolbar_section_list)):
            toolbar_section = menubar.addMenu(ui_sections.toolbar_section_list[num])
            
            for num2 in range(0, len(ui_sections.toolbar_dropdown_list[num])): 
                toolbar_section.addAction(ui_sections.toolbar_dropdown_list[num][num2])
            
            toolbar_section.addSeparator

        # add labels 
        text = QPlainTextEdit()
        text2 = QPlainTextEdit()
        # add textboxes
        for num in range(2,5):
            e.layout.addWidget(text, num, 1)
            if num == 4: break
            e.layout.addWidget(text2, num, 0)
        
        print(text.toPlainText())
        
        # add buttons for text to speech
        label = QLabel()
        label2 = QLabel()
        label.setText("Input")
        label2.setText("Output")        
        e.layout.addWidget(label, 1, 0)
        e.layout.addWidget(label2, 1, 1)        
        
        # Somehow do interface
    
    def paint(e):
        painter = QPainter(e)
        pic = QPixmap("icon.png")
        painter.drawPixmap(e.rect(), pic)
        colour = QColor
        # colour.setRed() #Where I stopped, assigning values for all 3 in rgb
        # painter.setPen(colour)
        # painter.drawRect(40, 40, 400, 200)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec())