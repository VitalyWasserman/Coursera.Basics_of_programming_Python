n = int(input())
m = 2
while m <= n:
    if n % m == 0:
        print(m)
        break
    else:
        m = m + 1
