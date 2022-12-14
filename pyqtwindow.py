from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *

import sys
import os

from stylesheet import *
from recognition import tess
from translate import Translator
import pretty_errors
from gtts import gTTS


class Window(QWidget):
    def __init__(e):
        QWidget.__init__(e)
        
        # Window Settings ----------------------------------------------------------------------------------- #
        e.layout = QGridLayout()
        e.setLayout(e.layout)
        e.setWindowTitle("Typetone")
        # screen_width, screen_height = 400, 400
        # e.setGeometry(10, 150, screen_width, screen_height)
        e.setWindowIcon(QIcon("icon.png"))

        # create top menu
        e.menubar = QMenuBar()
        e.layout.addWidget(e.menubar, 0, 0)
        for num in range(0, len(ui_sections.toolbar_section_list)):
            toolbar_section = e.menubar.addMenu(ui_sections.toolbar_section_list[num])
            
            for num2 in range(0, len(ui_sections.toolbar_dropdown_list[num])): 
                toolbar_section.addAction(ui_sections.toolbar_dropdown_list[num][num2])

        # Widget Definition ----------------------------------------------------------------------------------- #
        e.input_image_drawing = QPixmap()  

        e.title_label_input = QLabel()
        e.title_label_output = QLabel()
        e.title_label_input_dropdown = QLabel()
        e.title_label_output_dropdown = QLabel()
        e.title_label_buttons = QLabel()

        e.input_textbox_text = QLineEdit()

        e.input_label_drawing = QLabel()
        e.input_label_import = QLabel()
        e.output_label_text = QLabel()
        e.output_label_drawing = QLabel()
        e.output_label_import = QLabel()
        
        e.output_button_text_tts = QPushButton()
        e.output_button_drawing_tts = QPushButton()
        e.output_button_import_tts = QPushButton()

        e.input_dropdown_text = QComboBox()
        e.input_dropdown_drawing = QComboBox()
        e.input_dropdown_import = QComboBox()
        e.output_dropdown_text = QComboBox()
        e.output_dropdown_drawing = QComboBox()
        e.output_dropdown_import = QComboBox()

        # Widgets added to screen ----------------------------------------------------------------------------------- #
        # e.layout.addWidget()

        e.layout.addWidget(e.title_label_input, 2, 0)
        e.layout.addWidget(e.title_label_output, 2, 4)
        e.layout.addWidget(e.title_label_input_dropdown, 2, 1)
        e.layout.addWidget(e.title_label_output_dropdown, 2, 3)
        e.layout.addWidget(e.title_label_buttons, 2, 5)
       
        e.layout.addWidget(e.input_textbox_text, 3, 1)

        e.layout.addWidget(e.input_label_drawing, 4, 1)
        e.layout.addWidget(e.input_label_import, 5, 1)
        e.layout.addWidget(e.output_label_text, 3, 3)
        e.layout.addWidget(e.output_label_drawing, 4, 3)
        e.layout.addWidget(e.output_label_import, 5, 3)

        e.layout.addWidget(e.output_button_text_tts, 3, 5)
        e.layout.addWidget(e.output_button_drawing_tts, 4, 5)
        e.layout.addWidget(e.output_button_import_tts, 5, 5)

        e.layout.addWidget(e.input_dropdown_text, 3, 0)
        e.layout.addWidget(e.input_dropdown_drawing, 4, 0)
        e.layout.addWidget(e.input_dropdown_import, 5, 0)
        e.layout.addWidget(e.output_dropdown_text, 3, 4)
        e.layout.addWidget(e.output_dropdown_drawing, 4, 4)
        e.layout.addWidget(e.output_dropdown_import, 5, 4)

        # Widget Characterisation ----------------------------------------------------------------------------------- #
        e.title_label_input.setText("Input Langauge")
        e.title_label_output.setText("Output Language")
        e.title_label_input_dropdown.setText("Input")
        e.title_label_output_dropdown.setText("Output")
        e.title_label_buttons.setText("Text to speech")
        e.input_label_drawing.setText("Drawing:")
        e.input_label_import.setText("Import:")

        e.input_dropdown_text.addItems(language.lang_list)
        e.input_dropdown_drawing.addItems(language.lang_list)
        e.input_dropdown_import.addItems(language.lang_list)
        e.output_dropdown_text.addItems(language.lang_list)
        e.output_dropdown_drawing.addItems(language.lang_list)
        e.output_dropdown_import.addItems(language.lang_list)
        
        # Calling custom methods ----------------------------------------------------------------------------------- #
        e.output_dropdown_text.currentIndexChanged.connect(e.getDropdownItem)
        e.input_textbox_text.editingFinished.connect(e.translateUserText)
        #e.menubar.triggered(ui_sections.toolbar_dropdown_list[num][num2]).connect(e.translateUserImport)
        
        e.output_button_text_tts.pressed.connect(e.textToSpeech_text)

        # Translation Vatiables ----------------------------------------------------------------------------------- #
        e.lang_in = language.input
        e.lang_out = language.output

        e.translator = Translator(to_lang=e.lang_out)  
    
    def paint(e):
        e.painter = QPainter(e)
        e.pic = QPixmap("icon.png")
        e.painter.drawPixmap(e.rect(), e.pic)
        e.colour = QColor()
        # colour.setRed() #Where I stopped, assigning values for all 3 in rgb
        # painter.setPen(e.colour)
        # painter.drawRect(40, 40, 400, 200)

    def getDropdownItem(e):
        print(e.output_dropdown_import.currentText())

    def translateUserText(e):
        e.output_label_text.setText(e.translator.translate(e.input_textbox_text.text())) # Translates text in the textbox and adds it to label
    
    def translateUserImport(e):
        QFileDialog.getOpenFileName()
    
    def textToSpeech_text(e):
        e.tts = gTTS(e.translator.translate(e.input_textbox_text.text()))
        e.tts.save('text_tts.mp3')
        e.player = QMediaPlayer()

        e.directory = QUrl.fromLocalFile("text_tts.mp3")
        e.player.setSource(e.directory)
        e.player.play()

# Execution
app = QApplication(sys.argv)
# app.setStyleSheet('''
#     QWidget {
#         font-size: 30px;
#     }
# ''')
screen = Window()
screen.show()
sys.exit(app.exec())