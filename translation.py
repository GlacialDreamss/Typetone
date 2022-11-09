from tesset import tess
from translate import Translator

class language:
    lang = "zh"
    translator = Translator(to_lang=lang)
    translation = translator.translate(tess.text)
    print(translation)