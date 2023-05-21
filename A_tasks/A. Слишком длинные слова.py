import sys

n = int(sys.stdin.readline().split()[0]) # ввод

words = [] # создаем пустой список, где будут храниться слова

for line in sys.stdin:
    for word in line.split():
        words.append(word)
for word in words: # вытаскиваем слово из списка
    if len(word) > 10: # проверка длины слова
        print(word[0]+ str(len(word) - 2) + word[-1]) # обезаем слово по правилу "первая буква + кол-во букв между ними + последняя буква"
    else:
        print(word)