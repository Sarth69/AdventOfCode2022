import re

class Monkey:
    currentItems = []
    operation = ""
    nextIfTrue = 0
    nextIfFalse = 0
    id = 0
    inspected = 0
    test = 0
    def __init__(self, startingItems, operation, id, nextIfTrue, nextIfFalse, test) -> None:
        self.currentItems = startingItems
        self.operation = operation
        self.id = id
        self.nextIfFalse = nextIfFalse
        self.nextIfTrue = nextIfTrue
        self.test = test

currentMonkeyId = 0
startList = []
operation = ""
test = 0
nextIfFalse = 0
nextIfTrue = 0
monkeys=[]
modulo = 1

with open("jour11Input.txt") as lines:
    for line in lines:
        line = line.strip()
        match = re.match("Monkey ([0-9]):", line)
        if match:
            currentMonkeyId = int(match[1])
            continue
        match = re.match("Starting items:", line)
        if match:
            startList = line[16:].split(",")
            for i in range(len(startList)):
                startList[i] = int(startList[i])
            continue
        match = re.match("Operation:", line)
        if match:
            operation = line[11:]
            # print(operation)
            # loc = {}
            # old=1
            # new = 0
            # exec(operation, globals(), loc)
            # print(loc["new"])
            continue
        match = re.match("Test: divisible by ([0-9]*)", line)
        if match:
            test = int(match[1])
            modulo *= test
            continue
        match = re.match("If true: throw to monkey ([0-9])", line)
        if match:
            nextIfTrue = int(match[1])
            continue
        match = re.match("If false: throw to monkey ([0-9])", line)
        if match:
            nextIfFalse = int(match[1])
            continue
        monkeys.append(Monkey(startList, operation, currentMonkeyId, nextIfTrue, nextIfFalse, test))

for round in range(10000):
    print("Round :",round)
    # for monkey in monkeys:
    #     print(monkey.id, monkey.currentItems)
    for monkey in monkeys:
        for item in monkey.currentItems:
            monkey.inspected += 1
            old = item
            new = 0
            loc={}
            exec(monkey.operation, globals(), loc)
            new = loc["new"]
            # new = new // 3
            new = new % modulo
            if (new % monkey.test == 0):
                monkeys[monkey.nextIfTrue].currentItems.append(new)
            else:
                monkeys[monkey.nextIfFalse].currentItems.append(new)
        monkey.currentItems = []

for monkey in monkeys:
    print(monkey.inspected)