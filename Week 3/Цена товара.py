n = float(input())
#print(int(n), int((n - int(n))*100), sep=' ') неверно округляет
n = n * 100
rub = int(n // 100)
kop = int(n % 100)
print(rub, kop)

