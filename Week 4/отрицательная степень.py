def power(a, n):
    if n % 2 == 0:
        return (a ** 2) ** (n / 2)
    return a * a ** (n - 1)

a = int(input())
n = int(input())
print(power(a, n))

#OK
