# рекурсия и алгоритмы
# exsept - почитать что это
# Требуется найти n-е число Фибоначи. Через рекурсию.

# from modul1 import LastFibo
# print(LastFibo(7))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.


# journal1 = [1, 2, 3, 1, 2, 4, 5, 5]
# print(journal1)
# print(max(journal1), min(journal1))
# for i in range(len(journal1)):
#     if journal1[i]== max(journal1):
#         journal1[i] = min(journal1)
# print(journal1)

# journal1 = [1, 2, 3, 1, 2, 4, 5, 5]
# print(journal1)

# for item in journal1:
#     if item == max(journal1):
#         item = min(journal1)
#     print(item)

# Напишите функцию, которая принимает одно число
# и проверяет, является ли оно простым Напоминание: Простое число - это число, 
# которое имеет 2 делителя: 1  и n(само число)


# def is_simple(num):
#     if num > 2 and num % 2 != 0:
#         for i in range(3, num//2):
#             if num % i == 0:
#                 return False
#             return True
#     return False

# num = int(input("Введите число: "))

# print(is_simple(num))

# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе 
# запрещается объявлять массивы и использовать циклы
#  (даже для ввода и вывода).
# from modul1 import revers_range

# number = int(input("Введите число: "))
# revers_range(number)





