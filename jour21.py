import re

global valuesDict
valuesDict = {}

with open("jour21Input.txt") as lines:
    for line in lines:
        line = line.strip()
        values = re.match("([a-z]*): ([a-z]*) ([\+\-\*\/]) ([a-z]*)", line)
        if values:
            if values[1] == "root":
                valuesDict[values[1]] = [values[2],values[4],"="]
            else:
                valuesDict[values[1]] = [values[2],values[4],values[3]]
        else:
            valuesDict[line[:4]] = int(line[6:])

originalValues = valuesDict.copy()

def getValue(monkey):
    global valuesDict
    value = valuesDict[monkey]
    if isinstance(value,int):
        return value
    else:
        left = getValue(value[0])
        right = getValue(value[1])
        match value[2]:
            case "+":
                newValue = left + right
                valuesDict[monkey] = newValue
                return newValue
            case "-":
                newValue = left - right
                valuesDict[monkey] = newValue
                return newValue
            case "*":
                newValue = left * right
                valuesDict[monkey] = newValue
                return newValue
            case "/":
                newValue = left // right
                # if left%right != 0:
                #     print("div error")
                valuesDict[monkey] = newValue
                return newValue
            case "=":
                print(left, right, left>right)
                return left == right
            case _:
                print("error !")

humanValue = 3451534022348
valuesDict["humn"] = humanValue
while not getValue("root"):
    valuesDict = originalValues.copy()
    humanValue += 1
    valuesDict["humn"] = humanValue
    print(humanValue)
    break
print(humanValue)