import itertools

def eggnogg(text, liters, part):
    containers = []
    with open(text, 'r') as file:
        for line in file.readlines():
            containers.append(int(line[:-1]))
    if part == 1:
        goodCombinations = 0
        for i in range(1, len(containers)):
            for combination in itertools.combinations(containers, i):
                if sum(combination) == liters:
                    goodCombinations += 1
        return goodCombinations
    elif part == 2:
        minContainers = 0
        for i in range(1, len(containers)):
            for combination in itertools.combinations(containers, i):
                if sum(combination) == liters:
                    minContainers = len(combination)
                    break
            if minContainers != 0:
                break
        goodCombinations = 0
        for combination in itertools.combinations(containers, minContainers):
            if sum(combination) == liters:
                goodCombinations += 1
        return goodCombinations
        

if __name__ == "__main__":
    print(eggnogg("input.txt", 150, 2))
