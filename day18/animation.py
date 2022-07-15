import numpy
import sys
import copy

def genBoard(text):
    with open(text, 'r') as file:
        lights = file.readlines()
    lights = [line[:-1] for line in lights]
    board = numpy.zeros((len(lights[0]), len(lights)))
    for i in range(100):
        for j in range(100):
            if lights[i][j] == "#":
                board[i][j] = 1
    return board

def animation(text, rounds):
    board = genBoard(text)
    coordinates = [(-1, -1), (1, 1), (-1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
    corners = set([(0,0), (0, 99), (99, 0), (99, 99)])
    for corner in corners:
        board[corner[0], corner[1]] = 1
    for _ in range(rounds):
        newBoard = copy.deepcopy(board)
        for i in range(100):
            for j in range(100):
                if (i, j) not in corners:
                    onNeighbours = 0
                    offNeighbours = 0
                    for coord in coordinates:
                        y, x = coord[0] + i, coord[1] + j
                        if y < 0 or x < 0 or y >= 100 or x >= 100:
                            offNeighbours += 1
                        elif board[y][x] == 0:
                            offNeighbours += 1
                    onNeighbours = 8 - offNeighbours
                    if board[i][j] == 1:
                        if onNeighbours != 2 and onNeighbours != 3:
                            newBoard[i][j] = 0
                    if board[i][j] == 0:
                        if onNeighbours == 3:
                            newBoard[i][j] = 1
        board = newBoard
    return sum(numpy.nditer(board))


if __name__ == "__main__":
    numpy.set_printoptions(threshold=sys.maxsize)
    print(animation("input.txt", 100))