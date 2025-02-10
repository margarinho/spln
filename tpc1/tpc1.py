import sys

def reading_from_stdin(keyword=None):
    uniqlines =  []
    while True:
        line = input("> ")
        if line not in uniqlines and not "":
            if keyword is None or keyword in line:
                uniqlines.append(line)
        print ("\n".join(str(x) for x in uniqlines))
    
def reading_from_file(filename, keyword=None):
    uniqlines = []
    for line in open(filename, 'r').readlines():
        if line not in uniqlines:
            if keyword is None or keyword in line:
                uniqlines.append(line)
    print("".join(str(x) for x in uniqlines))

if __name__ == "__main__":
    keyword = sys.argv[2] if len(sys.argv) > 2 else None 
    if len(sys.argv) == 1:
        reading_from_stdin(keyword)
    else:
        reading_from_file(sys.argv[1], keyword)
