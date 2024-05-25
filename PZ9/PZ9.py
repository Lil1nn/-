#  Организовать словарь на 10 русско-английских слов обеспечивающий " перевод" английского слова на русский
# Создание словаря
dictionary = {
    "яблоко": "apple",
    "банан": "banana",
    "вишня": "cherry",
    "апельсин": "orange",
    "лимон": "lemon",
    "арбуз": "watermelon",
    "груша": "pear",
    "клубника": "strawberry",
    "малина": "raspberry",
    "ананас": "pineapple"
}

# Запрос перевода у пользователя
word = input("Введите слово на английском: ")

# Поиск перевода в словаре
if word in dictionary.values():
    for key, value in dictionary.items():
        if value == word:
            print("Перевод слова", word, "на русский:", key)
else:
    print("Слово", word, "не найдено в словаре")
