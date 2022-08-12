from PIL import Image
import pytesseract as tesse

class tess:
    text = tesse.image_to_string(Image.open("download.jpg"))