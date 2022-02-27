inFile = open('input.txt', 'r')
# outFile = open('output.txt', 'w')

listNumbers = []
# x = inFile.readline()

for line in inFile:
    lineSplit = line.replace('+7', '8').replace('-', '')\
        .replace('(', '').replace(')', '').split()
    if len(lineSplit[0]) == 7:
        lineSplit[0] = '8495' + lineSplit[0]
    listNumbers.append(lineSplit)
    # print(lineSplit)
# print(listNumbers)
for i in range(1, len(listNumbers)):
    if listNumbers[0] == listNumbers[i]:
        print('YES')
    else:
        print('NO')

# OK
