"""
Welcome to search in dictionary utility

Author: Parashar Bhatt
Created: 2 Nov 2020

"""
#Below code reads file and stores its content in variable "fl_Content"
import os
import json
import difflib
#from difflib import SequenceMatcher
from difflib import get_close_matches

print(os.getcwd())

dict_file= os.path.join( str( os.getcwd()) ,'search_word_in_dict_1\data.json')
#dict_file='search_word_in_dict_1\data.json'
print(dict_file)


with open(dict_file , "r") as fp:
    fl_content=fp.read()
fp.close()    



#print(fl_content)

# Below code loads json content into dictionary object using json.loads built-in method of json package
d=json.loads(fl_content)
print(f"Current different words in dictionary are: {len(d)} \n")

#print(d)    

#l=d["rain"]
#print(l)

    
# Get word from user to search in dictionary

search_word=input("Enter word to search in dictionary: ")

print("\n\nResult: \n")

# Get keys from dictionary
k=d.keys()

# store all keys of dictionary in lower case

n_k=[]
for x in k:
    n_k.append(x.lower())
#print(k)
    


def translate(word):
    word=word.lower()
       
    if word.lower() in d:
        meanings =  d[word.lower()] 
    elif word.title() in d:
        meanings =  d[word.title()] 
    elif word.upper() in d:
        meanings = d[word.upper()]
    else:
        if len( get_close_matches(word, d.keys(),n=3,cutoff=0.8)) > 0:
            yn= input( "did you mean %s instead? Enter 'Y' OR 'N' " % get_close_matches( word, d.keys(),n=3,cutoff=0.8)[0])
            yn=yn.upper()
            if yn == "Y":
                meanings =  get_close_matches( word, d.keys(),n=3,cutoff=0.8)[0]
            elif yn== "N":
                meanings="The word doesn't exist please double check it"
            else:
                meanings="We didn't understand your entry!"
        else:
              meanings=None
     
    return meanings

result=translate(search_word)    
           

if result == None:
    print("Can not display, Word does not exists in our dictionary ! ")
else:
    if type(result)==list:
        for x in result:
            print(x)
    else:
        print (result)
    
