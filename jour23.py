grid = []
gridImprove = 100
gridSize = (0,0)

with open("jour23Input.txt") as lines:
    for line in lines:
        line = line.strip()
        grid.append([i for i in line])

for i in range(len(grid)):
    grid[i] = ["." for i in range(gridImprove)] + grid[i] + ["." for i in range(gridImprove)]
grid = [["." for i in range(len(grid[0]))]for i in range(gridImprove)] + grid + [["." for i in range(len(grid[0]))]for i in range(gridImprove)]
gridSize = (len(grid),len(grid[0]))
directions =["N","S","W","E"]
round = 0
while True:
    round += 1
    movementWishes = {}
    pairsThatWontBeReached = []
    #first half
    for i in range(gridSize[0]):
        for j in range(gridSize[1]):
            if grid[i][j] == "#":
                move = False
                if i == 0 or j == 0 or j == gridSize[1]-1 or i == gridSize[0]-1:
                    print("grid too small")
                    break
                if grid[i-1][j-1] == "#":
                    move = True
                if grid[i-1][j] == "#":
                    move = True
                if grid[i-1][j+1] == "#":
                    move = True
                if grid[i+1][j] == "#":
                    move = True
                if grid[i+1][j-1] == "#":
                    move = True
                if grid[i+1][j+1] == "#":
                    move = True
                if grid[i][j+1] == "#":
                    move = True
                if grid[i][j-1] == "#":
                    move = True
                if move:
                    for direction in directions:
                        match direction:
                            case "N":
                                if grid[i-1][j] == "." and grid[i-1][j-1] == "." and grid[i-1][j+1] == ".":
                                    if (i-1,j) not in movementWishes.values():
                                        movementWishes[(i,j)] = (i-1,j)
                                    else:
                                        pairsThatWontBeReached.append((i-1,j))
                                    break
                            case "S":
                                if grid[i+1][j] == "." and grid[i+1][j-1] == "." and grid[i+1][j+1] == ".":
                                    if (i+1,j) not in movementWishes.values():
                                        movementWishes[(i,j)] = (i+1,j)
                                    else:
                                        pairsThatWontBeReached.append((i+1,j))
                                    break
                            case "E":
                                if grid[i][j+1] == "." and grid[i+1][j+1] == "." and grid[i-1][j+1] == ".":
                                    if (i,j+1) not in movementWishes.values():
                                        movementWishes[(i,j)] = (i,j+1)
                                    else:
                                        pairsThatWontBeReached.append((i,j+1))
                                    break
                            case "W":
                                if grid[i][j-1] == "." and grid[i+1][j-1] == "." and grid[i-1][j-1] == ".":
                                    if (i,j-1) not in movementWishes.values():
                                        movementWishes[(i,j)] = (i,j-1)
                                    else:
                                        pairsThatWontBeReached.append((i,j-1))
                                    break
                            case _:
                                print("error direction doesn't exist")
    #second half
    # print(round, movementWishes.values())
    if len(movementWishes.keys()) == 0:
        print("FINISHED ", round)
        break
    for key in movementWishes.keys():
        if movementWishes[key] not in pairsThatWontBeReached:
            grid[key[0]][key[1]] = "."
            grid[movementWishes[key][0]][movementWishes[key][1]] = "#"
    directions = directions[1:]+[directions[0]]
    # print(round,grid)

#Compute min and max
minX = len(grid)
minY = len(grid[0])
maxX = 0
maxY = 0
numberOfElves = 0
for i in range(gridSize[0]):
    for j in range(gridSize[1]):
        if grid[i][j] == "#":
            numberOfElves += 1
            if i < minX:
                minX = i
            if i > maxX:
                maxX = i
            if j < minY:
                minY = j
            if j > maxY:
                maxY = j

print(maxX,maxY,minX,minY)
print((maxX-minX+1)*(maxY-minY+1)-numberOfElves)
