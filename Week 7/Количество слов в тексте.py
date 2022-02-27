inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w')

L = []
lineSplitSumm = set(L)
for line in inFile:
    lineSplit = set(line.split())
    lineSplitSumm = lineSplitSumm | lineSplit
    # print(*lineSplitSumm)
print(len(lineSplitSumm), file=outFile)

inFile.close()
outFile.close()

# OK