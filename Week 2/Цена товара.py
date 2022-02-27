n = float(input())
n = n * 100
if (n - int(n)) >= 0.5:
    n = int(n) + 1
else:
    n = int(n)
rub = n // 100
kop = n % 100
print(rub, kop)
