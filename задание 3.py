import random

work = input('выберите подзадание: \na-случайное целое число \nb-случайное вещественное число \nc-случайный символ \n')

if work == 'a':
    num = input('введите границы для генерации случайного целого числа через пробел:   ')
    num = num.split()
    print('случайное целое число: ', random.randint(int(num[0]), int(num[1])))

elif work == 'b':
    num = input('введите границы для генерации случайного ыещественного числа через пробел:   ')
    num = num.split()
    print('случайное вещественное число: ', random.uniform(float(num[0]), float(num[1])))

elif work == 'c':
    num = input('введите границы для генерации случайного случайного символа через пробел:   ')
    num = num.split()
    x = ord(num[0])
    y = ord(num[1])
    if x > y:
        x, y = y, x
    print('случайный символ: ', chr(random.randint(x, y)))