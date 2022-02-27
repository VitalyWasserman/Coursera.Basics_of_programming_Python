inFile = open('input.txt', 'r')
dictWords = {}

for line in inFile:
    lineSplit = line.split()
    for i in lineSplit:
        if i not in dictWords:
            dictWords[i] = 1
        else:
            dictWords[i] = dictWords[i] + 1

list_dictWords = list(dictWords.items())
# print(list_dictWords)

# сортировка по второстепенному значению
temp_list_dictWords_1 = sorted(list_dictWords)

# сортировка по главному значению
temp_list_dictWords_2 = sorted(temp_list_dictWords_1,
                               key=lambda i: i[1], reverse=True)

# print(temp_list_dictWords_1)
# print(temp_list_dictWords_2)
print(temp_list_dictWords_2[0][0])

# OK
