L = list(map(int, input().split()))
for i in range (1, len(L)):
    if L[i] >= 0 and L[i - 1] >= 0:
        print(L[i - 1], L[i])
        break
    elif L[i] < 0 and L[i - 1] < 0:
        print(L[i - 1], L[i])
        break


#OK