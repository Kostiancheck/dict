"""Дано нечетное число n. Создайте двумерный массив из n×n элементов,
заполнив его символами "." (каждый элемент массива является строкой из одного символа).
Затем заполните символами "*" среднюю строку массива, средний столбец массива,
главную диагональ и побочную диагональ. В результате единицы в массиве должны о
бразовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами."""

n=int(input("Введите нечётное число \n"))
a=[[str(".") for j in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            a[i][j]="*"
        elif i==n-j-1:
            a[i][j] = "*"
        elif i==n//2:
            a[i][j] = "*"
        elif j==n//2:
            a[i][j] = "*"
        else:
            pass


for row in a:
    print(' '.join([str(el) for el in row]))