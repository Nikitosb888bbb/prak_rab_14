import random

rows = 3
cols = 4
list = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

print('Исходный список: ')
for row in list:
    print(row)

max_value = list[0][0]
max_row = 0
max_col = 0

i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        if list[i][j] > max_value:
            max_value = list[i][j]
            max_row = i
            max_col = j
        j += 1
    i += 1

print(f'Максимальный элемент: {max_value}')
print(f'Позиция: строка {max_row}, столбец {max_col}')
