inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w')
L = []
L_N = []
L_M = []

for line in inFile:
    lineSplit = line.rstrip()
    L.append(lineSplit)
# print(L)

NM = L[0].split()
N = int(NM[0])
M = int(NM[1])

del L[0]

# делим общий список на 2
for i in range(0, N):
    L_N.append(L[i])

for j in range(N, N + M):
    L_M.append(L[j])

# print(L_N)
# print(L_M)

SetCube_N = set(L_N)
SetCube_M = set(L_M)

# print(SetCube_N)
# print(SetCube_M)

# print('ответы')
# print(len(SetCube_N))
SetCube_Cross = SetCube_N & SetCube_M
# print(SetCube_Cross)
ListCube_Cross = list(SetCube_Cross)
print(len(ListCube_Cross), file=outFile)
ListCube_Cross = map(int, SetCube_Cross)
ListCube_Cross = sorted(ListCube_Cross)
print(*ListCube_Cross, file=outFile)

SetCube_NM = SetCube_N - SetCube_M
# print(SetCube_NM)
ListCube_NM = list(SetCube_NM)
print(len(ListCube_NM), file=outFile)
ListCube_NM = map(int, ListCube_NM)
ListCube_NM = sorted(ListCube_NM)
print(*ListCube_NM, file=outFile)

SetCube_MN = SetCube_M - SetCube_N
# print(SetCube_MN)
ListCube_MN = list(SetCube_MN)
print(len(ListCube_MN), file=outFile)
ListCube_MN = map(int, ListCube_MN)
ListCube_MN = sorted(ListCube_MN)
print(*ListCube_MN, file=outFile)

inFile.close()
outFile.close()

# OK
