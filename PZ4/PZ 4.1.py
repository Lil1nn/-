#  Дано вещественное число А и целое число N (>0). Используя один цикл, вывести все целые степени числа А от 1 до N.
a = float(input("Введите число A: "))
n = int(input("Введите число N: "))

result = 1

for i in range(abs(n)):
    result *= a

if n < 0:
    result = 1 / result

print("Результат:", result)
