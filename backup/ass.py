import re

numlist = ["hi","you"]

regex = ""
regex += "(?=.*\d{3}"+str(19)+"\d{3})"
regex += "(?=.*"+numlist[1]+")"

print(regex)

pattern = '(?=.*\d{3}19\d{3})(?=.*you)'

print (pattern)

string = " 1211923 2you"

if(re.match(pattern,string)):
    print("not empty")

if(re.findall(regex,string)):
    print("not emptyeeee")