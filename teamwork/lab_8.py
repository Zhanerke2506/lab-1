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

list = ["apple","pear","banana","grape"]


list2 = ["watermelon","peach"]
list.extend(list2)  #extends
list.append("abrikos") #adds
print(list)
print(list2)