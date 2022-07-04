from ast import literal_eval

def escape(text):
    nsum = 0
    with open(text, 'r') as file:
        for line in file.readlines():
            nsum += len(line[:-1]) - len(eval(line[:-1]))
    print(nsum)

def escape2(text):
    nsum = 0
    with open(text, 'r') as file:
        for line in file.readlines():
            nsum += len(repr(line[:-1])) - len(line[:-1])
    print(nsum)

escape2("input.txt")
a = b'\x00\x01'
ra = repr(a)
print(literal_eval(literal_eval(ra)))