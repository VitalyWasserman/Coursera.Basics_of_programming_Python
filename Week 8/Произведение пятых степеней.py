#seq = map(int, input().split())
#Multiplex_5 = 1
#for elem in seq:
#    Multiplex_5 = Multiplex_5 * elem ** 5
#print(Multiplex_5)


# то же самое в строку


#print(sum(list(map(lambda x: x ** 5, map(int, input().split()))))) сумма


# произведение
from functools import reduce

print(reduce(lambda x, y: x * y,  (map(lambda x: x ** 5, map(int, input().split())))))


# ok