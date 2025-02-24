import re
import jjcli
from collections import Counter
def lexer(text):
    #FIX ME patterns stopwprds lems
    return re.findall(r'\w+(?:-\w+)* | [^\w\s]+',text)

def counter(tokens):
    return Counter(*tokens)

def main():
    cli = jjcli.clfiter()
    tokens = []
    for txt in cli.text():
        l = lexer(txt)
        print(l)
        tokens.append(l)
    c = counter(tokens)
    print(c)
        