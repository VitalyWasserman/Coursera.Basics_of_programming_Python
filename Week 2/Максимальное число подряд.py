n1 = int(input())
n2 = int(input())
rep = int()
kol = 1
kol_max = int()
while n2 != 0:
    if n2 == n1:
        n1 = n2
        rep = n2
        kol += 1
        if kol > kol_max:
            kol_max = kol
    else:
        n1 = n2
        kol = 1
    n2 = int(input())
if kol > kol_max:
    kol_max = kol
print(kol_max)
