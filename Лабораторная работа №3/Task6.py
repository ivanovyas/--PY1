list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
maximum = 0  # Вводим переменную для максимального значения
index = 0  # Вводим переменную для индекса максимального значения
for pos, value in enumerate(list_numbers):  # Перебираем все элементы списка и их индексы
    if value >= maximum:  # Элемент больше или равен всем предыдущим
        maximum = value
        index = pos  # Индекс такого элемента

list_numbers[index], list_numbers[-1] = list_numbers[-1], list_numbers[index]  # Меняем местами последний максимальный и последний элементы

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

