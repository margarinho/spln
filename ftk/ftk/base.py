import re
import jjcli
from collections import Counter
def lexer(text):
    #FIX ME patterns stopwprds lems
    return re.findall(r'\w+(?:-\w+)* | [^\w\s]+',text)

def pretty_print(a, r, opt):
    
    total = sum(a.values())

    if "-a" in opt:
        for word, value in a.mostcommon():
            print(f"{word}  {value}")
    else:
        print("Total    " + total)
        for word, value in r:
            print(f"{word}  {value:.2f}")
        
def counter(tokens):
    counter = Counter(tokens)
    total_count = sum(counter.values())
    relative = [(word, count / total_count * 1000000) for word, count in counter.mostcommon()]
    return counter, relative
    

def main():
    #Completar o menu de opções
    """Options:
        -a: absolute frequency 
        -m 700: top 700 words (FIX ME)
        -j: json (FIX ME)
    """
    
    cli = jjcli.clfilter("am:", doc=main._doc_)
    tokens = []
    
    for txt in cli.text():
        l = lexer(txt)
        print(l)
        tokens.append(l)
        
    absolute, relative = counter(tokens)

    pretty_print(absolute,relative, cli.opt)


        