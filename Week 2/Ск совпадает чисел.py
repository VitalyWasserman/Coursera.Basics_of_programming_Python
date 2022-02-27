a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and a == c:
    n = 3
if a == b and b != c:
    n = 2
if a != b and b == c:
    n = 2
if a == c and c != b:
    n = 2
if a != b and b != c and a != c:
    n = 0
print(n)
