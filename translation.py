from recognition import tess
from stylesheet import language
from translate import Translator

class transl:
    lang_in = language.input
    lang_out = language.output

    translator = Translator(to_lang=lang_out)
    translation = translator.translate(tess.text)
print(transl.translation)