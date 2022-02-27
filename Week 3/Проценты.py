p = int(input())
x = (int(input())) * 100
y = int(input())
res = int(((x + y) + (x + y) * p / 100))
print(int((res / 100)), res - int(res / 100) * 100)
