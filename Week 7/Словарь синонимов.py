N = int(input())
i = 1
dictSyn = {}
while i <= N:
    lineSplit = input().split()
    dictSyn[lineSplit[0]] = lineSplit[1]
    i += 1
#print(dictSyn)
word = input()
for i in dictSyn:
    if word == i:
        print(dictSyn[i])
    else:
        if dictSyn[i] == word:
            print(i)

# OK
