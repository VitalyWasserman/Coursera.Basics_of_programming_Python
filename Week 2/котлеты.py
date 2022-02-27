k = int(input())
m = int(input())
n = int(input())
if n > k and k != 1:
    iter = n // k
    ostatok = n - (iter * k)
    time = (iter * k + ostatok) * 2
    print(time)
else:
    time = n * m * 2
    print(time)