def grid(text):
    x, y = 0,0 
    gridSum = 0
    gridSet = set()
    with open(text, 'r') as file:
        for char in file.readline():
            if (x, y) not in gridSet:
                gridSum += 1
                gridSet.add((x,y))
            if char == '^':
                y += 1
            elif char == 'v':
                y -= 1
            elif char == '>':
                x += 1
            elif char == '<':
                x -= 1
    return gridSum

def robotGrid(text):
    xs, ys, xr, yr = 0,0,0,0 
    gridSum = 0
    gridSet = set()
    with open(text, 'r') as file:
        for i, char in enumerate(file.readline()):
            if i % 2 == 0:
                x,y = xs, ys
            else:
                x,y = xr, yr

            if (x, y) not in gridSet:
                gridSum += 1
                gridSet.add((x,y))
            if char == '^':
                y += 1
            elif char == 'v':
                y -= 1
            elif char == '>':
                x += 1
            elif char == '<':
                x -= 1
            
            if i % 2 == 0:
                xs,ys = x, y
            else:
                xr,yr = x, y

    return gridSum

if __name__ == "__main__":
    print(grid("input.txt"))
    print(robotGrid("input.txt"))