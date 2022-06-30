def floorDecoder(text):
    with open(text, 'r') as file:
        floor = 0
        for char in file.readline():
            floor += 1 if char == '(' else -1
    return floor

def positionDecoder(text):
    with open(text, 'r') as file:
        floor = 0
        for i, char in enumerate(file.readline()):
            floor += 1 if char == '(' else -1
            if floor == -1:
                return i + 1

if __name__ == '__main__':
    print(floorDecoder("input.txt"))
    print(positionDecoder("input.txt"))