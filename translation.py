from recognition import tess
from translate import Translator
from stylesheet import language


class translation:
    lang_in = language.input
    lang_out = language.output

    translator = Translator(to_lang=lang_out)
    input =  translator.translate(tess.text)
print(translation.translator.translate(translation.input))