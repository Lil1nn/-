#В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
#Посчитать количество полученных элементов

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lines = text.split('\n')

works = set()
for line in lines:
    if "«" in line and "»" in line:
        work = line[line.find("«")+1 : line.find("»")]
        works.add(work)

print("Произведения писателя Ф. М. Достоевского:")
for work in works:
    print(work)

num_works = len(works)
print("\nОбщее количество произведений писателя: ", num_works)