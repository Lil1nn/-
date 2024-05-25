#   Дана строка. Подсчитать количество содержащихся в ней цифр.
def count_digits(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count

s= "123456"
print(count_digits(s))