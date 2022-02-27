n = int(input())
sum = 0
kol = 0
while n != 0:
    sum = sum + n
    kol += 1
    n = int(input())
print(sum / kol)