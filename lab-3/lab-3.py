#hill - шифрование
#текстті қабылдап hill методы арқылы шифрование жасап, шифрді қайтарады
import numpy as np

msg = input("Message: ").upper()

# zhup san bolsa sonyna 0 kosu
len_chk = 0
if len(msg) % 2 != 0:
    msg += "0"
    len_chk = 1

#текстти матрицаға
row = 2 #key 2lik bolgannan keiin 2 row bolady
col = int(len(msg)/2)
msg2d = np.zeros((row, col), dtype=int) #нулевая матрица курастырып аламыз

itr1 = 0
itr2 = 0
for i in range(len(msg)):
    if i % 2 == 0: #zhup index 0shy zholga askii-men ainalyp tusedi
        msg2d[0][itr1] = int(ord(msg[i])-65)
        itr1 += 1
    else: #tak index
        msg2d[1][itr2] = int(ord(msg[i])-65)
        itr2 += 1

key = input("Enter 4 letter Key String: ").upper()
key = key.replace(" ", "")

# key 2x2
key2d = np.zeros((2, 2), dtype=int)
itr3 = 0
for i in range(2):
    for j in range(2):
        key2d[i][j] = ord(key[itr3])-65
        itr3 += 1

encryp_text = ""
itr_count = int(len(msg)/2)
if len_chk == 0: #соңына 0 жалғамаған болсақ
    for i in range(itr_count):
        temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
        encryp_text += chr((temp1 % 26) + 65)
        temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
        encryp_text += chr((temp2 % 26) + 65)

else:
    for i in range(itr_count-1):
        temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
        encryp_text += chr((temp1 % 26) + 65)
        temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
        encryp_text += chr((temp2 % 26) + 65)

print("Encrypted Text: {}".format(encryp_text))