total = 0

with open("jour25Input.txt") as lines:
    for line in lines:
        line = line.strip()
        maxPower = len(line)-1
        for i in range(len(line)):
            match line[i]:
                case "2":
                    total += 5**(maxPower-i) * 2
                case "1":
                    total += 5**(maxPower-i) * 1
                case "-":
                    total += 5**(maxPower-i) * -1
                case "=":
                    total += 5**(maxPower-i) * -2

def dec2SNAFU(number):
    res = ""
    currentPower = 0
    minuses = 0
    minNumberThisPower = -2
    while number >= minNumberThisPower:
        div = (number+minuses)//(5**currentPower)
        mod = div%5
        match mod:
            case 3:
                minuses += (5**currentPower) * 2
                res = "=" + res
            case 4:
                minuses +=  (5**currentPower)
                res = "-" + res
            case 2:
                res = "2" + res
            case 1:
                res = "1" + res
            case 0:
                res = "0" + res
        currentPower += 1
        minNumberThisPower += 5**currentPower
        if currentPower != 1:
            minNumberThisPower += - 3 * (5**(currentPower-1))
        print(minNumberThisPower, currentPower)
    return res

print(dec2SNAFU(total))