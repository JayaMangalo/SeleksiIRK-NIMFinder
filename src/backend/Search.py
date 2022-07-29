from copy import deepcopy
import re
from backend import JSONLoader as jsloader
SEARCH_LIMIT = 200

def Search(searchquery):
    if(not jsloader.loaded):
        jsloader.loadJson()
    if(not searchquery):
        return []

    numlist,namelist,codelist = Dissect(searchquery)

    highprionimregex = ""
    for num in numlist:     
        if isAngkatan(num):
            highprionimregex += "(?=.*\d{3}"+str(num)+"\d{3})"
        else:    
            highprionimregex += "(?=.*"+num+")"

    lowprionimregex = []
    for code in codelist:
        lowprionimregex.append("(?=.*"+code[1]+"\d{5})")

    # print("HIGH: ",highprionimregex)
    # print("LOW: ",lowprionimregex)
    # print("BAME:" ,namelist)

    datalist = SearchNIMRegex(highprionimregex,lowprionimregex)
    datalist = SearchNameRegex(namelist,datalist)

    flat_list = []
    for i in datalist:
        if not i:
            continue
        if isinstance(i[0], str):
            flat_list.append(i)
        else:
            for j in i:
                flat_list.append(j)

    return appendDatalist(flat_list[:SEARCH_LIMIT])

def Dissect(searchquery):
    regexnum = re.compile(r"\d+", re.IGNORECASE)
    regextext = re.compile(r"[A-z]+", re.IGNORECASE) 

    numlist = re.findall(regexnum,searchquery)

    text = re.findall(regextext,searchquery)
    namelist = []
    codelist = []

    for word in text:
        code = SearchJson(word)
        if code:
            for cod in code:
                codelist.append(cod)
        else:
            namelist.append(word)
            
    return numlist,namelist,codelist
 
def SearchNIMRegex(highprionimregex,lowprionimregex):
    if not highprionimregex and not lowprionimregex:
        return deepcopy(jsloader.DATA_JSON_FILE_DATA)

    result = []
    for lines in deepcopy(jsloader.DATA_JSON_FILE_DATA):
        if(len(lines) == 3):
            if lowprionimregex:
                for regex in lowprionimregex:
                    if re.findall(highprionimregex+regex,lines[2]):
                        result.append(lines)
                        break
            else:
                if re.findall(highprionimregex,lines[2]):
                    result.append(lines)
        else:
            if lowprionimregex:
                for regex in lowprionimregex:
                    if re.findall(highprionimregex+regex,lines[1]):
                        result.append(lines)
                        break
            else:
                if re.findall(highprionimregex,lines[1]):
                    result.append(lines)
    return result

def SearchNameRegex(namelist, datalist):
    if not namelist:
        return datalist

    length = len(namelist)
    result = [[] for i in range(length)]
    
    for lines in datalist:
        match_counter = 0
        for name in namelist:
            if re.findall(name,lines[0],re.IGNORECASE):
                match_counter+=1   
        
        if match_counter > 0:
            result[length - match_counter].append(lines)
    return result   

def SearchJson(word):
    regexword = re.compile(r'\b'+re.escape(word)+r'\b', re.IGNORECASE)
    
    listofkeys = []
    for data in jsloader.ALLDATA:
        for lines in data:
            kode = re.findall(regexword,lines)
            if(kode):
                nimkode = data[lines]
                listofkeys.append([lines,nimkode])
    return listofkeys

def isAngkatan(num):
    return len(num) == 2 and int(num) > 1 and int(num) < 25

def getAngkatan(arr):
    if(len(arr)== 1):
        arr = arr[0]
    if(len(arr) == 3):
        kodejurusan = str(arr[2][:3])
        for line in jsloader.INVERSED_LIST_JURUSAN:
            if line == kodejurusan:
                return jsloader.INVERSED_LIST_JURUSAN.get(line)
    else:
        kodefakultas = str(arr[1][:3])
        for line in jsloader.INVERSED_LIST_FAKULTAS:
            if line == kodefakultas:
                return jsloader.INVERSED_LIST_FAKULTAS.get(line)

def appendDatalist(datalist):
    for lines in datalist:
        lines.append(getAngkatan(lines))
        if len(lines) == 3:
            lines.insert(2,"-")
    
    return datalist
def main():
    datalist = Search("vi vio ho")
    print(len(datalist))
    print(datalist)


    
if __name__ == '__main__':
    main()
