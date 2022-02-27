#L1 = map(int, input().split())
#L2 = map(int, input().split())
#L3 = []
#summ = list(zip(L1, L2))
#print(summ)

#или так (выводит тру и фэлс)
#for i in summ:
#    print(i[0] ^ i[1])

# или так
#for i in summ:
#    if i[0] == i[1]:
#        L3.append(0)
#    else:
#        L3.append(1)
#print(*L3)



# то же в одну строку
print(*list(map(lambda a, b: a ^ b, map(int, input().split()), map(int, input().split()))))

