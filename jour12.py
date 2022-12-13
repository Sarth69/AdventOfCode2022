grid=[["" for i in range(81)] for j in range(41)]
# grid = [["" for i in range(8)] for j in range(5)]
i = 0
aList = [(20,0)]
minDist = 10000000

with open("jour12Input.txt") as lines:
    for line in lines:
        line = line.strip()
        for j,letter in enumerate(line):
            if letter == "S":
                grid[i][j] = "a"
            elif letter == "E":
                grid[i][j] = "z"
            else:
                grid[i][j] = letter
            if letter == "a":
                aList.append((i,j))
        i+=1
# print(grid)

for a in aList:
    nodesToExplore = [a] #x,y
    # nodesToExplore = [(0,0)]
    visited = [[-1 for i in range(81)] for j in range(41)]
    # visited = [[-1 for i in range(8)] for j in range(5)]
    visited[a[0]][a[1]] = 0
    # visited[0][0] = 0

    while(len(nodesToExplore) > 0):
        currentNode = nodesToExplore.pop(0)
        # print(currentNode)
        # print(currentNode, visited[currentNode[0]][currentNode[1]])
        if currentNode[0] > 0:
            if abs(ord(grid[currentNode[0]][currentNode[1]])-ord(grid[currentNode[0]-1][currentNode[1]])) <= 1 or \
                ord(grid[currentNode[0]][currentNode[1]]) > ord(grid[currentNode[0]-1][currentNode[1]]):
                # print(grid[currentNode[0]][currentNode[1]], grid[currentNode[0]-1][currentNode[1]])
                if visited[currentNode[0]-1][currentNode[1]] == -1:
                    visited[currentNode[0]-1][currentNode[1]] = visited[currentNode[0]][currentNode[1]] + 1
                    nodesToExplore.append((currentNode[0]-1, currentNode[1]))
                else:
                    visited[currentNode[0]-1][currentNode[1]] = min(visited[currentNode[0]][currentNode[1]] + 1, visited[currentNode[0]-1][currentNode[1]])
        if currentNode[0] < len(grid)-1:
            if abs(ord(grid[currentNode[0]][currentNode[1]])-ord(grid[currentNode[0]+1][currentNode[1]])) <= 1 or \
                ord(grid[currentNode[0]][currentNode[1]]) > ord(grid[currentNode[0]+1][currentNode[1]]):
                # print(grid[currentNode[0]][currentNode[1]], grid[currentNode[0]+1][currentNode[1]])
                if visited[currentNode[0]+1][currentNode[1]] == -1:
                    visited[currentNode[0]+1][currentNode[1]] = visited[currentNode[0]][currentNode[1]] + 1
                    nodesToExplore.append((currentNode[0]+1, currentNode[1]))
                else:
                    visited[currentNode[0]+1][currentNode[1]] = min(visited[currentNode[0]][currentNode[1]] + 1, visited[currentNode[0]+1][currentNode[1]])
        if currentNode[1] > 0:
            if abs(ord(grid[currentNode[0]][currentNode[1]])-ord(grid[currentNode[0]][currentNode[1]-1])) <= 1 or \
                ord(grid[currentNode[0]][currentNode[1]]) > ord(grid[currentNode[0]][currentNode[1]-1]):
                # print(grid[currentNode[0]][currentNode[1]], grid[currentNode[0]][currentNode[1]-1])
                if visited[currentNode[0]][currentNode[1]-1] == -1:
                    visited[currentNode[0]][currentNode[1]-1] = visited[currentNode[0]][currentNode[1]] + 1
                    nodesToExplore.append((currentNode[0], currentNode[1]-1))
                else:
                    visited[currentNode[0]][currentNode[1]-1] = min(visited[currentNode[0]][currentNode[1]] + 1, visited[currentNode[0]][currentNode[1]-1])
        if currentNode[1] < len(grid[0])-1:
            if abs(ord(grid[currentNode[0]][currentNode[1]])-ord(grid[currentNode[0]][currentNode[1]+1])) <= 1 or \
                ord(grid[currentNode[0]][currentNode[1]]) > ord(grid[currentNode[0]][currentNode[1]+1]):
                # print(grid[currentNode[0]][currentNode[1]], grid[currentNode[0]][currentNode[1]+1])
                if visited[currentNode[0]][currentNode[1]+1] == -1:
                    visited[currentNode[0]][currentNode[1]+1] = visited[currentNode[0]][currentNode[1]] + 1
                    nodesToExplore.append((currentNode[0], currentNode[1]+1))
                else:
                    visited[currentNode[0]][currentNode[1]+1] = min(visited[currentNode[0]][currentNode[1]] + 1, visited[currentNode[0]][currentNode[1]+1])
    # print(visited[2][5])
    if visited[20][58] < minDist and visited[20][58] > 0:
        minDist = visited[20][58]

print(minDist)