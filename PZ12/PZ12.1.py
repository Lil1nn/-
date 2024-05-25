#  Проверить есть ли в последовательности целых N чисел число К
import random

check_number = lambda sequence, k: k in set(sequence)

N = 10
sequence = [random.randint(1, 10) for _ in range(N)]

K = int(input("Введите число К: "))

print("Последовательность чисел:", sequence)

print("Число K:", K)

if check_number(sequence, K):
    print("Число K найдено в последовательности.")
else:
    print("Число K не найдено в последовательности.")
