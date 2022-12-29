import pygame as pgm

class font:
    pgm.font.init()
    text_interface = pgm.font.Font("comic.ttf", 20)
    text_typing = ()

class colour:
    interface = (100,100,100)
    background = (220, 210, 220)
    toolbar = (0, 0, 0)
    texbox = (0, 0, 0)
    
    ui = (200, 130, 140)
    brush = (200, 165, 175)

    text_interface = (0, 0, 0)
    text_typing = ()

class language:
    lang_list_tess = ['afr', 'amh', 'ara', 'asm', 'aze', 'aze_cyrl', 'bel', 'ben', 'bod', 'bos', 'bre', 'bul', 'cat', 'ceb', 'ces', 'chi_sim', 'chi_sim_vert', 'chi_tra', 'chi_tra_vert', 'chr', 'cos', 'cym', 'dan', 'deu', 'div', 'dzo', 'ell', 'eng', 'enm', 'epo', 'equ', 'est', 'eus', 'fao', 'fas', 'fil', 'fin', 'fra', 'frk', 'frm', 'fry', 'gla', 'gle', 'glg', 'grc', 'guj', 'hat', 'heb', 'hin', 'hrv', 'hun', 'hye', 'iku', 'ind', 'isl', 'ita', 'ita_old', 'jav', 'jpn', 'jpn_vert', 'kan', 'kat', 'kat_old', 'kaz', 'khm', 'kir', 'kmr', 'kor', 'lao', 'lat', 'lav', 'lit', 'ltz', 'mal', 'mar', 'mkd', 'mlt', 'mon', 'mri', 'msa', 'mya', 'nep', 'nld', 'nor', 'oci', 'ori', 'osd', 'pan', 'pol', 'por', 'pus', 'que', 'ron', 'rus', 'san', 'sin', 'slk', 'slv', 'snd', 'spa', 'spa_old', 'sqi', 'srp', 'srp_latn', 'sun', 'swa', 'swe', 'syr', 'tam', 'tat', 'tel', 'tgk', 'tha', 'tir', 'ton', 'tur', 'uig', 'ukr', 'urd', 'uzb', 'uzb_cyrl', 'vie', 'yid', 'yor']
    lang_list_full = ['Afrikaans','Akan','Amharic','Arabic','Assamese','Azerbaijani','Bashkir','Belarusian','Bulgarian','Bengali','Tibetan','Breton','Bosnian','Catalan','Chamorro','Corsican','Cree','Czech','Old Church Slavonic','Chuvash','Welsh','Danish','German','Divehi','Dzongkha','Ewe','Greek','English','Esperanto','Spanish','Estonian','Basque','Persian','Fula','Finnish','Fijian','Faroese','French','Western Frisian','Irish','Scottish Gaelic','Galician','Gujarati','Manx','Hausa','Hebrew','Hindi','Hiri Motu','Croatian','Haitian','Hungarian','Armenian','Herero','Interlingua','Indonesian','Interlingue','Igbo','Nuosu','Inupiaq','Ido','Icelandic','Italian','Inuktitut','Japanese','Javanese','Georgian','Kongo','Kikuyu','Kwanyama','Kazakh','Kalaallisut','Khmer','Kannada','Korean','Kanuri','Kashmiri','Kurdish','Komi','Cornish','Kyrgyz','Latin','Luxembourgish','Ganda','Limburgish','Lingala','Lao','Lithuanian','Luba-Katanga','Latvian','Malagasy','Marshallese','Māori','Macedonian','Malayalam','Mongolian','Marathi','Malay','Maltese','Burmese','Nauru','Norwegian Bokmål','Northern Ndebele','Nepali','Ndonga','Dutch','Norwegian Nynorsk','Norwegian','Southern Ndebele','Navajo','Chichewa','Occitan','Ojibwe','Oromo','Oriya','Ossetian','Panjabi','Pāli','Polish','Pashto','Portuguese','Quechua','Romansh','Kirundi','Romanian','Russian','Kinyarwanda','Sanskrit','Sardinian','Sindhi','Northern Sami','Sango','Sinhala','Slovak','Slovenian','Shona','Somali','Albanian','Serbian','Southern Sotho','Sundanese','Swedish','Swahili','Tamil','Telugu','Tajik','Thai','Tigrinya','Turkmen','Tagalog','Tswana','Tonga','Turkish','Tsonga','Tatar','Twi','Tahitian','Uyghur','Ukrainian','Urdu','Uzbek','Venda','Vietnamese','Volapük','Walloon','Wolof','Xhosa','Yiddish','Yoruba','Zhuang','Chinese','Zul']
    lang_list_code = ['af','ak','am','ar','as','az','ba','be','bg','bn','bo','br','bs','ca','ch','co','cr','cs','cu','cv','cy','da','de','dv','dz','ee','el','en','eo','es','et','eu','fa','ff','fi','fj','fo','fr','fy','ga','gd','gl','gu','gv','ha','he','hi','ho','hr','ht','hu','hy','hz','ia','id','ie','ig','ii','ik','io','is','it','iu','ja','jv','ka','kg','ki','kj','kk','kl','km','kn','ko','kr','ks','ku','kv','kw','ky','la','lb','lg','li','ln','lo','lt','lu','lv','mg','mh','mi','mk','ml','mn','mr','ms','mt','my','na','nb','nd','ne','ng','nl','nn','no','nr','nv','ny','oc','oj','om','or','os','pa','pi','pl','ps','pt','qu','rm','rn','ro','ru','rw','sa','sc','sd','se','sg','si','sk','sl','sn','so','sq','sr','st','su','sv','sw','ta','te','tg','th','ti','tk','tl','tn','to','tr','ts','tt','tw','ty','ug','uk','ur','uz','ve','vi','vo','wa','wo','xh','yi','yo','za','zh','zu']
    # Not necessary in pyqt file
    input = "en"
    output = "chi"

class interface:
    screen_height = 800
    screen_width = 1500
    brush_size = 1

class ui_sections: #How can I do modular stuff, make a loop that goes through each section and uses parameters for a standardised structure
    toolbar_section_list = ["File", "View", "History", "Drawing", "Custom"]
    toolbar_section_num = len(toolbar_section_list) # On a scale of 1 to 10 how much do I need this and the line below?
    toolbar_rect_width = interface.screen_width/toolbar_section_num
    toolbar_screen_percent = 0.022
    toolbar_dropdown_list = [["Import File", "Export Drawing"], ["Fullscreen", "Windowed"], [], ["Brush Colour", "Brush Size", "Background Colour", "Clear Interface"], ["Interface Font", "Text to Speech Voice"]]
    toolbar_dropdown_listnum = [2, 3, 1, 3]

    translate_section_list = ["Input language: "+language.input,"Output language: "+language.output]
    translate_section_num = len(translate_section_list)
    translate_rect_width = interface.screen_width/translate_section_num
    translate_screen_percent = 0.6

    total_section_num = 3
