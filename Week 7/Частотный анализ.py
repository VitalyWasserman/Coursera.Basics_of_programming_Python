inFile = open('input.txt', 'r')
dictWords = {}

for line in inFile:
    lineSplit = line.split()
    for i in lineSplit:
        if i not in dictWords:
            dictWords[i] = 1
        else:
            dictWords[i] = dictWords[i] + 1
# print(dictWords)
list_dictWords = list(dictWords.items())
# print(list_dictWords)

# сортируем сначала по алфафиту
temp_list_dictWords_1 = sorted(list_dictWords)
# print(temp_list_dictWords_1)

# сортируем уже отсортированное по -алфавиту, по частоте
temp_list_dictWords_2 = sorted(temp_list_dictWords_1,
                               key=lambda i: i[1], reverse=True)
# print(temp_list_dictWords_2)

for i in range(len(temp_list_dictWords_2)):
    print(temp_list_dictWords_2[i][0])

# OK
