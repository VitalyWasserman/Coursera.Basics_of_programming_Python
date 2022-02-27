from math import sqrt


x1 = int(input())
x2 = int(input())
x3 = int(input())
n = 2
sum = x1 + x2

while x3 != 0:
    n += 1
    sum = sum + x2
    S = sum / n
    D = D + (x3 - S) ** 2
    #D = (x1 - S) ** 2 + (x2 - S) ** 2
    O = sqrt(D/(n - 1))



    x3 = int(input())


print(O)
