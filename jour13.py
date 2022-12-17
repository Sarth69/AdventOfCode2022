res = 0
index = 1
pairIndex = 0
first = []
second = []
allPackets = []

import json

def compare(first, second):
    #Returns 1 if right order, 0 if wrong, 2 if undecided
    if isinstance(first, int) and isinstance(second, int):
        if first < second:
            return 1
        if first > second:
            return 0
        return 2
    if isinstance(first, list) and isinstance(second, list):
        if len(first) == 0 and len(second) == 0:
            return 2
        if len(first) == 0:
            return 1
        if len(second) == 0:
            return 0
        value = compare(first[0], second[0])
        if value == 2:
            return compare(first[1:], second[1:])
        else:
            return value
    if isinstance(first, int):
        return compare([first], second)
    return compare(first, [second])

with open("jour13Input.txt") as lines:
    for line in lines:
        line = line.strip()
        print("line:",pairIndex,line)
        if pairIndex == 0:
            first = json.loads(line)
            allPackets.append(first)
        elif pairIndex == 1:
            second = json.loads(line)
            allPackets.append(second)
        else:
            #compute
            if compare(first, second):
                res += index
            pairIndex = -1
            index += 1
        pairIndex += 1

rank2 = 1
for packet in allPackets+[[[6]]]:
    if compare(packet, [[2]]):
        rank2 += 1
rank6 = 1
for packet in allPackets+[[[2]]]:
    if compare(packet, [[6]]):
        rank6 += 1
print(rank2*rank6)
