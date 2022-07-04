def getValueFromRegister(outputDict, key: str):
    if key.isnumeric():
        return int(key)
    elif key not in outputDict:
        outputDict[key] = -1
    return outputDict[key] 

def gates(text):
    outputDict = dict()
    with open(text, 'r') as file:
        instructionSet = file.readlines()
        while len(instructionSet) != 0:
            for line in instructionSet:
                checkRemove = False
                instruction = (line[:-1]).split(" ")
                if instruction[0] == "NOT":
                    # NOT x -> y
                    arg, output = getValueFromRegister(outputDict, instruction[1]), instruction[3]
                    if arg != -1:
                        checkRemove = True
                        outputDict[output] = ~(arg) % 65536
                elif instruction[1] == "AND":
                    # x AND y -> z
                    arg1, arg2, output = getValueFromRegister(outputDict, instruction[0]), getValueFromRegister(outputDict, instruction[2]), instruction[4]
                    if arg1 != -1 and arg2 != -1:
                        checkRemove = True
                        outputDict[output] = (arg1 & arg2) % 65536
                elif instruction[1] == "OR":
                    # x OR y -> z
                    arg1, arg2, output = getValueFromRegister(outputDict, instruction[0]), getValueFromRegister(outputDict, instruction[2]), instruction[4]
                    if arg1 != -1 and arg2 != -1:
                        checkRemove = True
                        outputDict[output] = (arg1 | arg2) % 65536
                elif instruction[1] == "LSHIFT":
                    # x LSHIFT 2 -> z
                    arg1, arg2, output = getValueFromRegister(outputDict, instruction[0]), getValueFromRegister(outputDict, instruction[2]), instruction[4]
                    if arg1 != -1 and arg2 != -1:
                        checkRemove = True
                        outputDict[output] = (arg1 << arg2) % 65536
                elif instruction[1] == "RSHIFT":
                    # x RSHIFT 2 -> z
                    arg1, arg2, output = getValueFromRegister(outputDict, instruction[0]), getValueFromRegister(outputDict, instruction[2]), instruction[4]
                    if arg1 != -1 and arg2 != -1:
                        checkRemove = True
                        outputDict[output] = (arg1 >> arg2) % 65536
                else:
                    # x -> y
                    arg, output = getValueFromRegister(outputDict, instruction[0]), instruction[2]
                    if arg != -1:
                        checkRemove = True
                        outputDict[output] = arg
                if checkRemove:
                    instructionSet.remove(line)
    return outputDict["a"]


if __name__ == "__main__":
    print(gates("input2.txt"))