languages = open("fluff/languages.txt","r",encoding="utf8")
codes = open("fluff/language_codes.txt","r",encoding="utf8")
save = open("fluff/result.txt","w",encoding="utf8")
save2 = open("fluff/lang.txt","w",encoding="utf8")
save3 = open("fluff/code.txt","w",encoding="utf8") 
for num in range(0, 117):
    code_current = codes.readline()
    lang_current = languages.readline()
    save.write("['"+lang_current[0:-1]+"','"+code_current[:2]+"'],")
    save2.write("'"+lang_current[0:-1]+"',")
    save3.write("'"+code_current[:2]+"',")