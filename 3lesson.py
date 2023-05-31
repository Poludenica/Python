# Функция - это фрагмент программы, используемый многократно
#  обозначается как def 
# def summnumbers(n, y = 'Hello'):
#     print(y)
#     summ = 0
#     for i in range(1, n+1):
#         summ += i
#     return summ
#     print('stop')

# print(summnumbers(5))
# если не передаем никакой аргумент, то ф-я берет значение по умолчанию

# def sum_str(*args): # указываем звездочку, если не знаем сколько аргументов будет передано
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'rtr', 'gh'))
# # print(sum_str(1, 8. 9))  # решить, почему не выводится - почему ошибка

# модули. Модульность. Это файл в котором прописаны разные функции
# чтобы импортировать модуль:
# вариант 1:
# import modul1
# print(modul1.max1(5,9))

# вариант 2:
# from modul1 import max1
# print(max1(5,10))

# вариант 3
# from modul1 import * # это обозначает, что из того модуля мы хотим импортировать абсолютно все функции

# вариант 4:
# import modul1 as m1 # присвоение на время модулю другого имени только в этой программе
# print(m1.max1(5,9))

# рекурсия - это ф-я вызывающая сама себя. При описании рекурсии важно указать, когда ф-и необходимо остановиться и перестать вызывать саму себя. 
# по-другому говоря, необходимо указать базис рекурсии

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# алгоритмы - набор инструкций для выполнения некоторой задачи. 
# к алгоритам относятся сортировки.
# быстрая сортировка - принадлежит стратегии "разделяй и властвуй". 
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot] 
#     greater = [i for i in array[1:] if i > pivot] 
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([10, 5, 2]))

# сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j +=1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i+=1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [1, 5, 6, 34, 56, 23, 45, 58]
merge_sort(list_1)
print(list_1)





