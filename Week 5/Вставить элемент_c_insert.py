L = list(map(int, input().split()))
k_C = list(map(int, input().split()))
#k = int(input())
#C = int(input())
L.insert(k_C[0], k_C[1])
print(*L)
#print(' '.join(map(str, L)))  То же самое, что *L