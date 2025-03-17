# Utils.py
# 12 março de 2025
# Contains functions --.--

import pickle
import re
from collections import Counter 


# type data (int, a[tuples])
# type name (str.pkl)
def pretty_print(data: tuple, name: str = None):
    p = []
    total = data[0]
    print("Word count: " + str(total))

    for key in data[1].keys():
        p.append(f"{data[1].get(key):.2f} {key}")
        
    p = ("\n".join(p))
   
    if name:
        write_pkl(name, data[1])
    else:
        print(p)

# r'\w+(?:-\w+)*|[^\w\s]+'
def lexer(regex: str, text: str):
    #FIX ME patterns stopwprds lems
    return re.findall(regex,text)

def counter_transformation(data: list):
    output = {}
    regex = r'(\d+)[ \t]+(\w+(?:-\w+)*|[^\w\s]+)'

    for line in data: 
        match = lexer(regex,line)[0]
        output[match[1]] = float(match[0])

    return Counter(output)

def read_txt(name: str):
    try:
        with open(name, 'r') as f:
            content = f.readlines()
        return content
    
    except Exception as e:
        print(f"Error on open the file: {e}")
        return None
        
def read_pkl(name: str):
    try:
        with open(name, 'rb') as f:
            content = pickle.load(f)
        return content
    
    except Exception as e:
        print(f"Error on opening the file: {e}")
        return None

def write_pkl(name: str, data: str):
    try:
        with open(name, 'wb') as f:
           pickle.dump(data,f)

    except Exception as e:
        print(f"Error on writing the file: {e}")
        return None