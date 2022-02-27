L = list(map(int, input().split()))
k_C = list(map(int, input().split()))
L.append(k_C[1])
#L[4:4] = 99
for i in range(0, len(L)):

print(*L)
#print(' '.join(map(str, L)))  То же самое, что *L

НЕ ДОДЕЛАНО