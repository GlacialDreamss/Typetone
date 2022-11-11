from PIL import Image
import pytesseract as pyt

class tess:
    text = pyt.image_to_string(Image.open("screenshot.png"))
print(tess.text)