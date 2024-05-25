#   Дана строка-предложение на русском языке. Вывести самое длинное слово в предложении. Если таких слов несколько, то вывести первое из них. Словом считать набор символов, не содержащий пробелов, знаков препинания и ограниченный пробелами, знаками препинания или началом/концом строки.
def longest_word(sentence):
    words = sentence.split()  # разбиваем предложение на слова
    max_length = 0
    longest = ""
    for word in words:
        clean_word = ”.join(filter(str.isalpha, word))  # удаляем знаки препинания
        if len(clean_word) > max_length:
            max_length = len(clean_word)
            longest = clean_word
    return longest