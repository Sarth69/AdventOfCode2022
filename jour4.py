import re

count=0

with open("jour4Input.txt") as file:
    for line in file:
        entries = re.split("[-,\n]",line)
        if (int(entries[0])>=int(entries[2]) and int(entries[0])<= int(entries[3])) \
        or (int(entries[1])>=int(entries[2]) and int(entries[1])<= int(entries[3])) \
        or (int(entries[2])>=int(entries[0]) and int(entries[2])<= int(entries[1])) \
        or (int(entries[3])>=int(entries[0]) and int(entries[3])<= int(entries[1])):
            print(line,entries)
            count+=1
print(count)
