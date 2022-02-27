def Intersection(L1, L2):
    L = sorted(L1 + L2)
    for i in range(1, len(L)):
        if L[i] == L[i - 1]:
            print(L[i], end=' ')


L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))
# L1 = [1, 3, 4, 7, 9]
# L2 = [2, 3, 7, 10, 11]
Intersection(L1, L2)

# ok
