#  Дан список размера N. Найти номера тех элементов списка, которые больше своего правого соседа, и количество таких элементов. Найденные номера выводить в порядке их возрастания.
def find_elements(numbers):
    result = []
    count = 0
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            result.append(i)
            count += 1
    return result, count

input_list = [3, 2, 5, 7, 4, 8, 9]
indices, total_count = find_elements(input_list)
print("Найденные номера элементов:", indices)
print("Количество таких элементов:", total_count)
