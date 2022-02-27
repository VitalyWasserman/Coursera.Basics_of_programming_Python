n1 = int(input())
n2 = int(input())
kol_kv = n2 - n1 + 1
kol_pod = n2 % kol_kv
if kol_pod == 0:
    print('YES')
else:
    print('NO')
