with open("jour17Input.txt") as lines:
    for line in lines:
        input = line

# print(input)
def moveHorizontal(shape,grid,left):
    newShapePosition = []
    if left=="<":
        for bloc in shape:
            if bloc[1] == 0 or grid[bloc[0]][bloc[1]-1] != ".":
                return shape
            newShapePosition.append((bloc[0],bloc[1]-1))
        return newShapePosition
    for bloc in shape:
        if bloc[1] == 6 or grid[bloc[0]][bloc[1]+1] != ".":
            return shape
        newShapePosition.append((bloc[0],bloc[1]+1))
    return newShapePosition

def moveDown(shape, grid, currentMaxHeight):
    newShapePosition = []
    for bloc in shape:
        if bloc[0] == 0 or grid[bloc[0]-1][bloc[1]] != ".":
            #The shape stops here
            for bloc in shape:
                grid[bloc[0]][bloc[1]] = "#"
                if bloc[0]+1 > currentMaxHeight:
                    currentMaxHeight = bloc[0]+1
            return (shape,grid,False, currentMaxHeight)
        newShapePosition.append((bloc[0]-1,bloc[1]))
    return (newShapePosition,grid,True, currentMaxHeight)

def spawnNewShape(shape, grid, currentMaxHeight, gridOffset):
    newShape = []
    grid += [[".",".",".",".",".",".","."]for i in range(currentMaxHeight+7-(len(grid)+gridOffset))]
    for bloc in shape:
        newShape.append((bloc[0]+currentMaxHeight,bloc[1]))
    return (newShape,grid)

def printGrid(grid):
    for line in range(len(grid)-1,-1,-1):
        print(grid[line])

def main(input):
    currentShape = 0
    grid = [[".",".",".",".",".",".","."]for i in range(7)]

    shapes = [[(3,2),(3,3),(3,4),(3,5)],
            [(4,2),(4,3),(4,4),(3,3),(5,3)],
            [(3,2),(3,3),(3,4),(4,4),(5,4)],
            [(3,2),(4,2),(5,2),(6,2)],
            [(3,2),(3,3),(4,2),(4,3)]]

    currentMaxHeight = 0
    currentWind = 0
    inputLen = len(input)
    # print("input len :", inputLen)
    gridOffset = 0

    for numberOfShapesToSpawn in range(1000000-999248):
        # print(numberOfShapesToSpawn/1000000000000*100, "%")
        shape, grid = spawnNewShape(shapes[currentShape], grid, currentMaxHeight, gridOffset)

        currentShape = (currentShape+1)%5
        movedDown = True
        while(movedDown):
            shape = moveHorizontal(shape,grid,input[currentWind])
            currentWind = (currentWind+1)%inputLen

            shape, grid, movedDown, currentMaxHeight = moveDown(shape, grid, currentMaxHeight)
    print("Total height :", currentMaxHeight)


main(input)
# 1597714285692