# def merge(L1, L2):
#    L = L1 + L2
#    L3 = []
#    for j in range(len(L)):
#        L3.append(min(L))
#  ищем минимальное значение, его в конец отдельного списка.
# из исходного удаляем
#        L.remove(min(L))
#    print(*L3)


def merge(L1, L2):
    L3 = []
    i, j = 0, 0
    for k in range((len(L1) + len(L2))):
        if i < len(L1) and j < len(L2):
            if L1[i] < L2[j]:
                L3.append(L1[i])
                i += 1
            else:
                L3.append(L2[j])
                j += 1
        elif i < len(L1):
            L3.append(L1[i])
            i += 1
        elif j < len(L2):
            L3.append(L2[j])
            j += 1
    print(*L3)


L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))
# L1 = [1, 5, 7]
# L2 = [2, 4, 4, 5]
merge(L1, L2)

# print(' '.join(map(str, L)))

# OK
