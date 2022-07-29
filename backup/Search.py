import re
import json



def Search(searchquery):
    if(not searchquery):
        return []

    numlist,namelist,codelist = Dissect(searchquery)

    nimregex = ""
    for num in numlist:     
        if isAngkatan(num):
            nimregex += "(?=.*\d{3}"+str(num)+"\d{3})"
        else:    
            nimregex += "(?=.*"+num+")"

    print(codelist)
    for code in codelist:
        print ("ASDF")
        nimregex += "(?=.*"+code[1]+")"
    
    print(nimregex)

    datalist = SearchNIMRegex(nimregex)
    datalist = SearchNameRegex(namelist,datalist)

    return datalist

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
 
def SearchNIMRegex(nimregex):
    if not nimregex:
        return DATA_JSON_FILE_DATA

    result = []
    for lines in DATA_JSON_FILE_DATA:
        # print(lines)
        if(len(lines) == 3):
            if re.findall(nimregex,lines[1]) or re.findall(nimregex,lines[2]):
                result.append(lines)
        else:
            if re.findall(nimregex,lines[1]):
                result.append(lines)
    return result

def SearchNameRegex(namelist, datalist):
    if not namelist:
        return datalist

    length = len(namelist)
    result = [[] for i in range(length)]
    
    for lines in datalist:
        counter = 0
        for name in namelist:
            if re.findall(name,lines[0],re.IGNORECASE):
                counter+=1    
        if counter > 0:
            result[length - counter].append(lines)

    print(result)
    return result   

def SearchJson(word):
    regexword = re.compile(r'\b'+re.escape(word)+r'\b', re.IGNORECASE)
    
    listofkeys = []
    for data in ALLDATA:
        for lines in data:
            kode = re.findall(regexword,lines)
            if(kode):
                nimkode = data[lines]
                listofkeys.append([lines,nimkode])
    return listofkeys

def isAngkatan(num):
    return len(num) == 2 and int(num) > 1 and int(num) < 25
   
def main():
    loadJson() 
    print(dissect("muhammad tito")) 
    Search("vi vio ho")
    
if __name__ == '__main__':
    main()
