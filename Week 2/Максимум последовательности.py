n = int(input())
n_max = n
while n != 0:
    n = int(input())
    if n > n_max:
        n_max = n
print(n_max)
