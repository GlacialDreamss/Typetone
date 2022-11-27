import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import QtGui

from stylesheet import ui_sections

class Window(QWidget):
    def __init__(e):
        super().__init__()
        e.setWindowTitle("Typetone")
        e.screen_width, e.screen_height = 400, 400
        e.setGeometry(10, 150, e.screen_width, e.screen_height)
        e.setWindowIcon(QtGui.QIcon("icon.png"))

        layout = QGridLayout()
        e.setLayout(layout)

        toolbar = QMenuBar()
        layout.addWidget(toolbar)

        for num  in range(0, ui_sections.toolbar_section_num):
            action = toolbar.addMenu(ui_sections.toolbar_section_list[num])
            for num2 in range(0, len(ui_sections.toolbar_dropdown_list[num])):
                toolbar.addAction(ui_sections.toolbar_dropdown_list[num][num2])

        tbox = QPlainTextEdit()
        layout.addWidget(tbox, 1, 0)

