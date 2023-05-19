# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 
# Вариант 1. под трехзначное число:
# num = int(input('Input a three-digit number: '))
# sum = 0
# inputnum = num 

# if num > 99 and num < 1000:
#     sum = num % 10
#     sum = sum + num//100
#     num = num // 10
#     sum = sum + num % 10
#     print(f'the sum of the three numbers of {inputnum} is {sum}')
# else: print('That number is not a three-digit number')


# Вариант 2. универсальная под любое число:
# num = int(input('Input a number: '))
# sum = 0
# inputnum = num
# while num > 0:
#   digit = num % 10
#   sum = sum + digit
#   num = num // 10
# print(f'the sum of the three numbers of {inputnum} is {sum}')
# 

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
# quantity = int(input('input the quantity of cranes: '))

# if quantity % 6 == 0:
#     k = quantity//6
#     a = k
#     b = k
#     c = k**2
#     print(f'Petya made {a} cranes, Seresha made {b} cranes and Katya made {c} cranes')
# else: print('The condition of multiplicity is not met')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# num = int(input("Input numbers of ticket: "))
# if num > 99999 and num < 1000000:
#     sum1 = num % 10
#     num = num//10
#     sum1 += num % 10
#     num = num//10
#     sum1 += num % 10
#     num = num//10
#     sum2 = num % 10
#     num = num//10
#     sum2 += num % 10
#     sum2 += num//10
#     if sum1 == sum2:
#         print("YES")
#     else:
#         print("NO")
# else:
#         print("That's the wrong number.")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
# n = int(input("Input the number of chocolate slices vertically: "))
# m = int(input("Input the number of slices of chocolate horizontally: "))
# k = int(input("Enter the number of slices to break off: "))
# if k % n == 0 or k % m == 0:
#     print("YES")
# else:
#     print("NO")