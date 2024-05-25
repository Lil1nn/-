#  В матрице найти максимальный положительный элемент, кратный 4.
import random

# Запросить у пользователя количество строк и столбцов матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Создать матрицу и заполнить случайными целыми числами
matrix = [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

# Вывести матрицу на экран
print("Сгенерированная матрица:")
for row in matrix:
    print(row)

# Искать максимальный положительный элемент, кратный 4, в матрице
max_element = None
for row in matrix:
    for element in row:
        if element > 0 and element % 4 == 0:
            if max_element is None or element > max_element:
                max_element = element

# Вывести найденный элемент на экран
if max_element is not None:
    print(f"Максимальный положительный элемент, кратный 4, в матрице: {max_element}")
else:
    print("В матрице не найден положительный элемент, кратный 4.")

