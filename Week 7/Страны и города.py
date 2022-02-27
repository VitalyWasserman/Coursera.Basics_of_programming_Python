N = int(input())
dictNi = {}
listMi = []

for Ni in range(0, N):
    lineSplit = input().split()
    # нулевой символ списка в ключ словаря, с первого - в значения
    dictNi[lineSplit[0]] = lineSplit[1:]

    # print(dictNi)

M = int(input())
for Mi in range(M):
    lineSplit = input()
    listMi.append(lineSplit)
# print(listMi)

for i in range(len(listMi)):
    for j in dictNi:
        # print(listMi[i], j)
        if listMi[i] in dictNi[j]: # равно значению
            print(j) #печатаем ключ
# OK
