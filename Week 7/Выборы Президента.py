inFile = open('input.txt', 'r', encoding="utf-8")
outFile = open('output.txt', 'w', encoding="utf-8")

dictWords = {}
countPresinent = 0

for line in inFile:
    lineSplit = line.split('\n')
    # print(line)
    countPresinent += 1
    for i in lineSplit:
        if i not in dictWords:
            dictWords[i] = 1
        else:
            dictWords[i] = dictWords[i] + 1
# print(dictWords)

# удаляем пустой индекс, кот получился после каждой строки
dictWords.pop('')
# print(countPresinent)
# print(dictWords)

# перобразуем в список
list_dictWords = list(dictWords.items())
# print(list_dictWords)

# сортируем по кол-ву голосов
list_dictWords.sort(key=lambda i: i[1], reverse=True)
# print(list_dictWords)

# если сумарный бал больше половины, то печатем этого
# кандидата, иначе, первых двух
if int(list_dictWords[0][1]) > countPresinent / 2:
    print(list_dictWords[0][0], file=outFile)
else:
    print(list_dictWords[0][0], list_dictWords[1][0], sep='\n', file=outFile)

# OK
