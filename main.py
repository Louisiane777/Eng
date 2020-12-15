import json
from difflib import get_close_matches
def translate(word):
    word = word.lower()
    word_title = word.title()
    word_upper = word.upper()
    if word in data:
        return data[word]
    elif word_title in data:
        return data[word_title] 
    elif word_upper in data:
        return data[word_upper]       
    elif len(get_close_matches(word,data.keys()))>0:
        closematch = get_close_matches(word,data.keys())[0]
        yn = input("Did you mean " + closematch + " answer y or n ")
        if yn.lower() == "y":
            return  data[closematch]
        elif yn.lower() == "n":
            return "Word not found"
        else:
            return "Wrong input"    
                
    else:
           return "word Not found"


data = json.load(open('data.json','r'))
word = input("Enter a word: ")
#print(data.keys())
res = translate(word)
if isinstance(res,list):
    for i in  range (len(res)):
        print(i+1, "-",res[i])
else:
    print(res)
