def sues(text, tape, part):
    tapeDict = dict()
    with open(tape, 'r') as file:
        for line in file.readlines():
            line = line[:-1].split(":")
            tapeDict[line[0]] = int(line[1][1])
    with open(text, 'r') as file:
        for line in file.readlines():
            # Sue 1: cars: 9, akitas: 3, goldfish: 0
            line = line[:-1].split(" ")
            atr1, atr2, atr3 = (line[2][:-1], int(line[3][:-1])), (line[4][:-1], int(line[5][:-1])), (line[6][:-1], int(line[7]))
            if part == 1:
                if tapeDict[atr1[0]] == atr1[1] and tapeDict[atr2[0]] == atr2[1] and tapeDict[atr3[0]] == atr3[1]:
                    return line[1][:-1]
            elif part == 2:
                attributeCount = 0
                attributes = [atr1, atr2, atr3]
                for attribute in attributes:
                    if attribute[0] == "cats" or attribute[0] == "trees":
                        if attribute[1] > tapeDict[attribute[0]]:
                            attributeCount += 1
                    elif attribute[0] == "pomeranians" or attribute[0] == "goldfish":
                        if attribute[1] < tapeDict[attribute[0]]:
                            attributeCount += 1
                    elif attribute[1] == tapeDict[attribute[0]]:
                        attributeCount += 1
                if attributeCount == 3:
                    return line[1][:-1]
    return 0

if __name__ == "__main__":
    print(sues("input.txt", "tape.txt", 2))