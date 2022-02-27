inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w')
median_9 = 0  # сумма баллов
median_10 = 0
median_11 = 0
kol_9 = 0  # кол-во чел по классу
kol_10 = 0
kol_11 = 0
L = []
for line in inFile:  # считываем каждую строку, добавляем в список, состоящий из списков=кол-ву строк
    lineSplit = line.split()
    L.append(lineSplit)
    if int(L[-1][-2]) == 9:  # выбиарем с конца списка класс
        kol_9 += 1
        median_9 += int(L[-1][-1])  # выбиарем с конца списка балл
    elif int(L[-1][-2]) == 10:
        kol_10 += 1
        median_10 += int(L[-1][-1])
    else:
        kol_11 += 1
        median_11 += int(L[-1][-1])
print(median_9 / kol_9, median_10 / kol_10, median_11 / kol_11, file=outFile)
inFile.close()
outFile.close()

# OK
