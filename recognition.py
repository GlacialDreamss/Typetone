from PIL import Image
import pytesseract as pyt

class tess:
    drawing_text = pyt.image_to_string(Image.open("screenshot.png"))
    #import_text = pyt.image_to_string(Image.open("___"))