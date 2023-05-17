# print(5)
# print(5)

"""
print(5)
print(5, 8)
print(5)
"""

# a = 5
# b = 5.89
# c = "hello"

# # print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))

# ввод данных
# print('Input first row')
# a = int(input())

# b = int(input('Input first row: '))
# print()
# print(a)

# print(a, '+', b, '=', a + b)

# c = 5.89
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# округление чисел
# a = 5.89778
# b = 6.6896
# print(a*b)
# print(round(a*b, 3))

# сокращенное присваивание
# i = 2
# i += 3  #i = i + 3
# i -= 3  #i = i - 3
# i *= 3  #i = i * 3
# i /= 3  #i = i / 3
# i //= 3  #i = i // 3
# i %= 3  #i = i % 3
# i **= 3  #i = i ** 3 возведение в степень 

# логические операции
# > больше
# >= больше или равно
# < меньше
# <= меньше или равно
# == равно (проверяет, равны ли числа)
# != не равно(проверяет, не равны ли значения)
# not не(отрицание)
# and и (конъюкция)
# or или (дизъюнкция)

# управляющие конструкции if; if-else
#  отступы tab или 4 пробела
#  elif - элс иф
# username = input('Input your name: ')
# if username == 'Masha':
#     print('Great! Hello, Masha!')
# elif username == 'Greg':
#     print('Oooh! I so glad to see you, Greg!')
# elif username == 'Bob':
#     print('Bob - cool')
# else:
#     print('Hi,', username)

# цикл while; while-else
# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('So')
#     print('enough')
# print(i)

#  Метод флажка
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: #если остаток при делении числа n На i равно 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# цикл for - используется для  перебора значений, функция range() - выдает значения из диапозона с шагом 1
# for i in 1, 5, 67:
#     print(i)

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(0, -5) # ----
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20

# r = range(100, 0, -20)
# for i in r:
#     print(i)

# a = 'qwerty'
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     print('*')


# # Строки
# text = "eat more This bRead"
# print('more' in text)
# print(text.lower())выравнивание по строчным
# print(text.upper()) #выравнивание по заглавным
# print(text.replace('more', 'MORE'))

# индексация. Срез 
# text = "eat more This bRead"
# print(text[0])
# print(text[len(text)-1]) #обращение к последнему индексу 
# print(text[-1]) # это запускает индексацию с конца строки, т.е с d
# print(text[:]) #выводятс все символы
# print(text[:2]) #выводят элементы с 0 до 2
# print(text[len(text)-2:]) #выводит два элемента с конца
# print(text[10:]) 
# print(text[2:9]) 
# print(text[6:-7]) 
# print(text[0:len(text):6]) #от 0 до конца строки с шагом 6
# print(text[::6]) #по умолчанию от начала для конца

# text = text[2:5] + text[-1] + text[:2]
# print(text)



    



