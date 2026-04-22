import random

list = [[random.randint(-50, 50) for _ in range(4)] for _ in range(3)]

print('Исходный список:')
for row in list:
    print(row)

positive_list = []

i = 0
while i < len(list):
    positive_row = []
    j = 0

    while j < len(list[i]):
        if list[i][j] > 0:
            positive_row.append(list[i][j])
        j += 1

    if positive_row:
        positive_list.append(positive_row)
    i += 1

print('Отфильтрованный список(только положительные элементы):')
if positive_list:
    for row in positive_list:
        print(row)
else:
    print('Положительные элементы отсутствуют')
