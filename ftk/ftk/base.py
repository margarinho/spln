# Base.py
# Last update 12 de março de 2025

from docopt import docopt
from ftk.utils import pretty_print, lexer, read_txt, read_pkl, read_txt, counter_transformation
from ftk.calcus import counter, normalization

def main():
    doc = """Usage:
    ftl-occ <f_input> -a 
    ftl-occ <f_input> -m <int>
    ftl-occ <f_input> -a -j <f_output>
    ftl-occ <f_input> -m <int> -j <f_output>
    """
    args = docopt(doc) 
    
    tokens = []
    
    f_input = args.get("<f_input>")
    
    upload_data = read_txt(f_input)
    regex = r'\w+(?:-\w+)*|[^\w\s]+'
    
    for txt in upload_data:
        l = [item.lower() for item in lexer(regex, txt)]
        tokens.extend(l)
    
    num = args.get("<int>") if args.get("-m") else 1000000
    
    absolute, relative = counter(tokens, float(num))   
    
    total = sum(absolute.values())
    
    # maybe make it better
    data = absolute if args.get("-a") else relative
    
    print("Print do counter para imprimir: ", data)
    
    pretty_print((total, data), args.get("<f_output>"))


def suprise_main():
    doc = """Usage:
    ftl-sup -s <file_long> <num>
    ftl-sup -pt <file_ref> <file_cor>
    """
    args = docopt(doc) 
    
    to_print = None
        
    if args.get("-s") and args.get("<file_long>") and args.get("<num>"):
        num = args.get("<num>")
        upload_data = read_txt(args.get("<file_long>"))
        counter = counter_transformation(upload_data)
        
        to_print = (counter, float(num), "ref_.pkl")
    
    elif args.get("-pt") and args.get("<file_ref>") and args.get("<file_cor>"):
        counter_ref = read_pkl(args.get("<file_ref>"))
        counter_cor = read_pkl(args.get("<file_cor>"))
        output = normalization(counter_ref, counter_cor)
        
        to_print = (output, 3, None)
        
    else:
        print("Try again")
        return
    
    total_output = sum(to_print[0].values())
    
    filter_output = {key: to_print[0].get(key) for key in to_print[0].keys() if to_print[0].get(key) > to_print[1]}
    
    pretty_print((total_output, dict(sorted(filter_output.items(), key=lambda item: item[1]))), to_print[2])
