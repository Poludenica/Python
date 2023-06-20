# Здесь map, lambda, filter, zip, enumerate и работа с файлами и с os

# def f(x):
#     return x*x
# a=f
# print(a(5))

# def calc1(a, b):
#     return a+b

# def calc2(a, b):
#     return a*b
    
# def math(op, x, y):
#     print(op(x, y))

# math(calc1, 5, 4)

# lambda функции. Позволяют сокращать функции

# calc1 = lambda a, b : a + b
# def math(op, x, y):
#     print(op(x, y))

# math(calc1, 5, 4)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i%2 == 0:
#         res.append((i, i**2))

# print(res)

# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x%2==0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# функция map 
# list1 = [x for x in range(1, 20)]
# print(list1)

# list1 = list(map(lambda x: x+10, list1))
# print(list1)

# задача: с клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел
#  Этот набор числе будет считан в качестве строки.
# как превратить список list строк в список list чисел? 

# .split() преобразовывает строки в список
# data = '15 156 96 3 5'
# print(data)

# data = data.split()
# print(data)

# data = list(map(int, data.split()))
# print(data)

# функция filter. ФИльтрует какие-то значения. Принимает два аргумента - функцию и объект. 
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 ==5, data))
# print(res)

# функция zip 
# Применяется к набору итерируемых объеутов и возвращает итератор с кортежами из элементов входных данных. 
# Ф-я пробегает по минимальному набору элементов, т.е. если в трех списках есть 4 значения, а в одном 3, 
# то он будет выдавать по 3 значениям
# users = ['user1', 'user2', 'user3']
# ids = [4, 2, 5]
# data = list(zip(users, ids))
# print(data)

# ф-я enumerate() применяется к итерируемому объекту и возвращает новый итератор с  кортежами из индекса и элементов входных данных
# позволянт пронумеровать набор данных
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)

# Файлы
# варианты режима mod:
# a - открытие для добавления данных
# r - открытие для чтения данных 
# w - открытие для записи данных. Каждый раз пересоздает. Т.е. если файл существовал, то он удалит, а затем запишет новые
# микс режимы:
# W+ позволяет открывать файл для записи и читать из него. Создает новый, если не существует
# r+ открывать файл для чтения и дописывать в него. Если файла не существует, выдаст ошибку
# colors = ['red', '8987', 'blue']
# data = open('file.txt', 'a') #здесь указываем режим, в котором будем работать/так же тут можно указать кодировку, которую хотим использовать
# data.writelines(colors) #разделителей не будет
# data.close()

# with open('file.txt', 'w') as data: #файл сам закроется не нужно close
#     data.write('line 1\n') # \n это перенос
#     data.write('line 2\n')
# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

# модуль os
# представляет множество ф-й для работы с операционной системой, причем их поведение, как правило, не зависит от ОС, поэтому программы остаются переносимыми.
# для того, чтобы начать работать с данным модулем необходимо его инмпортировать в свою программу:
# import os
# базовые ф-и данного модуля:
# os.chdir(path) - смена текущей директории
# import os
# os.chdir('C:/Users/7897/PycharmProjects/GB')

# os.getwd() - текущая рабочая директория
# import os
# print(os.getcwd()) 

# os.path - является вложенным модулем в модуль os и реализует некоторые полезные функции для работы с путями, такие как:
# os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/ogney/Desktop/GeekBrains/Work/Python/4lesson.py')) # '4lesson.py'

# os.path.abspath(path) - возвращает нормализованный абсолютный путь
# import os
# print(os.path.abspath('4lesson.py'))

# модуль shutil
# содержит набор ф-й высокого уровня для обработки файлов, групп файлов и папок. Доступные здесь ф-и позволяют копировать, 
# перемещать и удалять файлы и папки. Часто используются вместе с модулем os
# для того чтобы начать с ним работать его нужно импортировать в свою программу:
# import shutil
# ф-и модуля:
# shutil.copyfile(src, dst) - копирует содержимое(но не метаданные) файла src в файл dst
# shutil.copy(src, dts) - копирует содержимое файла src в файл или папку dst
# shutil.rmtree(path) - удаляет текущую директорию и все поддиректории; path должен указывать на директорию, а не на символическую ссылку





