import random

# Генерируем последовательность случайных целых чисел и записываем их в файл input.txt
with open('input.txt', 'w') as file:
    num_elements = 10
    numbers = [random.randint(-100, 100) for _ in range(num_elements)]
    file.write(' '.join(map(str, numbers)))

# Читаем числа из файла и выполняем требуемую обработку
with open('input.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))

min_index = numbers.index(min(numbers))
multiplier = numbers[0]

# Умножаем все элементы на первый элемент
processed_numbers = [num * multiplier for num in numbers]

# Записываем обработанные числа и информацию об исходных данных в новый файл output.txt
with open('output.txt', 'w') as file:
    file.write(f"Исходные данные: {numbers}\nКоличество элементов: {len(numbers)}\nИндекс последнего минимального элемента: {min_index}\n")
    file.write(f"Умножаем все элементы на первый элемент: {' '.join(map(str, processed_numbers))}")