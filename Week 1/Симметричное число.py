n = int(input(''))
a = n // 100
b = n % 100
a1 = a // 10
a2 = a % 10
b1 = b // 10
b2 = b % 10
r1 = a1 - b2
r2 = a2 - b1
print('', r1 + r2 + 1)
