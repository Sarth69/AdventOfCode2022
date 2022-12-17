import re

adjacentDict = {}
targets = []
globalMaxFinalPressure = 3000

with open("jour16Input.txt") as lines:
    for line in lines:
        line = line.strip()
        match = re.match("Valve ([A-Z]*) has flow rate=([0-9]*); tunnel[s]* lead[s]* to valve[s]* ([A-Z, ]*)", line)
        valve, flow, next = match[1], match[2], match[3].split(",")
        for i in range(len(next)):
            next[i] = next[i].strip()
        adjacentDict[valve] = {
            "next": next,
            "flow": int(flow)
        }
        if int(flow) > 0:
            targets.append(valve)

print(len(targets))
targets.sort()
# maxPressureThatCouldStillBeAdded = [0 for i in range(31)]
# for i in range(1,31):
#     stepsremaining = i
#     res = 0
#     targetsCopy = targets[::]
#     while stepsremaining > 0 and len(targetsCopy) > 0:
#         res += adjacentDict[targetsCopy.pop()]["flow"] * stepsremaining
#         res += adjacentDict[targetsCopy.pop()]["flow"] * stepsremaining
#         stepsremaining -= 2
#     maxPressureThatCouldStillBeAdded[i] = res

# print(maxPressureThatCouldStillBeAdded)

def moveOneNodePart2(timeRemaining, currentNode, currentElephantNode, adjacentDict, nodesOpen, currentPressureReleasedAt30Min):
    global globalMaxFinalPressure
    maxFinalPressure = currentPressureReleasedAt30Min

    maxPressureThatCouldStillBeAdded = 0
    stepsremaining = timeRemaining
    targetsCopy = targets[::]
    while stepsremaining > 0 and len(targetsCopy) > 0:
        for i in range(2):
            if len(targetsCopy) == 0:
                break
            triedOne = targetsCopy.pop()
            while triedOne in nodesOpen:
                if len(targetsCopy) == 0:
                    break
                triedOne = targetsCopy.pop()
            if triedOne in nodesOpen:
                break
            maxPressureThatCouldStillBeAdded += adjacentDict[triedOne]["flow"] * stepsremaining
        stepsremaining -= 2
    # print(maxPressureThatCouldStillBeAdded + currentPressureReleasedAt30Min)

    if timeRemaining <= 1:
        return currentPressureReleasedAt30Min
    if currentPressureReleasedAt30Min + maxPressureThatCouldStillBeAdded < globalMaxFinalPressure:
        return currentPressureReleasedAt30Min
    # print(maxPressureThatCouldStillBeAdded + currentPressureReleasedAt30Min)
    #CASE 1 : WE BOTH MOVE
    for next in adjacentDict[currentNode]["next"]:
        for elephantNext in adjacentDict[currentElephantNode]["next"]:
            testOpenNext = moveOneNodePart2(timeRemaining-1,
                next,
                elephantNext,
                adjacentDict,
                nodesOpen, 
                currentPressureReleasedAt30Min
            )
            if testOpenNext > maxFinalPressure:
                maxFinalPressure = testOpenNext
        #CASE 2 : I OPEN, EL MOVES
        if currentNode not in nodesOpen:
            testOpenNext = moveOneNodePart2(timeRemaining-1,
                currentNode,
                elephantNext,
                adjacentDict,
                nodesOpen+[currentNode], 
                currentPressureReleasedAt30Min+(timeRemaining-1)*adjacentDict[currentNode]["flow"]
            )
            if testOpenNext > maxFinalPressure:
                maxFinalPressure = testOpenNext
    #CASE 3 : I move, EL OPENS
    if currentElephantNode not in nodesOpen:
        for next in adjacentDict[currentNode]["next"]:
            testOpenNext = moveOneNodePart2(timeRemaining-1,
                next,
                currentElephantNode,
                adjacentDict,
                nodesOpen+[currentElephantNode], 
                currentPressureReleasedAt30Min+(timeRemaining-1)*adjacentDict[currentElephantNode]["flow"]
            )
            if testOpenNext > maxFinalPressure:
                maxFinalPressure = testOpenNext

    #CASE 4 : WE BOTH OPEN
    if currentElephantNode not in nodesOpen and currentNode not in nodesOpen and currentElephantNode != currentNode:
        testOpenNext = moveOneNodePart2(timeRemaining-1,
            currentNode,
            currentElephantNode,
            adjacentDict,
            nodesOpen+[currentElephantNode, currentNode], 
            currentPressureReleasedAt30Min+(timeRemaining-1)*adjacentDict[currentElephantNode]["flow"]+(timeRemaining-1)*adjacentDict[currentNode]["flow"]
        )
        if testOpenNext > maxFinalPressure:
            maxFinalPressure = testOpenNext
    if globalMaxFinalPressure < maxFinalPressure:
        globalMaxFinalPressure = maxFinalPressure
        print(globalMaxFinalPressure)
    return maxFinalPressure

print("res",moveOneNodePart2(26,"AA","AA",adjacentDict,[],0))
