a = int(input())
b = int(input())
c = int(input())
a1 = a % 2
b1 = b % 2
c1 = c % 2
sum = a1 + b1 + c1
if sum == 3 or sum == 0:
    print('NO')
else:
    print('YES')
