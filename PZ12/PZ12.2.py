#  Составить список, в который будут включены только согласные буквы и привести их к верхнему регистру.
vowels = "ауоиэыяюеё"  # гласные буквы
text =input("Введите текст:" )  # исходный текст

# Функция, которая проверяет, является ли символ согласной буквой
def is_consonant(char):
    return char.isalpha() and char.lower() not in vowels

# Функция, которая преобразует символ в верхний регистр
def to_upper(char):
    return char.upper()

# Список всех символов, которые удовлетворяют условию is_consonant
consonants = list(filter(is_consonant, text))

# Преобразуем все согласные буквы в верхний регистр
result = list(map(to_upper, consonants))

print(result)
