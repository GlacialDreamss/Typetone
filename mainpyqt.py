from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *

import sys
import os

from translate import Translator
from gtts import gTTS
from PIL import Image
import pretty_errors
import pytesseract
import playsound

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

        # Widget Definition ----------------------------------------------------------------------------------- #
        e.menubar = QMenuBar()
        
        e.title_label_input = QLabel()
        e.title_label_output = QLabel()
        e.title_label_input_dropdown = QLabel()
        e.title_label_output_dropdown = QLabel()
        e.title_label_buttons = QLabel()

        e.title_label_format = QLabel()
        e.title_label_drawing = QLabel()
        e.title_label_import = QLabel()
        e.title_label_text = QLabel()

        e.input_textbox_text = QLineEdit()
        e.input_label_import = QLabel()
        e.input_label_drawing = QLabel()

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

        e.drawing_pixmap = QPixmap("transparent.png")
        e.drawing_label = QLabel()

        # Drawing Attributes ----------------------------------------------------------------------------------- #
        # creating image object
        
        e.image = QImage(e.drawing_pixmap.size(), QImage.Format.Format_RGB32)
        e.drawing_label.setPixmap(e.drawing_pixmap)
        

        # drawing flag
        e.drawing = False
        # default brush size
        e.brushSize = 2
        # default color
        e.brushColor = qRgb(0,0,0)
        # Default background
        e.backgroundColour = qRgb(255, 255, 255)
        e.image.fill(e.backgroundColour)

        # QPoint object to tract the point
        e.lastPoint = QPoint()
        
        # Brush size slider
        e.slider = QSlider(Qt.Orientation.Horizontal, e)
        e.slider.setGeometry(50,50, 200, 50)
        e.slider.setMinimum(0)
        e.slider.setMaximum(30)
        e.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        e.slider.setTickInterval(2)
        
        # Language lists
        e.lang_list_tess = ['afr', 'amh', 'ara', 'asm', 'aze', 'aze_cyrl', 'bel', 'ben', 'bod', 'bos', 'bre', 'bul', 'cat', 'ceb', 'ces', 'chi_sim', 'chi_sim_vert', 'chi_tra', 'chi_tra_vert', 'chr', 'cos', 'cym', 'dan', 'deu', 'div', 'dzo', 'ell', 'eng', 'enm', 'epo', 'equ', 'est', 'eus', 'fao', 'fas', 'fil', 'fin', 'fra', 'frk', 'frm', 'fry', 'gla', 'gle', 'glg', 'grc', 'guj', 'hat', 'heb', 'hin', 'hrv', 'hun', 'hye', 'iku', 'ind', 'isl', 'ita', 'ita_old', 'jav', 'jpn', 'jpn_vert', 'kan', 'kat', 'kat_old', 'kaz', 'khm', 'kir', 'kmr', 'kor', 'lao', 'lat', 'lav', 'lit', 'ltz', 'mal', 'mar', 'mkd', 'mlt', 'mon', 'mri', 'msa', 'mya', 'nep', 'nld', 'nor', 'oci', 'ori', 'osd', 'pan', 'pol', 'por', 'pus', 'que', 'ron', 'rus', 'san', 'sin', 'slk', 'slv', 'snd', 'spa', 'spa_old', 'sqi', 'srp', 'srp_latn', 'sun', 'swa', 'swe', 'syr', 'tam', 'tat', 'tel', 'tgk', 'tha', 'tir', 'ton', 'tur', 'uig', 'ukr', 'urd', 'uzb', 'uzb_cyrl', 'vie', 'yid', 'yor']
        e.lang_list_full = ['Afrikaans','Akan','Amharic','Arabic','Assamese','Azerbaijani','Bashkir','Belarusian','Bulgarian','Bengali','Tibetan','Breton','Bosnian','Catalan','Chamorro','Corsican','Cree','Czech','Old Church Slavonic','Chuvash','Welsh','Danish','German','Divehi','Dzongkha','Ewe','Greek','English','Esperanto','Spanish','Estonian','Basque','Persian','Fula','Finnish','Fijian','Faroese','French','Western Frisian','Irish','Scottish Gaelic','Galician','Gujarati','Manx','Hausa','Hebrew','Hindi','Hiri Motu','Croatian','Haitian','Hungarian','Armenian','Herero','Interlingua','Indonesian','Interlingue','Igbo','Nuosu','Inupiaq','Ido','Icelandic','Italian','Inuktitut','Japanese','Javanese','Georgian','Kongo','Kikuyu','Kwanyama','Kazakh','Kalaallisut','Khmer','Kannada','Korean','Kanuri','Kashmiri','Kurdish','Komi','Cornish','Kyrgyz','Latin','Luxembourgish','Ganda','Limburgish','Lingala','Lao','Lithuanian','Luba-Katanga','Latvian','Malagasy','Marshallese','Māori','Macedonian','Malayalam','Mongolian','Marathi','Malay','Maltese','Burmese','Nauru','Norwegian Bokmål','Northern Ndebele','Nepali','Ndonga','Dutch','Norwegian Nynorsk','Norwegian','Southern Ndebele','Navajo','Chichewa','Occitan','Ojibwe','Oromo','Oriya','Ossetian','Panjabi','Pāli','Polish','Pashto','Portuguese','Quechua','Romansh','Kirundi','Romanian','Russian','Kinyarwanda','Sanskrit','Sardinian','Sindhi','Northern Sami','Sango','Sinhala','Slovak','Slovenian','Shona','Somali','Albanian','Serbian','Southern Sotho','Sundanese','Swedish','Swahili','Tamil','Telugu','Tajik','Thai','Tigrinya','Turkmen','Tagalog','Tswana','Tonga','Turkish','Tsonga','Tatar','Twi','Tahitian','Uyghur','Ukrainian','Urdu','Uzbek','Venda','Vietnamese','Volapük','Walloon','Wolof','Xhosa','Yiddish','Yoruba','Zhuang','Chinese','Zul']
        e.lang_list_code = ['af','ak','am','ar','as','az','ba','be','bg','bn','bo','br','bs','ca','ch','co','cr','cs','cu','cv','cy','da','de','dv','dz','ee','el','en','eo','es','et','eu','fa','ff','fi','fj','fo','fr','fy','ga','gd','gl','gu','gv','ha','he','hi','ho','hr','ht','hu','hy','hz','ia','id','ie','ig','ii','ik','io','is','it','iu','ja','jv','ka','kg','ki','kj','kk','kl','km','kn','ko','kr','ks','ku','kv','kw','ky','la','lb','lg','li','ln','lo','lt','lu','lv','mg','mh','mi','mk','ml','mn','mr','ms','mt','my','na','nb','nd','ne','ng','nl','nn','no','nr','nv','ny','oc','oj','om','or','os','pa','pi','pl','ps','pt','qu','rm','rn','ro','ru','rw','sa','sc','sd','se','sg','si','sk','sl','sn','so','sq','sr','st','su','sv','sw','ta','te','tg','th','ti','tk','tl','tn','to','tr','ts','tt','tw','ty','ug','uk','ur','uz','ve','vi','vo','wa','wo','xh','yi','yo','za','zh','zu']

        # Widgets added to screen ----------------------------------------------------------------------------------- #
        e.layout.addWidget(e.menubar, 0, 0)

        e.layout.addWidget(e.title_label_format, 1, 0)
        e.layout.addWidget(e.title_label_input_dropdown, 1, 1)
        e.layout.addWidget(e.title_label_input, 1, 2)
        e.layout.addWidget(e.title_label_output, 1, 3)
        e.layout.addWidget(e.title_label_output_dropdown, 1, 4)
        e.layout.addWidget(e.title_label_buttons, 1, 5)

        e.layout.addWidget(e.title_label_text, 2, 0)
        e.layout.addWidget(e.title_label_drawing, 3, 0)
        e.layout.addWidget(e.title_label_import, 4, 0)
        
        e.layout.addWidget(e.input_textbox_text, 2, 2)
        e.layout.addWidget(e.input_label_drawing, 3, 2)
        e.layout.addWidget(e.input_label_import, 4, 2)

        e.layout.addWidget(e.output_label_text, 2, 3)
        e.layout.addWidget(e.output_label_drawing, 3, 3)
        e.layout.addWidget(e.output_label_import, 4, 3)

        e.layout.addWidget(e.output_button_text_tts, 2, 5)
        e.layout.addWidget(e.output_button_drawing_tts, 3, 5)
        e.layout.addWidget(e.output_button_import_tts, 4, 5)

        e.layout.addWidget(e.input_dropdown_text, 2, 1)
        e.layout.addWidget(e.input_dropdown_drawing, 3, 1)
        e.layout.addWidget(e.input_dropdown_import, 4, 1)
        e.layout.addWidget(e.output_dropdown_text, 2, 4)
        e.layout.addWidget(e.output_dropdown_drawing, 3, 4)
        e.layout.addWidget(e.output_dropdown_import, 4, 4)

        e.layout.addWidget(e.drawing_label, 5, 3)
        e.layout.addWidget(e.slider, 6, 3)
        
        # Widget Characterisation ----------------------------------------------------------------------------------- #
        e.action_file_import = QAction("Import File", e)
        e.action_file_export = QAction("Export Drawing", e)
        e.action_file_screenshot = QAction("Translate Drawing", e)

        e.action_view_fullscreen = QAction("Fullscreen", e)
        e.action_view_windowed = QAction("Windowed", e)

        e.action_interface_font = QAction("Text Font", e)
        e.action_interface_colour = QAction("Interface Colour", e)

        e.action_drawing_colour_brush = QAction("Brush Colour", e)
        e.action_drawing_colour_background = QAction("Background Colour", e)
        e.action_drawing_clear = QAction("Clear Interface", e)
        
        # Create menus for the menubar
        e.menu_file = e.menubar.addMenu("File")
        e.menu_interface = e.menubar.addMenu("Interface")
        e.menu_drawing = e.menubar.addMenu("Drawing")

        # Add actions to the menus in the menubar
        e.menu_file.addAction(e.action_file_import)
        e.menu_file.addAction(e.action_file_export)
        e.menu_file.addAction(e.action_file_screenshot)

        e.menu_interface.addAction(e.action_interface_font)
        # e.menu_interface.addAction(e.action_interface_colour)

        e.menu_drawing.addAction(e.action_drawing_colour_brush)
        e.menu_drawing.addAction(e.action_drawing_colour_background)
        e.menu_drawing.addAction(e.action_drawing_clear)

        # Add text to title labels
        e.title_label_format.setText("Input Format")
        e.title_label_input.setText("Input")
        e.title_label_output.setText("Output")
        e.title_label_input_dropdown.setText("Input Language")
        e.title_label_output_dropdown.setText("Output Language")
        e.title_label_buttons.setText("Text to speech")
        e.title_label_text.setText("Text:")
        e.title_label_drawing.setText("Drawing:")
        e.title_label_import.setText("Import:")
        
        # New dropdown to determine the language detected by pytesseract
        e.input_dropdown_text.addItems(e.lang_list_full)
        e.input_dropdown_drawing.addItems(e.lang_list_full)
        e.input_dropdown_import.addItems(e.lang_list_full)
        e.output_dropdown_text.addItems(e.lang_list_full)
        e.output_dropdown_drawing.addItems(e.lang_list_full)
        e.output_dropdown_import.addItems(e.lang_list_full)

        # Keyboard Shortcuts 
        e.action_file_import.setShortcut("Ctrl + F")
        e.action_file_export.setShortcut("Ctrl + S")        
        
        # Calling custom methods ----------------------------------------------------------------------------------- #
        
        # Adding Menubar Methods
        e.action_file_import.triggered.connect(e.translateUserImport)
        e.action_file_export.triggered.connect(e.saveFile)
        e.action_file_screenshot.triggered.connect(e.translateUserDrawing)
        e.action_interface_font.triggered.connect(e.fontChange)
        e.action_interface_colour.triggered.connect(e.interfaceColourChange)
        e.action_drawing_colour_brush.triggered.connect(e.brushColourChange)
        e.action_drawing_colour_background.triggered.connect(e.backgroundColourChange)
        e.action_drawing_clear.triggered.connect(e.backgroundClear)

        # Widget Methods
        e.input_textbox_text.editingFinished.connect(e.translateUserText)
        
        e.output_button_text_tts.pressed.connect(e.textToSpeech_text)
        e.output_button_import_tts.pressed.connect(e.textToSpeech_import)
        e.output_button_drawing_tts.pressed.connect(e.textToSpeech_drawing)
        e.slider.valueChanged.connect(e.brushSizeChange)
    
    # Defining Menubar Methods ----------------------------------------------------------------------------------- #
    def saveFile(e):
        filePath, _ = QFileDialog.getSaveFileName(e, "Save Image", "",
                        "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
    
        e.image.save(filePath)

    def brushColourChange(e):
        e.brushColor =  QColorDialog.getColor()

    def brushSizeChange(e):
        e.brushSize = e.slider.value()

    def backgroundColourChange(e):
        e.backgroundColour = QColorDialog.getColor()
        e.image.fill(e.backgroundColour)
    
    def interfaceColourChange(e):
        e.image_interface = QImage(e.size(), QImage.Format.Format_RGB32)
        e.interfaceColour = QColorDialog.getColor()
        e.image_interface.fill(e.interfaceColour)
    
    # method for clearing every thing on canvas
    def backgroundClear(e):
        e.image.fill(e.backgroundColour)
        e.update()
    
    def fontChange(e):
        e.interface_font = QFontDialog.getFont()
        e.setFont(e.interface_font[0])
    
    # Defining Widget Methods ----------------------------------------------------------------------------------- #
    def translateUserText(e):
        # Work out which langauges are supported for translation, change the list
        e.text_lang_in = e.lang_list_code[e.input_dropdown_text.currentIndex()]
        e.text_lang_out = e.lang_list_code[e.output_dropdown_text.currentIndex()]
        e.text_translator = Translator(to_lang=e.text_lang_out,from_lang=e.text_lang_in)

        e.output_label_text.setText(e.text_translator.translate(e.input_textbox_text.text())) # Translates text in the textbox and adds it to label
    
    def translateUserImport(e):
        e.import_lang_in = e.input_dropdown_import.currentText()
        e.import_lang_out = e.output_dropdown_import.currentText()
        e.import_translator = Translator(to_lang=e.import_lang_out,from_lang=e.import_lang_in)
        
        e.file_import, _ = QFileDialog.getOpenFileName(e, "Open Image", "",
                        "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if e.file_import == "":
            return
        
        e.image_import = Image.open(e.file_import)
        e.text_import = pytesseract.image_to_string(e.image_import)

        e.input_label_import.setText(e.text_import)
        e.output_label_import.setText(e.import_translator.translate(e.text_import))
        

    def translateUserDrawing(e):
        e.image_drawing = Image.open("screenshot.png")
        e.text_drawing = pytesseract.image_to_string(e.image_drawing)

        e.drawing_lang_in = e.input_dropdown_drawing.currentText()
        e.drawing_lang_out = e.output_dropdown_drawing.currentText()
        e.drawing_translator = Translator(to_lang=e.drawing_lang_out,from_lang=e.drawing_lang_in)
        e.input_label_drawing.setText(e.text_drawing)        
        e.output_label_drawing.setText(e.drawing_translator.translate(e.text_drawing))
    
    def textToSpeech_text(e):
        e.tts_text = gTTS(e.output_label_text.text())
        e.tts_text.save('text_tts.mp3')
        playsound.playsound("text_tts.mp3")
        os.remove("text_tts.mp3")

    def textToSpeech_import(e):
        e.tts_import = gTTS(e.output_label_import.text())
        e.tts_import.save('import_tts.mp3')
        playsound.playsound("import_tts.mp3")
        os.remove("import_tts.mp3")

    def textToSpeech_drawing(e):
        e.tts_drawing = gTTS(e.output_label_drawing.text())
        e.tts_drawing.save('drawing_tts.mp3')
        playsound.playsound("drawing_tts.mp3")
        os.remove("drawing_tts.mp3")

    
    # Defining Drawing Methods ----------------------------------------------------------------------------------- #
    # method for checking mouse cicks
    def mousePressEvent(e, event):

        # if left mouse button is pressed
        if event.buttons() == Qt.MouseButton.LeftButton:
            # make drawing flag true
            e.drawing = True
            # make last point to the point of cursor
            e.lastPoint = event.pos()

    # method for tracking mouse activity
    def mouseMoveEvent(e, event):
        
        # checking if left button is pressed and drawing flag is true
        if (event.buttons() == Qt.MouseButton.LeftButton) & e.drawing:
            
            # creating painter object
            painter = QPainter(e.image)
            
            # set the pen of the painter
            painter.setPen(QPen(e.brushColor, e.brushSize,
                            Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            
            # draw line from the last point of cursor to the current point
            # this will draw only one step
            painter.drawLine(e.lastPoint, event.pos())
            
            # change the last point
            e.lastPoint = event.pos()
            # update
            e.update()

    # method for mouse left button release
    def mouseReleaseEvent(e, event):

        if event.buttons() == Qt.MouseButton.LeftButton:
            # make drawing flag false
            e.drawing = False

    # paint event
    def paintEvent(e, event):
        # create a canvas
        canvasPainter = QPainter(e)
        # draw rectangle on the canvas
        #canvasPainter.drawImage(e.drawing_label.rect(), e.image, e.drawing_pixmap.rect())
        e.point = QPoint()
        e.point.setX(452)
        e.point.setY(150)
        canvasPainter.setBrushOrigin(e.point)
        canvasPainter.drawImage(e.point, e.image)
        e.image.save('screenshot.png')

# Execution
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec())