import re

stacks=[[] for i in range(9)]
print(stacks)
init = True

with open("jour5Input.txt") as file:
    for line in file:
        if (init) :
            if line[1]=="1":
                init = False
                print(stacks)    
                continue
            for i in range(len(line)):
                if i%4==1:
                    if line[i]!=" ":
                        stacks[i//4]= [line[i]] + stacks[i//4] 
        else:
            matchs = re.match("move ([0-9]*) from ([0-9]*) to ([0-9]*)", line)
            if matchs:
                movingCrates=[]
                for i in range(int(matchs[1])):
                    toMove = stacks[int(matchs[2])-1].pop()
                    movingCrates.append(toMove)
                stacks[int(matchs[3])-1] += movingCrates[::-1]
                print(line, stacks)
    
print(stacks)
res = ""
for i in range(9):
    res += stacks[i][-1]

print(res)