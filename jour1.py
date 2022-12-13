current = 0
max = [0,0,0]

with open("jour1Input.txt") as file:
    for line in file:
        if line != "\n":
            current += int(line);
        else:
            if current > max[0]:
                max[0] = current
                max.sort()
            current=0
print(max[0]+max[1]+max[2])