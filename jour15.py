import re

# lineToConsider = 2000000
maxSize = 4000000
# maxSize = 20

for lineToConsider in range(0,maxSize):
    print(lineToConsider)
    with open("jour15Input.txt") as lines:
        positionsConsidered = {}
        res = 0
        for i,line in enumerate(lines):
            line = line.strip()
            match = re.match("Sensor at x=([\-0-9]*), y=([\-0-9]*): closest beacon is at x=([\-0-9]*), y=([\-0-9]*)", line)
            sx,sy,bx,by = int(match[1]), int(match[2]), int(match[3]), int(match[4])
            distToLine2M = abs(sy-lineToConsider)
            distToB = abs(sy-by)+abs(sx-bx)
            if distToB > distToLine2M:
                for x in range(max(0,sx-(distToB-distToLine2M)), min(maxSize+1,sx+(distToB-distToLine2M)+1)):
                    # print(x)
                    # if (x != bx or lineToConsider != by) and x not in positionsConsidered.keys():
                    #     positionsConsidered[x] = True
                    #     res += 1
                    # if x == bx:
                    #     positionsConsidered[x] = True
                    #     res += 1
                    if x not in positionsConsidered.keys():
                        positionsConsidered[x] = True
                        res += 1

            # for i in range(-distToB, distToB+1):
            #     for j in range(-distToB+abs(i),distToB-abs(i)+1):
            #         positionsConsidered[sx+i][sy+j] = True
        # print(lineToConsider, res)
        if res != maxSize+1:
            for i in range(maxSize + 1):
                if i not in positionsConsidered.keys():
                    print("here",i,lineToConsider, i*4000000+lineToConsider)
                    break
            



# print(res)