import re

def dissect(searchquery):
    regexnum = r"\d+"
    regextext = r"[A-z]+"

    num = re.findall(regexnum,searchquery)

    text = re.findall(regextext,searchquery)
    codetext = []
    # nametext = []
    
    for word in text:
        if isKode(word):
            codetext.append(word)
        # else:
        #     nametext.append(word)
            
    return num,text,codetext
    
def isKode(word):
    return True

def main():
    print(dissect("12/3 +adf-= +=123"))

if __name__ == '__main__':
    main()
    