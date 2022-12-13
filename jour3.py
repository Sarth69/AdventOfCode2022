score=0
line1=""
line2=""
group=0

print(ord("a"), ord("A"), "a"<"A")
with open("jour3Input.txt") as file:
    for line in file:
        if group%3==0:
            line1=line
            group+=1
            continue
        if group%3==1:
            line2=line
            group+=1
            continue
        group+=1
        for letter in line:
            if letter in line1 and letter in line2 and ord(letter)>=65:
                print(line, line1, line2, letter)
                if letter < "a":
                    score += ord(letter)-65+27
                else:
                    score += ord(letter)-96
                break
print(score)
