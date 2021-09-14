x = [j for j in range(97, 123)]
simbol = {j:i for i, j in enumerate(map(chr, x), 1)}


n = input('введите 2 буквы английского алфавита через пробел:   ')
n = n.split()

print(f'первая буква {n[0]} на {simbol[n[0]]} месте')
print(f'вторая буква {n[1]} на {simbol[n[1]]} месте')
print(f'между ними {abs(simbol[n[1]]-simbol[n[0]]-1)} символов')