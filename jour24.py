blizard = []
gridHeight = 0
gridWidth = 0

with open("jour24Input.txt") as lines:
    for k,line in enumerate(lines):
        line = line.strip()
        gridHeight += 1
        gridWidth = len(line)-2
        for i in range(1,len(line)):
            if line[i] != "." and line[i] != "#":
                blizard.append((k-1,i-1,line[i]))

gridHeight -= 2

print(blizard,gridHeight,gridWidth)

toVisit = []
toVisitNext = [(-1,0,643)]
# toVisitNext = [(-1,0,41)]

def canYouVisit(blizard, whereToVisit, time):
    canVisit = True
    for bliz in blizard:
        match bliz[2]:
            case "^":
                if whereToVisit[0] == (bliz[0]-time)%gridHeight and whereToVisit[1] == bliz[1]:
                    canVisit = False
            case "v":
                if whereToVisit[0] == (bliz[0]+time)%gridHeight and whereToVisit[1] == bliz[1]:
                    canVisit = False
            case "<":
                if whereToVisit[1] == (bliz[1]-time)%gridWidth and whereToVisit[0] == bliz[0]:
                    canVisit = False
            case ">":
                if whereToVisit[1] == (bliz[1]+time)%gridWidth and whereToVisit[0] == bliz[0]:
                    canVisit = False
    return canVisit

finished = False
# while not finished:
#     # input(toVisitNext)
#     toVisit = toVisitNext[::]
#     print(toVisitNext[0][2])
#     toVisitNext = []
#     while len(toVisit) > 0:
#         visiting = toVisit.pop()
#         # print(visiting)
#         if visiting[0] == 0 and visiting[1] == 0:
#             print(visiting[2]+1)
#             finished = True
#             break
#         if (visiting[0],visiting[1]) == (gridHeight-1, gridWidth-1):
#             toVisitNext.append((gridHeight, gridWidth-1, visiting[2]+1))
#         if visiting[0] > 0:
#             if canYouVisit(blizard, (visiting[0]-1,visiting[1]), visiting[2]+1):
#                 if (visiting[0]-1,visiting[1],visiting[2]+1) not in toVisitNext:
#                     toVisitNext.append((visiting[0]-1,visiting[1],visiting[2]+1))
#         if (visiting[0],visiting[1]) == (gridHeight, gridWidth-1):
#             toVisitNext.append((gridHeight, gridWidth-1, visiting[2]+1))
#             continue
#         if visiting[1] > 0:
#             if canYouVisit(blizard, (visiting[0],visiting[1]-1), visiting[2]+1):
#                 if (visiting[0],visiting[1]-1,visiting[2]+1) not in toVisitNext:
#                     toVisitNext.append((visiting[0],visiting[1]-1,visiting[2]+1))
#         if visiting[1] < gridWidth-1:
#             if canYouVisit(blizard, (visiting[0],visiting[1]+1), visiting[2]+1):
#                 if (visiting[0],visiting[1]+1,visiting[2]+1) not in toVisitNext:
#                     toVisitNext.append((visiting[0],visiting[1]+1,visiting[2]+1))
#         if visiting[0] < gridHeight-1:
#             if canYouVisit(blizard, (visiting[0]+1,visiting[1]), visiting[2]+1):
#                 if (visiting[0]+1,visiting[1],visiting[2]+1) not in toVisitNext:
#                     toVisitNext.append((visiting[0]+1,visiting[1],visiting[2]+1))
#         if canYouVisit(blizard,(visiting[0],visiting[1]), visiting[2]+1):
#             if (visiting[0],visiting[1],visiting[2]+1) not in toVisitNext:
#                 toVisitNext.append((visiting[0],visiting[1],visiting[2]+1))

# finished = False
while not finished:
    # input(toVisitNext)
    toVisit = toVisitNext[::]
    print(toVisitNext[0][2])
    toVisitNext = []
    while len(toVisit) > 0:
        visiting = toVisit.pop()
        # print(visiting)
        if visiting[0] == gridHeight-1 and visiting[1] == gridWidth-1:
            print(visiting[2]+1)
            finished = True
            break
        if (visiting[0],visiting[1]) == (0, 0):
            toVisitNext.append((-1, 0, visiting[2]+1))
        if visiting[0] < gridHeight-1:
            if canYouVisit(blizard, (visiting[0]+1,visiting[1]), visiting[2]+1):
                if (visiting[0]+1,visiting[1],visiting[2]+1) not in toVisitNext:
                    toVisitNext.append((visiting[0]+1,visiting[1],visiting[2]+1))
        if (visiting[0],visiting[1]) == (-1, 0):
            toVisitNext.append((-1, 0, visiting[2]+1))
            continue
        if visiting[0] > 0:
            if canYouVisit(blizard, (visiting[0]-1,visiting[1]), visiting[2]+1):
                if (visiting[0]-1,visiting[1],visiting[2]+1) not in toVisitNext:
                    toVisitNext.append((visiting[0]-1,visiting[1],visiting[2]+1))
        if visiting[1] > 0:
            if canYouVisit(blizard, (visiting[0],visiting[1]-1), visiting[2]+1):
                if (visiting[0],visiting[1]-1,visiting[2]+1) not in toVisitNext:
                    toVisitNext.append((visiting[0],visiting[1]-1,visiting[2]+1))
        if visiting[1] < gridWidth-1:
            if canYouVisit(blizard, (visiting[0],visiting[1]+1), visiting[2]+1):
                if (visiting[0],visiting[1]+1,visiting[2]+1) not in toVisitNext:
                    toVisitNext.append((visiting[0],visiting[1]+1,visiting[2]+1))
        if canYouVisit(blizard,(visiting[0],visiting[1]), visiting[2]+1):
            if (visiting[0],visiting[1],visiting[2]+1) not in toVisitNext:
                toVisitNext.append((visiting[0],visiting[1],visiting[2]+1))
