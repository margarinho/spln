import re
from docopt import docopt
from collections import Counter
def lexer(text):
    #FIX ME patterns stopwprds lems
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+',text)

def pretty_print(a, r, label_a, name):
    outp = []
    total = sum(a.values())

    if label_a:
        for word, value in a.most_common():
           outp.append(f"{value}    {word}")
    else:
        print("Total    " + str(total))
        for word, value in r:
           outp.append(f"{value:.2f}    {word}")

    if name:
        print("hello")
        with open(f"{name}.txt","w") as f:
            f.write("\n".join(outp))
    else:
        print("\n".join(outp))
        
def counter(tokens, num):
    counter = Counter(tokens)
    total_count = sum(counter.values())
    type(num)
    relative = [(word, (int(count) / total_count) * num) if isinstance(count, (int, float)) else (word, 0) for word, count in counter.most_common()]

    return counter, relative
    

def main():
    doc = """Usage:
    ftl-occ <file> -a 
    ftl-occ <file> -m <int>
    ftl-occ <file> -j <saida_json>
    ftl-occ <file> -a -m <int>
    ftl-occ <file> -a -j <saida_json>
    ftl-occ <file> -m <int> -j <saida_json>
    ftl-occ <file> -a -m <int> -j <saida_json>
    """
    args = docopt(doc) 
    
    tokens = []
    
    if args.get("<file>"):
        with open('ficheiro.txt', 'r') as file:
            content = file.readlines()
    
    for txt in content:
        l = lexer(txt)
        tokens.extend(l)
    
    num = args.get("<int>") if args.get("-m") else 1000000
    
    print(num)
    
    absolute, relative = counter(tokens, float(num))    
    
    pretty_print(absolute,relative, args.get("-a"), args.get("<saida_json>"))



        