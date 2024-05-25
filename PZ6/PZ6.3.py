#  Дан список А размера N и целые числа К и L (1 < K < L < N). Переставить в обратном порядке элементы списка, расположенные между элементами Ак и AL, не включая эти элементы.
def reverse_elements_between(A, K, L):
    if K < L < len(A):
        A[K+1:L] = A[K+1:L][::-1]
    return A
n = int(input("Введите количество элементов в списке: "))

# Запрос у пользователя самих элементов списка
A = [int(input("Введите элемент {}: ".format(i+1)) for i in range(n)]
K = int(input("Введите значение K: "))
L = int(input("Введите значение L: "))

result = reverse_elements_between(A, K, L)
print(result)
