import itertools

def naughtyList(text):
    goodList = []
    badSet = {"ab", "cd", "pq", "xy"}
    with open(text, 'r') as file:
        stringList = file.readlines()
        for string in stringList:
            vowelsCount = 0
            charDict = dict()
            doubleCheck = False
            substringCheck = True
            for char in string:
                vowelsCount += 1 if char in "aeiou" else 0
                if char in charDict:
                    charDict[char] += 1
                else:
                    charDict[char] = 1
            if vowelsCount < 3:
                continue
            for key, value in charDict.items():
                if value >= 2 and key+key in string:
                    doubleCheck = True
                    break
            if not doubleCheck:
                continue
            for badSubstring in badSet:
                if badSubstring in string:
                    substringCheck = False
                    break
            if substringCheck:
                goodList.append(string)
    return goodList, len(goodList)


def longSubstring(key : str, text : str):
    firstCheck = False
    if key in text:
        newText = text.replace(key, '', 1)
        if key in newText:
            firstCheck = True
    if not firstCheck:
        return False
    if key[0] == key[1]:
        while len(key) < len(text):
            key += key[0]
            if key in text:
                return False
    else:
        while len(key) < len(text):
            key = key[0] + key + key[1]
            if key in text:
                return False
    return True

def letterInTheMiddle(key : str, text : str):
    for i in range(len(text) - 2):
        if text[i] == key and text[i+2] == key:
            return True
    return False

def betterNaughtyList(text):
    goodList = []
    with open(text, 'r') as file:
        stringList = file.readlines()
    for string in stringList:
        string = string[0:-1]
        doubleCheck = False
        middleCheck = False
        stringComb = set()
        stringUniqueLetters = list(set(string))

        for comb in itertools.combinations(string, 2):
            stringComb.add(comb[0] + comb[1])
        for comb in stringComb:
            doubleCheck = longSubstring(comb, string)
            if doubleCheck:
                break
        if doubleCheck:
            for char in stringUniqueLetters:
                middleCheck = letterInTheMiddle(char, string)
                if middleCheck:
                    goodList.append(string)
                    break
    return len(goodList)

if __name__ == "__main__":
    print(betterNaughtyList("input.txt"))
