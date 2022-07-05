import json

def addNumbersInJson(jason):
    jsum = 0
    if isinstance(jason, list):
        for element in jason:
            partialSum = addNumbersInJson(element)
            jsum += partialSum
        return jsum
    elif isinstance(jason, dict):
        for key, value in jason.items():
            if value == "red":
                jsum = 0
                break
            partialSum = addNumbersInJson(value)
            jsum += partialSum
        return jsum
    elif isinstance(jason, str):
        return 0
    elif isinstance(jason, int):
        return jason


if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        jason = json.load(file)
    print(addNumbersInJson(jason))