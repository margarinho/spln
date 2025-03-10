from docopt import docopt
import re

def pretty_print(list_c):
    for (value, word) in list_c:
        print(f"{value}    {word}")
        
def parsing(line):
    n = [item.strip() for item in re.split(r'[\t ]+', line)]  
    return (int(n[0]), n[1])

def reading(path_pt):
    filtered_lines = []
    with open(path_pt, "r") as f:
         for line in f:
            filtered_line = parsing(line)
            filtered_lines.append(filtered_line)
    
    return  filtered_lines 

def filter_tuples(tuples_list, num):
    return [tup for tup in tuples_list if tup[0] > num]

def corresp (tuples_pt, tuples_txt):
    tuples = []
    zero = 1 /  sum([x[0] for x in tuples_pt])
    for t in tuples_txt:
        match = next((item for item in tuples_pt if item[1] == t[1]), (zero,t[1]))
        r = t[0] / match[0]
        tuples.append((r,t[1]))
        
    return tuples


def main():
    doc = """Usage:
    ftl-freq -pt <file>
    """
    args = docopt(doc) 
    
    if not args.get("<file>"):
        return
    
    path_pt = "formas.totalpt.txt"
    tuples_pt = filter_tuples( reading(path_pt), 1)
    
    tuples_txt1 = [(1634, 'drenagem'),
                (1634, 'Calheiros'),
                (1632, 'violinista'),
                (1632, 'veria'),
                (1632, 'velejadores'),
                (1632, 'unitário'),
                (1632, 'rupturas')
                ]
    
    tuples_txt2 = filter_tuples( reading(args.get("<file>")), 0)
    
    c = corresp(tuples_pt, tuples_txt2)
    
    pretty_print(c)
    
    