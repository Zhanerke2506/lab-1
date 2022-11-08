# Hello! I'm Nurmakhanova Aliya and I'm gonna do this laboratory work with you ^-^
alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = int(input('Шаг шифровки: '))
message = input("Сообщение для Дешифровки: ").upper()
result = ''
lang = input('Выберите язык RU/EU: ')
if lang == 'RU':
    for i in message:
        mesto = alphabet_RU.find(i)
        new_mesto = mesto + key
        if i in alphabet_RU:
            result += alphabet_RU[new_mesto]
        else:
            result += i
else:
    for i in message:
        mesto = alphabet_EN.find(i)
        new_mesto = mesto + key
        if i in alphabet_EN:
            result += alphabet_EN[new_mesto]
        else:
            result += i
print(result)
