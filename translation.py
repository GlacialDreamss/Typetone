from recognition import tess
from stylesheet import language
from translate import Translator

class translation:
    lang_in = language.input
    lang_out = language.output

    translator = Translator(to_lang=lang_out)
    input =  translator.translate(tess.text)
print(translation.translator.translate(translation.input))