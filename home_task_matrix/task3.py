"""Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его
символами "." и "*" в шахматном порядке.
В левом верхнем углу должна стоять точка."""
n=int(input('n='))
m=int(input('m='))


a=[["."] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i%2==0 and j%2==1) or(i%2==1 and j%2==0):
            a[i][j]="*"

for row in a:
    print(' '.join([str(el) for el in row]))