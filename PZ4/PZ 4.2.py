#  Дано целое число N (>0). Найти наименьшее целое положительное число К, квадрат которого превосходит N: К2 > N. Функцию извлечения квадратного корня не использовать
N = int(input("Введите целое число N (> 0): "))

K = 1
while K ** 2 <= N:
    K += 1

print("Наименьшее целое положительное число К, квадрат которого превосходит N:", K)