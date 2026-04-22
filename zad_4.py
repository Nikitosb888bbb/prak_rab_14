import random

list = [[random.randint(1, 5) for _ in range(5)] for _ in range(4)]

search_value = int(input('Введите искомый элемент: '))

print('Исходный список:')
for row in list:
    print(row)

found_position = []

i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        if list[i][j] == search_value:
            found_position.append((i, j))
        j += 1
    i += 1

if found_position:
    print(f'Элемент {search_value} найден в следующих позициях: ')
    pos_idx = 0
    while pos_idx < len(found_position):
        pos = found_position[pos_idx]
        print(f'Строка {pos[0]}, столбец {pos[1]}')
        pos_idx += 1
else:
    print(f'Элемент {search_value} не найден')
