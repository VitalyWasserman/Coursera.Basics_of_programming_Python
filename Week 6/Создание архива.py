L1 = list(map(int, input().split()))
s = L1[0]
n = L1[1]
L2 = []
V = 0
k = 0
for i in range(n):
    L2 = L2 + list(map(int, input().split()))
L2.sort()
# print(*L2, sum)
if sum(L2) < s:
    print(len(L2))
else:
    while V <= s:
        V = V + L2[k]
        k += 1
    print(k - 1)

# ok
