last4 = []
count=0

with open("jour6Input.txt") as file:
    for line in file:
        for i in line:
            count += 1
            last4.append(i)
            if len(last4) >= 14:
                last4.pop(0)
                if len(set(last4)) == 14:
                    break
print(count)