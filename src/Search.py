import re
import json
import os
import psutil

process = psutil.Process(os.getpid())
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
print(process.memory_info().rss)  # in bytes 

IGNORED_WORDS = ["TEKNIK","TEKNOLOGI","DAN"]

DATA_JSON_FILE_PATH = "src/json/data_13_21.json"
KODE_FAKULTAS_JSON_FILE_PATH = "src/json/kode_fakultas.json"
KODE_JURUSAN_JSON_FILE_PATH = "src/json/kode_jurusan.json"
LIST_FAKULTAS_JSON_FILE_PATH = "src/json/list_fakultas.json"
LIST_JURUSAN_JSON_FILE_PATH = "src/json/list_jurusan.json"

def dissect(searchquery):
    regexnum = re.compile(r"\d+", re.IGNORECASE)
    regextext = re.compile(r"[A-z]+", re.IGNORECASE) 

    num = re.findall(regexnum,searchquery)

    text = re.findall(regextext,searchquery)
    codelist = []

    for word in text:
        code = searchJson(word)
        if code:
            codelist.append(code)

            
    return num,text,codelist
    

def loadJson():
    global DATA_JSON_FILE_DATA
    global KODE_FAKULTAS_JSON_FILE_DATA 
    global KODE_JURUSAN_JSON_FILE_DATA
    global LIST_FAKULTAS_JSON_FILE_DATA
    global LIST_JURUSAN_JSON_FILE_DATA
    global ALLDATA

    f = open (DATA_JSON_FILE_PATH, "r")
    DATA_JSON_FILE_DATA = json.loads(f.read())
    f.close()
    f = open (KODE_FAKULTAS_JSON_FILE_PATH, "r")
    KODE_FAKULTAS_JSON_FILE_DATA = json.loads(f.read())
    f.close()
    f = open (KODE_JURUSAN_JSON_FILE_PATH, "r")
    KODE_JURUSAN_JSON_FILE_DATA = json.loads(f.read())
    f.close()
    f = open (LIST_FAKULTAS_JSON_FILE_PATH, "r")
    LIST_FAKULTAS_JSON_FILE_DATA = json.loads(f.read())
    f.close()
    f = open (LIST_JURUSAN_JSON_FILE_PATH, "r")
    LIST_JURUSAN_JSON_FILE_DATA = json.loads(f.read())
    f.close()
    ALLDATA = [KODE_FAKULTAS_JSON_FILE_DATA,KODE_JURUSAN_JSON_FILE_DATA,LIST_FAKULTAS_JSON_FILE_DATA,LIST_JURUSAN_JSON_FILE_DATA]

def searchJson(word):
    if word in IGNORED_WORDS:
        return []

    regexword = re.compile(r'\b'+re.escape(word)+r'\b', re.IGNORECASE)
    # print(regexword)

    listofkeys = []
    for i,data in enumerate(ALLDATA):
        for lines in data:
            kode = re.findall(regexword,lines)
            if(kode):
                nimkode = data[lines]
                listofkeys.append([lines,nimkode])
    return listofkeys

def main():
    loadJson()
    listofkeys = (searchJson("fisika"))
    print(listofkeys)
    
    
if __name__ == '__main__':
    main()
    