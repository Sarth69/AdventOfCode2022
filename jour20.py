inputData = []
mixedData = []

decryptionKey = 811589153
# decryptionKey = 2

with open("jour20Input.txt") as lines:
# with open("testJour20.txt") as lines:
    for line in lines:
        inputData.append(int(line))

for i in range(len(inputData)):
    inputData[i] = (inputData[i]*decryptionKey,i)
mixedData = inputData[::]
dataLen = len(inputData)

print(inputData)

for k in range(10):
    for i in range(len(inputData)):
        currentIndex = mixedData.index(inputData[i])
        if mixedData[currentIndex][1] != i:
            print("error")
            break
        if inputData[i][0] == 0:
            continue
        mixedData.pop(currentIndex)
        newIndex = (currentIndex+inputData[i][0]%(dataLen-1))
        # print(newIndex)
        if newIndex < 0:
            newIndex = (newIndex%dataLen)-1
        elif newIndex >= dataLen:
            newIndex = (newIndex%dataLen)+1
        elif newIndex == 0:
            newIndex = dataLen-1
        # print(mixedData[:newIndex], [inputData[i]], mixedData[newIndex:])
        mixedData = mixedData[:newIndex]+ [inputData[i]] + mixedData[newIndex:]
    # print(k,    mixedData)

zeroIndex = 0
for i in range(dataLen):
    if mixedData[i][0] == 0:
        zeroIndex = i

print(mixedData[(zeroIndex+1000)%dataLen][0]+mixedData[(zeroIndex+2000)%dataLen][0]+mixedData[(zeroIndex+3000)%dataLen][0])