from xmlrpc.server import SimpleXMLRPCRequestHandler
import numpy

def turn(array, bit, startingCoords, endingCoords):
    x,y = startingCoords
    while y <= endingCoords[1]:
        while x <= endingCoords[0]:
            array[y][x] = bit
            x += 1
        x = startingCoords[0]
        y += 1

def toggle(array, startingCoords, endingCoords):
    x,y = startingCoords
    while y <= endingCoords[1]:
        while x <= endingCoords[0]:
            array[y][x] = 0 if array[y][x] == 1 else 1
            x += 1
        x = startingCoords[0]
        y += 1

def lights(text):
    lightsList = numpy.zeros((1000, 1000))
    with open(text, 'r') as file:
        for line in file.readlines():
            instruction = line.split(" ")
            if instruction[0] == "turn" and instruction[1] == "on":
                startingCoords = [int(n) for n in instruction[2].split(",")]
                endingCoords = [int(n) for n in ((instruction[4])[:-1]).split(",")]
                turn(lightsList, 1, startingCoords, endingCoords)
            elif instruction[0] == "turn" and instruction[1] == "off":
                startingCoords = [int(n) for n in instruction[2].split(",")]
                endingCoords = [int(n) for n in ((instruction[4])[:-1]).split(",")]
                turn(lightsList, 0, startingCoords, endingCoords)
            elif instruction[0] == "toggle":
                startingCoords = [int(n) for n in instruction[1].split(",")]
                endingCoords = [int(n) for n in ((instruction[3])[:-1]).split(",")]
                toggle(lightsList, startingCoords, endingCoords)
    return numpy.sum(lightsList)


if __name__ == "__main__":
    print(lights("input.txt"))
   