import sys

def reading_from_standrinput():
    uniqlines =  []
    while True:
        line = input("> ")
        if line not in uniqlines and not "":
            uniqlines.append(line)
        print ("\n".join(str(x) for x in uniqlines))
    
def reading_from_file(filename):
    uniqlines = []
    for line in open(filename, 'r').readlines():
        if line not in uniqlines:
            uniqlines.append(line)
    print("".join(str(x) for x in uniqlines))

if __name__ == "__main__":
    n = len(sys.argv)
    if n == 1:
        reading_from_standrinput()
    else:
        reading_from_file(sys.argv[1])