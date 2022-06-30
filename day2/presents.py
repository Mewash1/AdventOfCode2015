def paperCount(text):
    paperSum = 0
    with open(text, 'r') as file:
        for present in file.readlines():
            dimensions = present[0:-1].split('x')
            a,b,c = int(dimensions[0]) * int(dimensions[1]), int(dimensions[1]) * int(dimensions[2]), int(dimensions[0]) * int(dimensions[2])
            paperSum += 2 * a + 2 * b + 2 * c + min(a,b,c)
    return paperSum

def paperCountWithRibbon(text):
    paperSum = 0
    with open(text, 'r') as file:
        for present in file.readlines():
            if present == "":
                break
            dimensions = present[0:-1].split('x')
            a,b,c = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
            dimSet = [a,b,c]
            smallest = min(dimSet)
            dimSet.remove(smallest)
            middle = min(dimSet)

            paperSum += a * b * c + 2 * smallest + 2 * middle
    return paperSum

if __name__ == "__main__":
    print(paperCount("input.txt"))
    print(paperCountWithRibbon("input.txt"))