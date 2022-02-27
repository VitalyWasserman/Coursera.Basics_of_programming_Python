inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w')
L = []
for line in inFile:
    # считываем каждую строку, добавляем в список, состоящий из списков=кол-ву строк
    lineSplit = line.split()
    L.append(lineSplit)
L_sort = sorted(L)
for i in range(len(L_sort)):
    # перебираем каждый элемент общего списка и печатаем его вложенные элементы по индексу
    print(L_sort[i][0], L_sort[i][1], L_sort[i][3], file=outFile)

inFile.close()
outFile.close()

# OK
