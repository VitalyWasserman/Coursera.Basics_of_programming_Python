n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 <= n2:
    max2 = n1
    max1 = n2
else:
    max1 = n1
    max2 = n2
while n3 != 0:
    if n3 >= max1:
        max2 = max1
        max1 = n3
    elif n3 > max2:
        max2 = n3
    n3 = int(input())
print(max2)
