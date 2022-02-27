L = list(map(int, input().split()))
x = int(input())
place = 1
for i in L:
    if i >= x:
        place += 1
print(place)

# OK