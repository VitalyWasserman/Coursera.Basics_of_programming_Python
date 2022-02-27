n = int(input())  # кол-во участников
listStudents = []  # сюда будем добавлять список студентов
for i in range(n):
    listStudents.append(list(input().split()))  # добавляем студентов по одному до числа n
    # print(listStudents)
listStudents.sort(key=lambda i: int(i[1]), reverse=True)

for i in (listStudents):
    print(i[0], i[1])

# ok
