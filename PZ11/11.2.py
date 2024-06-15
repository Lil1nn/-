# Чтение содержимого файла
with open('text18-15.txt', 'r',encoding="utf-16") as file:
    original_text = file.read()
    print("Содержимое файла:")
    print(original_text)

# Подсчет количества букв в нижнем регистре
lowercase_count = sum(1 for char in original_text if char.islower())
print("Количество букв в нижнем регистре:", lowercase_count)

# Замена символов нижнего регистра на верхний и запись в новый файл
uppercase_text = original_text.upper()
with open('text.txt', 'w', encoding="utf-16") as file:
    file.write(uppercase_text)

print("Текст в стихотворной форме с заменой на верхний регистр сохранен в файле 'text.txt'.")
