n = int(input())
n1 = 1
S = 0
while n1 <= n:
    S = S + (1 / n1 ** 2)
    n1 += 1
print(S)
