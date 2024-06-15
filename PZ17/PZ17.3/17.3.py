import os

# Перейти в каталог PZ11
os.chdir(r'C:\Users\user\Desktop\PZ\PZ11')

# Вывести список всех файлов в этом каталоге
files_in_pz11 = [f for f in os.listdir() if os.path.isfile(f)]
print("Файлы в каталоге PZ11:", files_in_pz11)
# Перейти в корень проекта (предполагается, что он на два уровня выше)
os.chdir(r'C:\Users\user\Desktop\PZ\PZ17\PZ17.3')

# Создать папку test и test1 внутри нее
os.makedirs('test/test1', exist_ok=True)

# Переместить два файла из ПЗ6 в папку test
os.rename(r'C:\Users\user\Desktop\PZ\PZ6/PZ6.1.py', r'C:\Users\user\Desktop\PZ\PZ17\PZ17.3\test\PZ6.1.py')
os.rename(r'C:\Users\user\Desktop\PZ\PZ6/PZ6.2.py', r'C:\Users\user\Desktop\PZ\PZ17\PZ17.3\test\PZ6.2.py')

# Переместить один файл из ПЗ7 в папку test1 и переименовать его в test.txt
os.rename(r'C:\Users\user\Desktop\PZ\PZ7/PZ17.txt', r'C:\Users\user\Desktop\PZ\PZ17\PZ17.3\test/test1/test.txt')
test_files = [f for f in os.listdir('test') if os.path.isfile(os.path.join('test', f))]
for f in test_files:
    file_path = os.path.join('test', f)
    print(f"Размер файла {f}: {os.path.getsize(file_path)} байт")
# Вернуться в PZ11
os.chdir(r'C:\Users\user\Desktop\PZ\PZ11')

# Найти файл с самым коротким именем
files_in_pz11 = [f for f in os.listdir() if os.path.isfile(f)]
shortest_filename = min(files_in_pz11, key=len)
print("Файл с самым коротким именем:", os.path.basename(shortest_filename))
# Перейти в папку с отчетом в формате .pdf
os.chdir(r'C:\Users\user\Desktop\PZ\PZ17')  # Укажите путь к папке с отчетом

# Найти .pdf файл и запустить его
pdf_file = next(f for f in os.listdir() if f.endswith('.pdf'))
os.startfile(pdf_file)
# Удалить файл test.txt
os.remove(r'C:\Users\user\Desktop\PZ\PZ17\PZ17.3\test\test1\test.txt')
