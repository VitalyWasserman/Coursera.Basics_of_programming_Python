K = int(input())
inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w')
ListStudents = []
Notes = []
j = 1

for line in inFile:  # считываем каждую строку,
    # добавляем в список, состоящий из списков=кол-ву строк
    lineSplit = line.split()
    # print(lineSplit) # суммируем оценки
    lineSplit.append(int(lineSplit[-1]) + int(lineSplit[-2]) + int(lineSplit[-3]))
    # print(lineSplit)
    if int(lineSplit[-2]) >= 40 and int(lineSplit[-3]) >= 40 \
            and int(lineSplit[-4]) >= 40:
        ListStudents.append(lineSplit[-1])  # оставляем только сумарный балл
        # print(ListStudents)

ListStudents.sort(reverse=True)  # список сумарных оценок
print(ListStudents)

for i in range(1, len(ListStudents)):
    if ListStudents[i] != ListStudents[i - 1]:
        Notes.append(j)
        j = 1
    else:
        j += 1
Notes.append(j)  # список кол-ва каждой сумарной оценки
print(Notes)
KolStudents = 0

if K >= len(ListStudents):
    print(0, file=outFile)
elif K < Notes[0]:
    print(1, file=outFile)
else:
    for k in range(0, len(Notes)):
        if KolStudents + Notes[k] <= K:
            KolStudents = KolStudents + Notes[k]
            MinNote = ListStudents[KolStudents - 1]
        else:
            print(MinNote)
            print(MinNote, file=outFile)
            break


inFile.close()
outFile.close()


# OK
