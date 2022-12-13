grid=[]

with open("jour8Input.txt") as lines:
    for line in lines:
        line = line.strip()
        gridLine=[]
        for number in line:
            gridLine.append(int(number))
        grid.append(gridLine)

# print(grid)

visible = 0
visibleTrees=[[False for i in range(len(grid[0]))] for i in range(len(grid))]

for i in range(len(grid)):
    maxHeightFromLeft = -1
    maxHeightFromRight = -1
    for j,tree in enumerate(grid[i]):
        if tree > maxHeightFromLeft:
            if not visibleTrees[i][j]:
                visible += 1
                visibleTrees[i][j] = True
            maxHeightFromLeft = tree
    print("new right")
    for j in range(len(grid[i])-1,-1,-1):
        tree = grid[i][j]
        if tree > maxHeightFromRight:
            if not visibleTrees[i][j]:
                visible += 1
                visibleTrees[i][j] = True
            maxHeightFromRight = tree

for i in range(len(grid[0])):
    maxHeightFromTop = -1
    maxHeightFromBottom = -1
    for j in range(len(grid)):
        if grid[j][i] > maxHeightFromTop:
            if not visibleTrees[j][i]:
                visible += 1
                visibleTrees[j][i] = True
            maxHeightFromTop = grid[j][i]
    for j in range(len(grid)-1,-1,-1):
        if grid[j][i] > maxHeightFromBottom:
            if not visibleTrees[j][i]:
                visible += 1
                visibleTrees[j][i] = True
            maxHeightFromBottom = grid[j][i]

scenicScore = [[1 for i in range(len(grid[0]))] for i in range(len(grid))]
maxScenicScore=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        colView = j
        rowView = i
        while(colView+1 < len(grid[0])):
            colView += 1
            if grid[i][j]<=grid[i][colView]:
                break
        scenicScore[i][j] *= colView-j
        colView = j
        while(colView-1 >= 0):
            colView -= 1
            if grid[i][j]<=grid[i][colView]:
                break
        scenicScore[i][j] *= j-colView

        while(rowView+1 < len(grid)):
            rowView += 1
            if grid[i][j]<=grid[rowView][j]:
                break
        scenicScore[i][j] *= rowView-i
        rowView = i
        while(rowView-1 >= 0):
            rowView -= 1
            if grid[i][j]<=grid[rowView][j]:
                break
        scenicScore[i][j] *= i-rowView
        if scenicScore[i][j]>maxScenicScore:
            maxScenicScore = scenicScore[i][j]
print(maxScenicScore)
