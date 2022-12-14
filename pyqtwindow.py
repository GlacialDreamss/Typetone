from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import sys

from stylesheet import *
from translation import *
from recognition import tess
from translate import Translator
import pretty_errors


class Window(QWidget):
    def __init__(e):
        QWidget.__init__(e)

        e.layout = QGridLayout()
        e.setLayout(e.layout)
        e.setWindowTitle("Typetone")
        screen_width, screen_height = 400, 400
        e.setGeometry(10, 150, screen_width, screen_height)
        e.setWindowIcon(QIcon("icon.png"))

        #Program needs to be able to show the screen (bottom of file) and update the file based on the screen (infinite loop). The issue is being able to access attributes as they are currently in the init which I did by trying to put the stuff below in a main method. This results in methods being uncallable in the main method. Do not remove QWidget from the Window() as there is no widget object being used (it would have to be used in the statements but I can't do that because it doesn't apply to the main screen)

        # create menu
        menubar = QMenuBar()
        e.layout.addWidget(menubar, 0, 0)
        for num in range(0, len(ui_sections.toolbar_section_list)):
            toolbar_section = menubar.addMenu(ui_sections.toolbar_section_list[num])
            
            for num2 in range(0, len(ui_sections.toolbar_dropdown_list[num])): 
                toolbar_section.addAction(ui_sections.toolbar_dropdown_list[num][num2])
            
            toolbar_section.addSeparator
    
        # Widget Definition ----------------------------------------------------------------------------------- #
        e.input_image_drawing = QPixmap()  

        e.title_label_input = QLabel()
        e.title_label_output = QLabel()

        e.input_textbox_text = QLineEdit()
        e.output_label_text = QLabel()
        e.output_label_drawing = QLabel()
        e.output_label_import = QLabel()
        
        e.output_button_text_tts = QPushButton()
        e.output_button_drawing_tts = QPushButton()
        e.output_button_import_tts = QPushButton()

        e.input_dropdown_text = QComboBox()
        e.output_dropdown_text = QComboBox()
        e.output_dropdown_drawing = QComboBox()
        e.output_dropdown_import = QComboBox()

        # Widgets added to screen ----------------------------------------------------------------------------------- #
        # e.layout.addWidget()

        e.layout.addWidget(e.title_label_input, 2, 0)
        e.layout.addWidget(e.title_label_output, 2, 1)   
       
        e.layout.addWidget(e.input_textbox_text, 3, 0)
        e.layout.addWidget(e.output_label_text, 3, 1)
        e.layout.addWidget(e.output_label_drawing, 4, 1)
        e.layout.addWidget(e.output_label_import, 5, 1)

        e.layout.addWidget(e.output_button_text_tts, 3, 3)
        e.layout.addWidget(e.output_button_drawing_tts, 4, 3)
        e.layout.addWidget(e.output_button_import_tts, 5, 3)

        e.layout.addWidget(e.input_dropdown_text, 2, 2)
        e.layout.addWidget(e.output_dropdown_text, 3, 2)
        e.layout.addWidget(e.output_dropdown_drawing, 4, 2)
        e.layout.addWidget(e.output_dropdown_import, 5, 2)

        # Widget Characterisation ----------------------------------------------------------------------------------- #
        e.title_label_input.setText("Input")
        e.title_label_output.setText("Output") 

        e.input_textbox_text.editingFinished.connect(e.translateUserText)     
        

        # Translation Vatiables ----------------------------------------------------------------------------------- #
        e.lang_in = language.input
        e.lang_out = language.output

        e.translator = Translator(to_lang=e.lang_out)  
    
    def paint(e):
        e.painter = QPainter(e)
        e.pic = QPixmap("icon.png")
        e.painter.drawPixmap(e.rect(), e.pic)
        e.colour = QColor
        # colour.setRed() #Where I stopped, assigning values for all 3 in rgb
        # painter.setPen(e.colour)
        # painter.drawRect(40, 40, 400, 200)

    def translateUserText(e):
        e.output_label_text.setText(e.translator.translate(e.input_textbox_text.text())) # Translates text in the textbox and adds it to label
    def translateUserImport(e):
        print
    def texttospeech(e):
        print

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec())
