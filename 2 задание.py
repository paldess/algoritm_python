number = input('введите число:    ')

chetn = 0
notchetn = 0

for i in number:
    try:
        i = int(i)
        if i % 2 == 0:
            chetn += i
        else:
            notchetn += i
    except ValueError:
        print('вводить нужно только цифры. завершаю программу')
        exit(0)

print(f'сумма четных чисел равна {chetn} \nсумма нечетных чисел равна {notchetn}')