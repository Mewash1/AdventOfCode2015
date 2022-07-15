def molecules(text):
    with open(text, 'r') as file:
        textList = file.readlines()
    textList = [line[:-1] for line in textList]
    molecule = textList[-1]
    moleculeSet = set()
    for production in textList:
        if production == "":
            break
        key, arrow, value = production.split(" ")
        for i in range(len(molecule) - len(key) + 1):
            if key == molecule[i:i+len(key)]:
                moleculeSet.add(molecule[:i] + value + molecule[i+len(key):])
    return len(moleculeSet)


def genMolecule(text):
    with open(text, 'r') as file:
        textList = file.readlines()
    textList = [line[:-1] for line in textList]
    molecule = textList[-1]
    for production in textList:
        if production == "":
            break
        key, arrow, value = production.split(" ")

if __name__ == "__main__":
    print(molecules("input.txt"))
    # b => ABC
    x = "abc"
    y = "ABC"
    print(x[:1] + y + x[2:])