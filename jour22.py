grid = [["" for i in range(150)] for j in range(200)] #200 lignes, 150 colonnes

readingGrid = True
movement = 0
direction = 0 # 0r1d2l3u
position = (0,50)
# position = (0,8)

def computeNextPosition(position, grid, direction, movement):
    newPosition = (position[0],position[1])
    newDirection = direction
    # print(position, direction, movement)
    
    while movement > 0:
        match direction:
            case 0:
                nextToTest = (newPosition[0], newPosition[1]+1)
                if newPosition[1]+1 == len(grid[0]) or grid[nextToTest[0]][nextToTest[1]] in [" ",""]:
                    if 0 <= nextToTest[0] <= 49:
                        nextToTest = (149-nextToTest[0],100)
                        newDirection = 2
                    elif 50 <= nextToTest[0] <= 99:
                        nextToTest = (49,50+nextToTest[0])
                        newDirection = 3
                    elif 100 <= nextToTest[0] <= 149:
                        nextToTest = (149-nextToTest[0],149)
                        newDirection = 2
                    else:
                        nextToTest = (149,nextToTest[0]-100)
                        newDirection = 3
                if grid[nextToTest[0]][nextToTest[1]] == "#":
                    return (newPosition[0],newPosition[1]), direction
                newPosition = nextToTest
                direction = newDirection
            case 1:
                nextToTest = (newPosition[0]+1, newPosition[1])
                if newPosition[0]+1 == len(grid) or grid[nextToTest[0]][nextToTest[1]] in [" ",""]:
                    if 0 <= nextToTest[1] <= 49:
                        nextToTest = (0,100+nextToTest[1])
                        newDirection = 1
                    elif 50 <= nextToTest[1] <= 99:
                        nextToTest = (100+nextToTest[1],49)
                        newDirection = 2
                    else:
                        nextToTest = (nextToTest[1]-50,99)
                        newDirection = 2
                if grid[nextToTest[0]][nextToTest[1]] == "#":
                    return newPosition, direction
                newPosition = nextToTest
                direction = newDirection
            case 2:
                nextToTest = (newPosition[0], newPosition[1]-1)
                if newPosition[1] == 0 or grid[nextToTest[0]][nextToTest[1]] in [" ",""]:
                    if 0 <= nextToTest[0] <= 49:
                        nextToTest = (149-nextToTest[0],0)
                        newDirection = 0
                    elif 50 <= nextToTest[0] <= 99:
                        nextToTest = (100,nextToTest[0]-50)
                        newDirection = 1
                    elif 100 <= nextToTest[0] <= 149:
                        nextToTest = (149-nextToTest[0],50)
                        newDirection = 0
                    else:
                        nextToTest = (0,nextToTest[0]-100)
                        newDirection = 1
                if grid[nextToTest[0]][nextToTest[1]] == "#":
                    return (newPosition[0],newPosition[1]), direction
                newPosition = nextToTest
                direction = newDirection
            case 3:
                nextToTest = (newPosition[0]-1, newPosition[1])
                if newPosition[0] == 0 or grid[nextToTest[0]][nextToTest[1]] in [" ",""]:
                    if 0 <= nextToTest[1] <= 49:
                        nextToTest = (50+nextToTest[1],50)
                        newDirection = 0
                    elif 50 <= nextToTest[1] <= 99:
                        nextToTest = (100+nextToTest[1],0)
                        newDirection = 0
                    else:
                        nextToTest = (199,nextToTest[1]-100)
                        newDirection = 3
                if grid[nextToTest[0]][nextToTest[1]] == "#":
                    return (newPosition[0],newPosition[1]), direction
                newPosition = nextToTest
                direction = newDirection
        movement -= 1
    return newPosition, direction

            

with open("jour22Input.txt") as lines:
    for k,line in enumerate(lines):
        if line == "\n":
            readingGrid = False
        if readingGrid:
            for i in range(len(line)-1):
                grid[k][i] = line[i]
        else:
            directions = line.strip()

while directions != "":
    leftIndex = directions.find("L")
    rightIndex = directions.find("R")
    print(direction)
    if leftIndex == -1 and rightIndex == -1:
        #Final move
        position, direction = computeNextPosition(position, grid, direction, int(directions))
        break
    if leftIndex < rightIndex or rightIndex == -1:
        movement = int(directions[:leftIndex])
        directions = directions[leftIndex+1:]
        position, direction = computeNextPosition(position, grid, direction, movement)
        direction = (direction-1)%4
    else:
        movement = int(directions[:rightIndex])
        directions = directions[rightIndex+1:]
        position, direction = computeNextPosition(position, grid, direction, movement)
        direction = (direction+1)%4
    # print(movement)
    # input(position)
    # print("after",position, movement, direction)
# print("after",position, movement, direction)
        

print(position, 1000*(position[0]+1)+4*(position[1]+1)+direction)
