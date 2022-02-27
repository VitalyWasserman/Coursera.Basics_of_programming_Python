n1 = int(input())
n2 = int(input())
n3 = int(input())
kol = 0
if n2 > n1:
    kol += 1
while n3 != 0:
    if n3 > n2:
        kol += 1
    n2 = n3
    n3 = int(input())
print(kol)