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

dict_file= os.path.join( str( os.getcwd()) ,'data.json')
print(dict_file)

"""
with open(dict_file , "r") as fp:
    fl_content=fp.read()
fp.close()    
"""
#C:\Users\sunday\Desktop\work\pb_python\py_vscode\py_github_projects\search_word_in_dict_1\data.json

#print(fl_content)
