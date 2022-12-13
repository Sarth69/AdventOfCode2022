score=0

with open("jour2Input.txt") as file:
    for line in file:
        match line[0]:
            case "A":
                match line[2]:
                    case "X":
                        score += 3
                    case "Y":
                        score += 1+3
                    case "Z":
                        score += 2+6
            case "B":
                match line[2]:
                    case "X":
                        score += 1
                    case "Y":
                        score += 2+3
                    case "Z":
                        score += 3+6
            case "C":
                match line[2]:
                    case "X":
                        score += 2
                    case "Y":
                        score += 3+3
                    case "Z":
                        score += 1+6
print(score)