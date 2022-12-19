languages = open("language_codes.txt","r")
codes = open("languages.txt","r")
save = open("result.txt","w")
language_code_array = [[]]
for num in range(0, 183):
    code_current = codes.readline()
    lang_current = languages.readline()
    save.write("["+code_current+","+lang_current+"],")


