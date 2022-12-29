# importing libraries
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

# window class
class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Painting Window")

		# setting geometry to main window
		self.setGeometry(100, 100, 800, 600)
		

		# creating image object
		self.image = QImage(self.size(), QImage.Format.Format_RGB32)

		# making image color to white
		self.image.fill(qRgb(255,255,255))

		# variables
		# drawing flag
		self.drawing = False
		# default brush size
		self.brushSize = 2
		# default color
		self.brushColor = qRgb(0,0,0)

		# QPoint object to tract the point
		self.lastPoint = QPoint()

		
		# creating menu bar
		mainMenu = self.menuBar()

		# creating file menu for save and clear action
		fileMenu = mainMenu.addMenu("File")

		# adding brush size to main menu
		b_size = mainMenu.addMenu("Brush Size")

		# adding brush color to ain menu
		colour_methods = mainMenu.addMenu("Colour")

		# creating save action
		saveAction = QAction("Save", self)
		# adding short cut for save action
		saveAction.setShortcut("Ctrl + S")
		# adding save to the file menu
		fileMenu.addAction(saveAction)
		# adding action to the save
		saveAction.triggered.connect(self.save)

		# creating clear action
		clearAction = QAction("Clear", self)
		# adding short cut to the clear action
		clearAction.setShortcut("Ctrl + C")
		# adding clear to the file menu
		fileMenu.addAction(clearAction)
		# adding action to the clear
		clearAction.triggered.connect(self.clear)

		# creating options for brush sizes
		# creating action for selecting pixel of 4px
		pix_4 = QAction("4px", self)
		# adding this action to the brush size
		b_size.addAction(pix_4)
		# adding method to this
		pix_4.triggered.connect(self.Pixel_4)

		# similarly repeating above steps for different sizes
		pix_7 = QAction("7px", self)
		b_size.addAction(pix_7)
		pix_7.triggered.connect(self.Pixel_7)

		pix_9 = QAction("9px", self)
		b_size.addAction(pix_9)
		pix_9.triggered.connect(self.Pixel_9)

		pix_12 = QAction("12px", self)
		b_size.addAction(pix_12)
		pix_12.triggered.connect(self.Pixel_12)
		
		# creating options for brush color
		# creating action for black color
		brush = QAction("Brush", self)
		# adding this action to the brush colors
		colour_methods.addAction(brush)
		# adding methods to the black
		brush.triggered.connect(self.blackColor)

		# similarly repeating above steps for different color
		background = QAction("Background", self)
		colour_methods.addAction(background)
		background.triggered.connect(self.backgroundChange)

	# method for checking mouse cicks
	def mousePressEvent(self, event):

		# if left mouse button is pressed
		if event.button() == Qt.MouseButton.LeftButton:
			# make drawing flag true
			self.drawing = True
			# make last point to the point of cursor
			self.lastPoint = event.pos()

	# method for tracking mouse activity
	def mouseMoveEvent(self, event):
		
		# checking if left button is pressed and drawing flag is true
		if (event.buttons() == Qt.MouseButton.LeftButton) & self.drawing:
			
			# creating painter object
			painter = QPainter(self.image)
			
			# set the pen of the painter
			painter.setPen(QPen(self.brushColor, self.brushSize,
							Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
			
			# draw line from the last point of cursor to the current point
			# this will draw only one step
			painter.drawLine(self.lastPoint, event.pos())
			
			# change the last point
			self.lastPoint = event.pos()
			# update
			self.update()

	# method for mouse left button release
	def mouseReleaseEvent(self, event):

		if event.button() == Qt.MouseButton.LeftButton:
			# make drawing flag false
			self.drawing = False

	# paint event
	def paintEvent(self, event):
		# create a canvas
		canvasPainter = QPainter(self)
		
		# draw rectangle on the canvas
		canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

	# method for saving canvas
	def save(self):
		filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
						"PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

		if filePath == "":
			return
		self.image.save(filePath)

	# method for clearing every thing on canvas
	def clear(self):
		# make the whole canvas white
		self.image.fill(qRgb(255,255,255))
		# update
		self.update()

	# methods for changing pixel sizes
	def Pixel_4(self):
		self.brushSize = 4

	def Pixel_7(self):
		self.brushSize = 7

	def Pixel_9(self):
		self.brushSize = 9

	def Pixel_12(self):
		self.brushSize = 12

	# methods for changing brush color
	def blackColor(self):
		self.brushColor =  QColorDialog.getColor()

	def backgroundChange(self):
		self.image.fill(QColorDialog.getColor())



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# showing the window
window.show()

# start the app
sys.exit(App.exec())
