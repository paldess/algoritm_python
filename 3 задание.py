number = input('введите число:    ')

result = ''
for i in range(1, len(number)+1):
    result += number[-i]

print(result)