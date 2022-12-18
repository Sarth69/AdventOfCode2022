grid = [[["air" for k in range(20)]for i in range(20)]for j in range(20)]

with open("jour18Input.txt") as lines:
    for line in lines:
        line = line.strip()
        line = line.split(",")
        grid[int(line[0])][int(line[1])][int(line[2])] = "lava"

res = 0
for h in range(20*20*20):
    print(h)
    for i in range(20):
        for j in range(20):
            for k in range(20):
                if grid[i][j][k] == "air":
                    if i != 0:
                        if grid[i-1][j][k] == "water":
                            grid[i][j][k] = "water"
                    else:
                        grid[i][j][k] = "water"
                    if i != 19:
                        if "water" == grid[i+1][j][k]:
                            grid[i][j][k] = "water"
                    else:
                        grid[i][j][k] = "water"
                    if j != 0:
                        if "water" == grid[i][j-1][k]:
                            grid[i][j][k] = "water"
                    else:
                        grid[i][j][k] = "water"
                    if j != 19:
                        if "water" == grid[i][j+1][k]:
                            grid[i][j][k] = "water"
                    else:
                        grid[i][j][k] = "water"
                    if k != 0:
                        if "water" == grid[i][j][k-1]:
                            grid[i][j][k] = "water"
                    else:
                        grid[i][j][k] = "water"
                    if k != 19:
                        if "water" == grid[i][j][k+1]:
                            grid[i][j][k] = "water"
                    else:
                        grid[i][j][k] = "water"

for i in range(20):
    for j in range(20):
        for k in range(20):
            if grid[i][j][k] == "lava":
                if i != 0:
                    if "water" == grid[i-1][j][k]:
                        res += 1
                else:
                    res += 1
                if i != 19:
                    if "water" ==  grid[i+1][j][k]:
                        res += 1
                else:
                    res += 1
                if j != 0:
                    if "water" ==  grid[i][j-1][k]:
                        res += 1
                else:
                    res += 1
                if j != 19:
                    if "water" ==  grid[i][j+1][k]:
                        res += 1
                else:
                    res += 1
                if k != 0:
                    if "water" ==  grid[i][j][k-1]:
                        res += 1
                else:
                    res += 1
                if k != 19:
                    if "water" == grid[i][j][k+1]:
                        res += 1
                else:
                    res += 1
            # if not grid[i][j][k]:
            #     if i != 0 and grid[i-1][j][k] and i != 19 and grid[i+1][j][k] and j != 0 and grid[i][j-1][k] and j != 19 \
            #         and grid[i][j+1][k] and k != 0 and grid[i][j][k-1] and k != 19 and grid[i][j][k+1]:
            #             res -= 6

print(res)