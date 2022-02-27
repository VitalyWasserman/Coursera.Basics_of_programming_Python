def IsAscending(i):
    if i == n:
        print('YES')
    else:
        print('NO')


L = list(map(int, input().split()))
n = len(L)
i = 1
while i < n and L[i] > L[i - 1]:
    i += 1
IsAscending(i)


# работает, но надо избавиться от if