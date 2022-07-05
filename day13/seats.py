# Alice would lose 57 happiness units by sitting next to Bob.
import itertools

from numpy import maximum

def seats(text):
    happinessDict = dict()
    with open(text, 'r') as file:
        happinessList = file.readlines()
    for guest in happinessList:
        guest = guest.split(" ")
        name, sign, value, neighbour = guest[0], guest[2], guest[3], guest[10][:-2]
        sign = -1 if sign == "lose" else 1
        if name not in happinessDict:
            happinessDict[name] = dict()
        happinessDict[name][neighbour] = sign * int(value)
    nameSet = set()
    happinessDict["You"] = dict()
    for name in happinessDict.keys():
        # start Part 2
        happinessDict["You"][name] = 0
        happinessDict[name]["You"] = 0
        # end Part 2
        nameSet.add(name)

    maximumHappiness = 0
    currentHappiness = 0
    for seating in itertools.permutations(nameSet, len(nameSet)):
        for i in range(-1, len(seating) - 1):
            currentHappiness += happinessDict[seating[i]][seating[i+1]] + happinessDict[seating[i+1]][seating[i]]
        maximumHappiness = currentHappiness if currentHappiness > maximumHappiness else maximumHappiness
        currentHappiness = 0
    return maximumHappiness

if __name__ == "__main__":
    print(seats("input.txt"))