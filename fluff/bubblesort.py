lang = open("fluff/langsorted.txt", "w")
code = open("fluff/codesorted.txt", "w")
lang_list_full = ['Afrikaans','Amharic','Arabic','Assamese','Azerbaijani','Bashkir','Belarusian','Bulgarian','Bengali','Tibetan','Breton','Bosnian','Catalan','Corsican','Czech','Welsh','Danish','German','Divehi','Greek','English','Esperanto','Spanish','Estonian','Basque','Persian','Finnish','Fijian','French','Western Frisian','Irish','Scottish Gaelic','Galician','Gujarati','Hausa','Hebrew','Hindi','Croatian','Haitian','Hungarian','Armenian','Indonesian','Igbo','Icelandic','Italian','Inuktitut','Japanese','Georgian','Kazakh','Khmer','Kannada','Korean','Kurdish','Kyrgyz','Latin','Luxembourgish','Lao','Lithuanian','Latvian','Malagasy','Māori','Macedonian','Malayalam','Mongolian','Marathi','Malay','Maltese','Burmese','Norwegian Bokmål','Nepali','Dutch','Norwegian Nynorsk','Norwegian','Chichewa','Occitan','Oriya','Panjabi','Polish','Pashto','Portuguese','Quechua','Romanian','Russian','Kinyarwanda','Sindhi','Sinhala','Slovak','Slovenian','Shona','Somali','Albanian','Serbian','Southern Sotho','Sundanese','Swedish','Swahili','Tamil','Telugu','Tajik','Thai','Tigrinya','Turkmen','Tagalog','Tonga','Turkish','Tatar','Tahitian','Uyghur','Ukrainian','Urdu','Uzbek','Vietnamese','Xhosa','Yiddish','Yoruba','Chinese','Zul']
lang_list_code = ['af','am','ar','as','az','ba','be','bg','bn','bo','br','bs','ca','co','cs','cy','da','de','dv','el','en','eo','es','et','eu','fa','fi','fj','fr','fy','ga','gd','gl','gu','ha','he','hi','hr','ht','hu','hy','id','ig','is','it','iu','ja','ka','kk','km','kn','ko','ku','ky','la','lb','lo','lt','lv','mg','mi','mk','ml','mn','mr','ms','mt','my','nb','ne','nl','nn','no','ny','oc','or','pa','pl','ps','pt','qu','ro','ru','rw','sd','si','sk','sl','sn','so','sq','sr','st','su','sv','sw','ta','te','tg','th','ti','tk','tl','to','tr','tt','ty','ug','uk','ur','uz','vi','xh','yi','yo','zh','zu']
num = 1
while True:

    lang1_length = len(lang_list_full[num-1])
    lang2_length = len(lang_list_full[num])
    
    if lang1_length > lang2_length:

        for pos in range(0,lang2_length):

            temp = lang_list_full[num]
            temp_code = lang_list_code[num]

            if lang_list_full[num-1][pos:pos+1] < lang_list_full[num][pos:pos+1]:
                print(lang_list_full[num],lang_list_full[num-1])

                lang_list_full[num] = lang_list_full[num-1]
                lang_list_full[num-1] = temp
                
                lang_list_code[num] = lang_list_code[num-1]
                lang_list_code[num-1] = temp_code
    
    if lang1_length < lang2_length:

        for pos in range(0,lang1_length):

            temp = lang_list_full[num]
            temp_code = lang_list_code[num]

            if lang_list_full[num-1][pos:pos+1] < lang_list_full[num][pos:pos+1]:

                lang_list_full[num] = lang_list_full[num-1]
                lang_list_full[num-1] = temp

                lang_list_code[num] = lang_list_code[num-1]
                lang_list_full[num-1] = temp_code
    
    if lang_list_full == lang_list_full.sort():

        for fin in range(0,lang_list_full):

            lang.write(lang_list_full[fin])

        break