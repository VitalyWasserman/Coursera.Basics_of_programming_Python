L = list(map(int, input().split()))
#print(L[::2])
print(' '.join(map(str, L[::2])))
#преобразуем список в строку через map, затем joinом слепляем через пробелы
#print(*L[::2])
# то же самое, но спец оператором *. Выводит все элементы списка через пробел

#ok