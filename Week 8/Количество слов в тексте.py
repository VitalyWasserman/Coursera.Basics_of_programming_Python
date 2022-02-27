#Вариант 1. Работает, но не функционально

#inFile = open('input.txt', 'r', encoding='utf8')

#print(len(set(inFile.read().split())))


#Вариант 2 . Работает, но рантайм еррор Читаем строками, режем джойном
#print(len(set(' '.join(open('input.txt', 'r', encoding='utf8').readlines()).split())))

#илич читая весь файл целиком
#print(len(set(open('input.txt', 'r', encoding='utf8').read().split())))


#Вариант 3. С импортом stdin  ПРОШЕЛ

#from sys import stdin

#print(len(set(stdin.read().split())))
