import re

res = 0
global globalMaxNumberOfGeodes
globalMaxNumberOfGeodes = 0

def compute(timeRemaining, inputData, numberOfRobots, currentRessources):
    if timeRemaining == 0:
        return currentRessources["geode"]
    global globalMaxNumberOfGeodes
    maxNumberOfGeodes = currentRessources["geode"]

    if timeRemaining*numberOfRobots["geode"] + maxNumberOfGeodes + timeRemaining*(timeRemaining-1)/2 < globalMaxNumberOfGeodes:
        return maxNumberOfGeodes

    #OPTION 1 : craft ore robot next
    timeToWait = max(1,((inputData["oreRobotOreCost"]-currentRessources["ore"]-1)//numberOfRobots["ore"])+2)
    if timeToWait < timeRemaining:
        numberOfRobotsNext = numberOfRobots.copy()
        currentRessourcesNext = currentRessources.copy()
        numberOfRobotsNext["ore"] += 1
        currentRessourcesNext["ore"] = currentRessources["ore"]-inputData["oreRobotOreCost"] + (numberOfRobotsNext["ore"]-1)*timeToWait
        currentRessourcesNext["clay"] += timeToWait*numberOfRobotsNext["clay"]
        currentRessourcesNext["obsidian"] += timeToWait * numberOfRobotsNext["obsidian"]
        currentRessourcesNext["geode"] += timeToWait * numberOfRobotsNext["geode"]
        numberOfGeodesNext = compute(timeRemaining-timeToWait,inputData,numberOfRobotsNext,currentRessourcesNext)
        if numberOfGeodesNext > maxNumberOfGeodes:
            maxNumberOfGeodes = numberOfGeodesNext
        if maxNumberOfGeodes > globalMaxNumberOfGeodes:
            # print("1",timeRemaining,currentRessourcesNext,numberOfRobotsNext,inputData)
            globalMaxNumberOfGeodes = maxNumberOfGeodes

    #OPTION 2 : craft clay robot next
    timeToWait = max(1,((inputData["clayRobotOreCost"]-currentRessources["ore"]-1)//numberOfRobots["ore"])+2)
    if timeToWait < timeRemaining:
        numberOfRobotsNext = numberOfRobots.copy()
        currentRessourcesNext = currentRessources.copy()
        numberOfRobotsNext["clay"] += 1
        currentRessourcesNext["ore"] = currentRessources["ore"]-inputData["clayRobotOreCost"] + numberOfRobotsNext["ore"]*timeToWait
        currentRessourcesNext["clay"] += timeToWait*(numberOfRobotsNext["clay"]-1)
        currentRessourcesNext["obsidian"] += timeToWait * numberOfRobotsNext["obsidian"]
        currentRessourcesNext["geode"] += timeToWait * numberOfRobotsNext["geode"]
        numberOfGeodesNext = compute(timeRemaining-timeToWait,inputData,numberOfRobotsNext,currentRessourcesNext)
        if numberOfGeodesNext > maxNumberOfGeodes:
            maxNumberOfGeodes = numberOfGeodesNext
        if maxNumberOfGeodes > globalMaxNumberOfGeodes:
            # print("2",timeRemaining,currentRessourcesNext,numberOfRobotsNext,inputData)
            globalMaxNumberOfGeodes = maxNumberOfGeodes

    #OPTION 3 : craft obsi robot next
    if numberOfRobots["clay"] > 0:
        timeToWait = max(max(1,((inputData["obsidianRobotOreCost"]-currentRessources["ore"]-1)//numberOfRobots["ore"])+2),((inputData["obsidianRobotClayCost"]-currentRessources["clay"]-1)//numberOfRobots["clay"])+2)
        if timeToWait < timeRemaining:
            numberOfRobotsNext = numberOfRobots.copy()
            currentRessourcesNext = currentRessources.copy()
            numberOfRobotsNext["obsidian"] += 1
            currentRessourcesNext["ore"] = currentRessources["ore"]-inputData["obsidianRobotOreCost"] + numberOfRobotsNext["ore"]*timeToWait
            currentRessourcesNext["clay"] = currentRessources["clay"]-inputData["obsidianRobotClayCost"] + numberOfRobotsNext["clay"]*timeToWait
            currentRessourcesNext["obsidian"] += timeToWait*(numberOfRobotsNext["obsidian"]-1)
            currentRessourcesNext["geode"] += timeToWait * numberOfRobotsNext["geode"]
            numberOfGeodesNext = compute(timeRemaining-timeToWait,inputData,numberOfRobotsNext,currentRessourcesNext)
            if numberOfGeodesNext > maxNumberOfGeodes:
                maxNumberOfGeodes = numberOfGeodesNext
            if maxNumberOfGeodes > globalMaxNumberOfGeodes:
                # print('z',timeRemaining,currentRessourcesNext,numberOfRobotsNext,inputData)
                globalMaxNumberOfGeodes = maxNumberOfGeodes

    #OPTION 4 : craft geode robot next
    if numberOfRobots["obsidian"] > 0:
        timeToWait = max(max(1,((inputData["geodeRobotOreCost"]-currentRessources["ore"]-1)//numberOfRobots["ore"])+2),((inputData["geodeRobotObsidianCost"]-currentRessources["obsidian"]-1)//numberOfRobots["obsidian"])+2)
        if timeToWait < timeRemaining:
            numberOfRobotsNext = numberOfRobots.copy()
            currentRessourcesNext = currentRessources.copy()
            numberOfRobotsNext["geode"] += 1
            currentRessourcesNext["ore"] = currentRessources["ore"]-inputData["geodeRobotOreCost"] + numberOfRobotsNext["ore"]*timeToWait
            currentRessourcesNext["clay"] += numberOfRobotsNext["clay"] * timeToWait
            currentRessourcesNext["obsidian"] = currentRessources["obsidian"]-inputData["geodeRobotObsidianCost"] + numberOfRobotsNext["obsidian"]*timeToWait
            currentRessourcesNext["geode"] += timeToWait*(numberOfRobotsNext["geode"]-1)
            numberOfGeodesNext = compute(timeRemaining-timeToWait,inputData,numberOfRobotsNext,currentRessourcesNext)
            if numberOfGeodesNext > maxNumberOfGeodes:
                maxNumberOfGeodes = numberOfGeodesNext
            if maxNumberOfGeodes > globalMaxNumberOfGeodes:
                # print('4',timeRemaining,currentRessourcesNext,numberOfRobotsNext,inputData)
                globalMaxNumberOfGeodes = maxNumberOfGeodes

    return maxNumberOfGeodes

with open("jour19Input.txt") as lines:
    for line in lines:
        line = line.strip()
        lineParsed = re.match("Blueprint ([0-9]*): Each ore robot costs ([0-9]*) ore. Each clay robot costs ([0-9]*) ore. Each obsidian robot costs ([0-9]*) ore and ([0-9]*) clay. Each geode robot costs ([0-9]*) ore and ([0-9]*) obsidian.", line)
        blueprintId = int(lineParsed[1])
        oreRobotOreCost = int(lineParsed[2])
        clayRobotOreCost = int(lineParsed[3])
        obsidianRobotOreCost = int(lineParsed[4])
        obsidianRobotClayCost = int(lineParsed[5])
        geodeRobotOreCost = int(lineParsed[6])
        geodeRobotObsidianCost = int(lineParsed[7])

        inputData = {
            "blueprintId":blueprintId,
            "oreRobotOreCost":oreRobotOreCost,
            "clayRobotOreCost":clayRobotOreCost,
            "obsidianRobotClayCost":obsidianRobotClayCost,
            "obsidianRobotOreCost":obsidianRobotOreCost,
            "geodeRobotObsidianCost":geodeRobotObsidianCost,
            "geodeRobotOreCost":geodeRobotOreCost
        }

        numberOfRobots = {
            "ore":1,
            "clay":0,
            "obsidian":0,
            "geode":0
        }

        currentRessources = {
            "ore": 0,
            "clay": 0,
            "obsidian": 0,
            "geode": 0
        }
        globalMaxNumberOfGeodes = 0
        res += blueprintId * compute(timeRemaining=25, inputData=inputData, numberOfRobots=numberOfRobots, currentRessources=currentRessources)
        print(blueprintId,res)

print(res)