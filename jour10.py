cycles = 0
register = 1
res = 0
cyclesToConsider = [20,60,100,140,180,220]
lineToPrint=""

with open("jour10Input.txt") as lines:
    for line in lines:
        line = line.strip()
        if line[0]=="n":
            cycles += 1
            if cycles in cyclesToConsider:
                res += register*cycles
            # print("a", register, cycles%40)
            if(abs(register-((cycles-1)%40))<=1):
                lineToPrint += "#"
            else:
                lineToPrint += "."
            if len(lineToPrint) % 40 == 0:
                print(lineToPrint)
                lineToPrint = ""
        else:
            if cycles+1 in cyclesToConsider:
                res += register*(cycles+1)
            cycles += 2
            # print("b", register, cycles%40)
            if(abs(register-((cycles-1)%40)+1)<=1):
                lineToPrint += "#"
            else:
                lineToPrint += "."
            if len(lineToPrint) % 40 == 0:
                print(lineToPrint)
                lineToPrint = ""
            if(abs(register-((cycles-1)%40))<=1):
                lineToPrint += "#"
            else:
                lineToPrint += "."
            if len(lineToPrint) % 40 == 0:
                print(lineToPrint)
                lineToPrint = ""
            # print(lineToPrint)
            if cycles in cyclesToConsider:
                res += register*cycles
            register += int(line[5:])

print(res)