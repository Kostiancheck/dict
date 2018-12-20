"""Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.    """
n=int(input('n='))
m=int(input('m='))
list=[[int(input('Введіть число ')) for j in range(m)]for i in range(n)]

a=int(input('a='))
b=int(input('b='))

for row in list:
    print(' '.join([str(el) for el in row]))
print('\n\n')

for j in range(m):
    for i in range(n):
        some_var=list[i][a]
        list[i][a]=list[i][b]
        list[i][b]=some_var
for row in list:
    print(' '.join([str(el) for el in row]))