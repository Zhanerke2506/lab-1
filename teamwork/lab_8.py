# Hello! I'm Nurmakhanova Aliya and I'm gonna do this laboratory work with you ^-^
# alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# key = int(input('Шаг шифровки: '))
# message = input("Сообщение для Дешифровки: ").upper()
# result = ''
# lang = input('Выберите язык RU/EU: ')
# if lang == 'RU':
#     for i in message:
#         mesto = alphabet_RU.find(i)
#         new_mesto = mesto + key
#         if i in alphabet_RU:
#             result += alphabet_RU[new_mesto]
#         else:
#             result += i
# else:
#     for i in message:
#         mesto = alphabet_EN.find(i)
#         new_mesto = mesto + key
#         if i in alphabet_EN:
#             result += alphabet_EN[new_mesto]
#         else:
#             result += i
# print(result)

# print("hi guys !  why this code isn't working. qasqa")
# print("i'm comin back for you")
room = str(input())
if room == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    s = (p * (p-a) * (p-b) * (p-c))**0.5
    print(s)
elif room == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif room == 'круг':
    r = int(input())
    pi = 3.14
    print(pi * r**2)
else:
    print("Введите треугольник, круг или прямоугольник")