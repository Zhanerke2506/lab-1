a = input("a:")
b = input("b:")

while not(a.isdigit() and b.isdigit()):
    print("Input number!")
    a = input("a:")
    b = input("b:")

print(int(a) + int(b))