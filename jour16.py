import re

adjacentDict = {}
targets = []
globalMaxFinalPressure = 0

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
maxPressureThatCouldStillBeAdded = [0 for i in range(31)]
for i in range(1,31):
    stepsremaining = i
    res = 0
    targetsCopy = targets[::]
    while stepsremaining > 0 and len(targetsCopy) > 0:
        res += adjacentDict[targetsCopy.pop()]["flow"] * stepsremaining
        stepsremaining -= 2
    maxPressureThatCouldStillBeAdded[i] = res

print(maxPressureThatCouldStillBeAdded)

def moveOneNode(timeRemaining, currentNode, adjacentDict, nodesOpen, currentPressureReleasedAt30Min):
    # print(timeRemaining)
    global globalMaxFinalPressure
    if timeRemaining == 0 or timeRemaining == 1:
        return currentPressureReleasedAt30Min
    if currentPressureReleasedAt30Min + maxPressureThatCouldStillBeAdded[timeRemaining] < globalMaxFinalPressure:
        return currentPressureReleasedAt30Min
    maxFinalPressure = currentPressureReleasedAt30Min
    for next in adjacentDict[currentNode]["next"]:
        if next not in nodesOpen:
            testOpenNext = moveOneNode(timeRemaining-2,
                next,
                adjacentDict,
                nodesOpen+[next], 
                currentPressureReleasedAt30Min+(timeRemaining-2)*adjacentDict[next]["flow"]
            )
            if testOpenNext > maxFinalPressure:
                maxFinalPressure = testOpenNext
        testOpenNext = moveOneNode(timeRemaining-1,
            next,
            adjacentDict,
            nodesOpen, 
            currentPressureReleasedAt30Min
        )
        if testOpenNext > maxFinalPressure:
            maxFinalPressure = testOpenNext
    if globalMaxFinalPressure < maxFinalPressure:
        globalMaxFinalPressure = maxFinalPressure
        print(globalMaxFinalPressure)
    return maxFinalPressure

print(moveOneNode(30,"AA",adjacentDict,[],0))
