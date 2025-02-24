'''
Repetidas - Remove linhas repetidas de um programa.

Usage - 
    repetidas options file*

Options
    -s      keep spaces
    -e      remove empty lines
    -h      put "#" in empty lines    
'''

import sys 
import getopt
import re

def rm_lines(flags):
    uniqlines = []

    data = map(str.strip, flags['d']) if flags['e'] and not flags['s'] else flags['d']
    c = "\n" if flags['e'] and not flags['s'] else ""
    
    for line in data:

        if line not in uniqlines or line in ["","\n"]:
            if flags['h'] and line in ["","\n"]:
                line = f"#{line}"
            uniqlines.append(line)

    print(c.join(uniqlines))

def main():
    try: 
        opts, args = getopt.getopt(sys.argv[1:], "f:seh", ["file=", "spaces", "empty", "hash"]) 
    except getopt.GetoptError as err: 
        print(f"Error: {err}") 
        sys.exit(1)

    flags = {
        "d": [],
        "s": False,
        "e": False,
        "h": False,
    }
    file=None

    for opt, arg in opts: 
        if opt in ("-f", "--file"):
            file = arg
        elif opt in ("-s", "--spaces"): 
            flags['s'] = True
        elif opt in ("-e", "--empty"): 
            flags['e'] = True
        elif opt in ("-h", "--hash"): 
            flags['h'] = True

        
    if file:
         with open(file, "r") as f:
            flags["d"] += f.readlines()
    
    try:
        for line in sys.stdin:
            flags["d"].append(line)
            rm_lines(flags)  # Processa cada nova entrada

    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
