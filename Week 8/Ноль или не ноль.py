#n = int(input())
#L = []
#for i in range(n):
#    L.append(int(input()))
#print(0 in L)


# то же самое, в строку

print(any(map(lambda x: int(input()) == 0, range(int(input())))))

# OK