ротьл#  С помощью функций получить вертикальную и горизонтальную линии. Линия проводится многократной печатью символа. Заключить слово в рамку из полученных линий.
def print_horizontal_line(symbol, length):
    line = symbol * length
    print(line)
def print_vertical_line(symbol, length):
    for i in range(length):
        print(symbol)

def print_word_in_frame(word):
    length = len(word)
    print_horizontal_line("*", length + 4)
    print_vertical_line("*", 3)
    print("*", word, "*")
    print_vertical_line("*", 3)
    print_horizontal_line("*", length + 4)

word = input("Введите слово: ")
print_word_in_frame(word)