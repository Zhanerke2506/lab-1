# Функция map() может принимать пользовательские функции в качестве параметров. 
# Параметры этих функций устанавливаются исключительно пользователем или программистом.

names = ['aliya','zhanerke','almash']
mapped_names = list(map(lambda x: x+' madam',names))
print(mapped_names)


# Функция reduce(), 
# как можно понять из названия, применяет 
# переданную функцию к итерируемому объекту и возвращает одно значение.
from functools import reduce
#numbers = [3, 4, 6, 9, 34, 12]
numbers = [36,27,24,21,18,12]
def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers)
print(result)


# Функция filter() используется 
# для создания списка, состоящего из значений, для которых функция возвращает true. Синтаксис этого следующий:

def func(x):
    if x>=3:
        return x
y = filter(func, (1,2,3,4))  
print(y)
print(list(y))
