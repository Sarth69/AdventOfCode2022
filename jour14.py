import re

minX = 500
maxX = 500
maxY = 0

with open("jour14Input.txt") as lines:
    for line in lines:
        line = line.strip()
        values = line.split(" -> ")
        for value in values:
            match = re.match("([0-9]*)\,([0-9]*)", value)
            if int(match[1]) > maxX:
                maxX = int(match[1])
            if int(match[1]) < minX:
                minX = int(match[1])
            if int(match[2]) > maxY:
                maxY = int(match[2])

print(minX, maxX, maxY)
minX -= maxY
maxX += maxY
grid = [["air" for i in range(maxY+3)] for i in range(minX, maxX+1)]

with open("jour14Input.txt") as lines:
    for line in lines:
        line = line.strip()
        values = line.split(" -> ")
        begin = re.match("([0-9]*)\,([0-9]*)", values[0])
        begin = (int(begin[1]), int(begin[2]))
        for k in range(1,len(values)):
            match = re.match("([0-9]*)\,([0-9]*)", values[k])
            for i in range(min(begin[0],int(match[1])), max(begin[0],int(match[1]))+1):
                for j in range(min(begin[1],int(match[2])), max(begin[1],int(match[2]))+1):
                    grid[i-minX][j] = "rock"
            begin = (int(match[1]), int(match[2]))

#Add the infinite bottom
for i in range(maxX-minX+1):
    grid[i][-1] = "rock"

count = 0

def generateSand(grid):
    if grid[500-minX][0] != "air":
        print("here")
        return grid,False
    sandPos = (500-minX, 0)
    while True:
        # if sandPos[1] == maxY:
        #     print("there")
        #     return grid, False
        if grid[sandPos[0]][sandPos[1]+1] == "air":
            sandPos = (sandPos[0], sandPos[1]+1)
            continue
        if sandPos[0] == 0:
            print("there2")
            return grid, False
        if grid[sandPos[0]-1][sandPos[1]+1] == "air":
            sandPos = (sandPos[0]-1, sandPos[1]+1)
            continue
        if sandPos[0] == maxX-minX:
            print("there3")
            return grid, False
        if grid[sandPos[0]+1][sandPos[1]+1] == "air":
            sandPos = (sandPos[0]+1, sandPos[1]+1)
        else:
            grid[sandPos[0]][sandPos[1]] = "sand"
            return grid, True

while True:
    grid, newSand = generateSand(grid)
    if newSand:
        count += 1
    else:
        break

print(count)