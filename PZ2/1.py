#  Известно, что x кг конфет стоит А рублей , Y кг ирисок стоит В рублей. Определить , сколько стоит 1 кг шоколадных конфет , 1 кг ирисок , а также во сколько раз шоколадные конфеты дороже ирисок
def p(x, a, b):
    c = a / x
    i = b / x
    r = c / i

    return c, i, r


x = float(input("Введите вес шоколадных конфет в кг: "))
a = float(input("Введите стоимость шоколадных конфет в рублях: "))
b = float(input("Введите стоимость ирисок в рублях: "))

c, i, r = p(x, a, b)

print("Стоимость 1 кг шоколадных конфет:", c, "рублей")
print("Стоимость 1 кг ирисок:", i, "рублей")
print("Шоколадные конфеты дороже ирисок в", r, "раз")