import random

list = [[random.randint(1, 50) for _ in range(4)] for _ in range(3)]

print('Исходный список: ')
for row in list:
    print(row)

row_sums =[]
total_sum = 0
max_row_sum = 0
max_row_index = 0

row_idx = 0
while row_idx < len(list):
    current_row_sum = 0
    col_idx = 0

    while col_idx < len(list[row_idx]):
        current_row_sum += list[row_idx][col_idx]
        col_idx += 1

    row_sums.append(current_row_sum)
    total_sum += current_row_sum

    if current_row_sum > max_row_sum:
        max_row_sum = current_row_sum
        max_row_index = row_idx

    row_idx += 1

print('Суммы по строкам:')
i = 0
while i < len(row_sums):
    print(f'Строка {i}: {row_sums[i]}')
    i += 1

print(f'Общая сумма всех элементов: {total_sum}')
print(f'Строка с максимальным элементом: {max_row_sum}')
