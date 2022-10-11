from random import shuffle

arr = [*range(1, 50)]
shuffle(arr)
print(sorted(arr[:6]))