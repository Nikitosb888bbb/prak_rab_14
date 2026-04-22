max_item_count = input('Введите количество предметов, которе может унести игрок: ')
item_value = input('Введите ценность найденых предметов (через пробел): ')

try:
    num = int(max_item_count)
    items = list(map(int, item_value.split()))

    sorted_items = items.copy()

    i = 0
    while i < len(sorted_items) - 1:
        j = 0
        while j < len(sorted_items) - i - 1:
            if sorted_items[j] > sorted_items[j + 1]:
                temp = sorted_items[j]
                sorted_items[j] = sorted_items[j + 1]
                sorted_items[j + 1] = temp
            j += 1
        i += 1

    selected_items = []
    index = 0
    while index < num and index < len(sorted_items):
        selected_items.append(sorted_items[index])
        index += 1

    total_value = 0
    k = 0
    while k < len(selected_items):
        total_value += selected_items[k]
        k += 1

    print(f'Максимальная возможная суммарная ценность: {total_value}')

except ValueError:
    print('Ошибка ввода данных. Убедитесь, что вводите целые числа.')
