# #1 Вычислить число c заданной точностью d
# print('Введите число')
# n = float(input()) #number
# print('Введите до скольки хотите округлить число')
# d = float(input()) #точность
# if d == 1:
#     print(int(n))
# else:
#     d = str(d)
#     d = d.split('.')
#     d = len(d[1]) #посчитаем длину правой части
#     print(round(n, d)) # округляем n до d

# #2
# print("Введите N")
# n = int(input())
# li = [i for i in range(2,n+1,1) if n%i == 0]
# print(f'{li} - все множители числа {n}')

# def simple_mn(x):
#     for i in range (2,x//2+1):
#         if x%i == 0:
#             return False
#     return True
        
# new_list = list(filter(simple_mn, li))
# print(f'{new_list} - простые множители числа {n}')

# 3 Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# print('Введите элементы списка через пробел')
# a = list(map(int, input().split()))
# new_list=[]
# for i in a:
#     if a.count(i) == 1:
#         new_list.append(i)
# print(new_list)

# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# import random
# print('Введите степень k')
# k = int(input())
# coef= [random.randint(0,100) for _ in range(k+1)]
# print(coef)
# with open ('coef.txt', 'w', encoding='utf-8') as a:
#     for i in range(len(coef)):
#         if k-i !=1 and k-i!=0:
#             a.write(f'{coef[i]}x^{k-i} +')
#         elif k-i == 1:
#             a.write(f'{coef[i]}x +')
#         elif k-i == 0:
#             a.write(f'{coef[i]} = 0')

 

        
