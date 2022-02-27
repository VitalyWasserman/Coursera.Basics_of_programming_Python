n1 = int(input())
n2 = int(input())
n3 = int()
if n2 == 0:
    kol_max = 1
else:
    n3 = int(input())
    if n1 < n2:
        max = n2
        kol_max = 1
    elif n1 > n2:
        max = n1
        kol_max = 1
    else:
        max = n2
        kol_max = 2
while n3 != 0:
    if n3 > max:
        max = n3
        kol_max = 1
    elif n3 == max:
        kol_max += 1
    n3 = int(input())
print(kol_max)
