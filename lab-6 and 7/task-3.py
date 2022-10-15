"""
5. Словарь синонимов
Вам дан словарь, состоящий из пар слов. 
Каждое слово является синонимом к парному ему слову. 
Все слова в словаре различны. Для одного данного слова определите его синоним.
"""

dictionary = {}
n = int(input())
for i in range(n):
    first, second = input().split()
    dictionary[first] = second
    dictionary[second] = first

print(dictionary[input()])