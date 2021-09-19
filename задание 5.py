
x = 0

for i in range(32, 128):
    if x % 10 == 0 and x != 0:
        print(f'{i} - {chr(i)}', end=';\n')
        x += 1
    else:
        print(f'{i} - {chr(i)}', end='; ')
        x += 1