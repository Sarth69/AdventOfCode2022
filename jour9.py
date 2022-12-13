visited = [[False for i in range(1000)] for i in range(1000)]
posHead = (500,500)
posTail = [(500,500) for i in range(9)]

visited[posTail[8][0]][posTail[8][1]] = True
visitedNumber = 1

def moveTail(posHeadTotal, posTailTotal, visitedNumber):
    for i in range(9):
        posTail = posTailTotal[i]
        if i == 0:
            posHead = posHeadTotal
        else:
            posHead = posTailTotal[i-1]
        if (abs(posHead[0]-posTail[0])>1 or abs(posTail[1]-posHead[1]) > 1):
            if posHead[0] == posTail[0]:
                if posTail[1] < posHead[1]:
                    posTail = (posTail[0],posTail[1] +1)
                else:
                    posTail = (posTail[0],posTail[1] -1)
            elif posHead[1] == posTail[1]:
                if posTail[0] < posHead[0]:
                    posTail = (posTail[0] +1, posTail[1])
                else:
                    posTail = (posTail[0]-1, posTail[1])
            else:
                if posTail[1] < posHead[1]:
                    posTail = (posTail[0],posTail[1] +1)
                else:
                    posTail = (posTail[0],posTail[1]-1)
                if posTail[0] < posHead[0]:
                    posTail = (posTail[0] +1,posTail[1])
                else:
                    posTail = (posTail[0]-1,posTail[1])
        if not visited[posTail[0]][posTail[1]] and i == 8:
            visited[posTail[0]][posTail[1]] = True
            visitedNumber += 1
        posTailTotal[i] = posTail
    return posHeadTotal, posTailTotal, visitedNumber


with open("jour9Input.txt") as lines:
    for line in lines:
        line=line.strip()
        print(posHead, posTail, line[0], int(line[2:]), visitedNumber) 
        match line[0]:
            case "D":
                for i in range(int(line[2:])):
                    posHead = (posHead[0]+1, posHead[1])
                    posHead, posTail, visitedNumber = moveTail(posHead, posTail,visitedNumber)                    
            case "R":
                for i in range(int(line[2:])):
                    posHead = (posHead[0], posHead[1]+1)
                    posHead, posTail, visitedNumber = moveTail(posHead, posTail,visitedNumber)   
            case "U":
                for i in range(int(line[2:])):
                    posHead = (posHead[0]-1, posHead[1])
                    posHead, posTail, visitedNumber = moveTail(posHead, posTail,visitedNumber)   
            case "L":
                for i in range(int(line[2:])):
                    posHead = (posHead[0], posHead[1]-1)
                    posHead, posTail, visitedNumber = moveTail(posHead, posTail,visitedNumber)  
        print(posHead, posTail, line[0], line[2:], visitedNumber) 

print(visitedNumber)
