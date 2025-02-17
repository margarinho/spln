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

    for line in data:
        if line not in uniqlines or line == "\n":
            if flags['h'] and line == "\n":
                line = "#\n"
            uniqlines.append(line)

    print("".join(uniqlines))

def main():
    try: 
        opts, args = getopt.getopt(sys.argv[1:], "f:s:e:h", ["file=", "spaces", "empty", "hash"]) 
    except getopt.GetoptError as err: 
        print(f"Error: {err}") 
        sys.exit(1)

    flags = {
        "d": None,
        "s": False,
        "e": False,
        "h": False,
    }

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
        flags['d'] = open(file, "r").read()
    else:
        flags['d'] = sys.stdin.read()

    rm_lines(flags)

if __name__ == "__main__":
    main()
