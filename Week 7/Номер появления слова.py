inFile = open('input.txt', 'r')

countDict = {}
listWords = []

for line in inFile:
    lineSplit = line.split()
    for word in lineSplit:
        if word not in countDict:
            countDict[word] = 1
            listWords.append(0)
        else:
            countDict[word] = countDict[word] + 1
            listWords.append(countDict[word] - 1)
print(*listWords)

# OK
