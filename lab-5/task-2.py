a = [["Zhanerke", 80],
     ["Aruzhan", 85]]
name = input("name:")
for i in range(len(a)):
    for j in range(len(a)):
        if name == a[i][0]:
            print(a[i][0], ":", a[i][1])
            break
        else:
            print("Ondai student joq!")
            break