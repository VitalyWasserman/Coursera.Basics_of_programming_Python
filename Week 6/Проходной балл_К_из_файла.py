# K = int(input())
inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w')
ListStudents = []
Notes = []
ListStudentsSumm = []
j = 1

for line in inFile:  # считываем каждую строку,
    lineSplit = line.split()
    ListStudents.append(lineSplit)
    # print(ListStudents)
K = int((ListStudents[0][0]))
del ListStudents[0]
# print(K)
print(ListStudents)
print(len(ListStudents))
for i in range(0, len(ListStudents)):
    if int(ListStudents[i][-1]) >= 40 and int(ListStudents[i][-2]) >= 40 \
            and int(ListStudents[i][-3]) >= 40:
        ListStudentsSumm.append(int(ListStudents[i][-1]) +
                                int(ListStudents[i][-2]) +
                                int(ListStudents[i][-3]))
        print(ListStudentsSumm)

ListStudentsSumm.sort(reverse=True)  # список сумарных оценок
print(ListStudentsSumm)

for i in range(1, len(ListStudentsSumm)):
    if ListStudentsSumm[i] != ListStudentsSumm[i - 1]:
        Notes.append(j)
        j = 1
    else:
        j += 1
Notes.append(j)  # список кол-ва каждой сумарной оценки
print(Notes)
KolStudents = 0

if K >= int(len(ListStudentsSumm)):
    print(0, file=outFile)
elif K < Notes[0]:
    print(1, file=outFile)
else:
    for k in range(0, len(Notes)):
        if KolStudents + Notes[k] <= K:
            KolStudents = KolStudents + Notes[k]
            MinNote = ListStudentsSumm[KolStudents - 1]
        else:
            print(MinNote, file=outFile)
            break

inFile.close()
outFile.close()

# OK
