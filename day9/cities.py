from cmath import inf
import itertools

def cities(text):
    citiesDict = dict()
    with open(text, 'r') as file:
        for line in file.readlines():
            # X to Y = 1
            route = line[:-1].split(" ")
            if route[0] not in citiesDict:
                citiesDict[route[0]] = dict()
            if route[2] not in citiesDict:
                citiesDict[route[2]] = dict()
            citiesDict[route[0]][route[2]] = int(route[4])
            citiesDict[route[2]][route[0]] = int(route[4])
    allPaths = itertools.permutations(citiesDict.keys(), 8)
    currentSum = 0
    lowestSum = float(inf)
    highestSum = 0
    for path in allPaths:
        for i in range(len(path) - 1):
            currentSum += citiesDict[path[i]][path[i+1]]
        lowestSum = currentSum if currentSum < lowestSum else lowestSum
        highestSum = currentSum if currentSum > highestSum else highestSum
        currentSum = 0
    return lowestSum, highestSum

print(cities("input.txt"))