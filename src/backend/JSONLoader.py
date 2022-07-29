import json
import os
loaded = False
RELATIVE_PATH = "../../backend/"
DATA_JSON_FILE_PATH = os.path.join(RELATIVE_PATH+ "json/data_13_21.json")
KODE_FAKULTAS_JSON_FILE_PATH = os.path.join(RELATIVE_PATH+ "json/kode_fakultas.json")
KODE_JURUSAN_JSON_FILE_PATH = os.path.join(RELATIVE_PATH+ "json/kode_jurusan.json")
LIST_FAKULTAS_JSON_FILE_PATH = os.path.join(RELATIVE_PATH+ "json/list_fakultas.json")
LIST_JURUSAN_JSON_FILE_PATH = os.path.join(RELATIVE_PATH+ "json/list_jurusan.json")

def loadJson():
    global loaded
    if loaded:
        return
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
    loaded = True

    global INVERSED_LIST_FAKULTAS
    global INVERSED_LIST_JURUSAN

    INVERSED_LIST_FAKULTAS =  {v: k for k, v in LIST_FAKULTAS_JSON_FILE_DATA.items()}
    INVERSED_LIST_JURUSAN =  {v: k for k, v in LIST_JURUSAN_JSON_FILE_DATA.items()}