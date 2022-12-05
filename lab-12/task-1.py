import os

def euclid_ext(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclid_ext(b, a % b)
        return d, y, x - y * (a // b)

p = 5
q = 19
n = p * q
phi = (p - 1) * (q - 1)
print(n, phi)
e = 24
gcd, d, y = euclid_ext(e, phi)
d %= phi
if d < 0:
    d += phi
open_key = (e, n)
secret_key = (d, n)
print(open_key)
f = open('openkey.txt', 'w')
f.write(str(open_key))

print(secret_key)
f = open('secretkey.txt', 'w')
f.write(str(secret_key))

m = input("Выбрать текст для зашифрования:")
encrypted = []
for i in m:
    o = ord(i)
    enc = pow(o, e) % n
    encrypted.append(enc)
print(encrypted)
f = open('encryptedfile.txt',  'w')
f.write(str(encrypted))

print ("Я на позиции:", f.tell())
f.truncate(10)
f.close()

os.rename('encryptedfile.txt', 'encrypted.txt')


# decrypted = []
# for i in enc:
#     dec = pow(i, d) % n
#     ch = chr(dec)
#     decrypted.append(ch)
# print(decrypted)
# f = open('decryptedfile.txt', 'w')
# f.write(str(decrypted))
# f.close()