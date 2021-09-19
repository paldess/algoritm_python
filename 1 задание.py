


while True:
    number1 = int(input('введите первое число:   '))
    number2 = int(input('введите второе читсло:   '))

    s = -1
    while s == -1:
        go = input('введите действие(+,-,/,*, или 0 для выхода):   ')
        if go == '0':
            print('до свидания')
            exit(0)
        elif go == '+':
            result = number1+number2
            s = 1
        elif go == '-':
            result = number1-number2
            s = 1
        elif go == '*':
            result = number1*number2
            s = 1
        elif go == '/':
            if number2 == 0:
                result = 'на ноль делить нельзя'
            else:
                result = number1/number2
            s = 1
        else:
            print('ввели неверный знак')
    print(result)