string = input('введите длины 3-х отрезкоов через пробел:   ')
x, y, z = map(int, string.split())


if x<= 0 or y<=0 or z<=0:
    print('треуголльник не построить')
elif x+y<z or x+z<y or z+y<x:
    print('треуголльник не построить')
else:
    if x == y == z:
        print('треугольник равносторонний')
    elif x == y or x == z or z == y:
        print('треугольник равнобедренный')
    else:
        print('тругольник разносторонний')