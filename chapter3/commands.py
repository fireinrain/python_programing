from sys import argv
from scanfile import  scanner
class UnknowCommand(Exception):pass

def processLine(line):
    if line[0]=='*':
        print('Ms',line[1:-1])
    elif line[0]=='+':
        print('Mr',line[1:-1])
    else:
        raise UnknowCommand(line)
filename='dataa.txt'
if len(argv)==2:filename=argv[1]
scanner(filename,processLine)