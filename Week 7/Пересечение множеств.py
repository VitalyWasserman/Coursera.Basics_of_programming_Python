mySet1 = set(map(int, input().split()))
mySet2 = set(map(int, input().split()))
print(*sorted(list(mySet1 & mySet2)))

# ok
