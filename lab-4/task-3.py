# Дана строка.
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# В девятой строке выведите длину данной строки.
s = input("text:")
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])

print(len(s)) #длинасы
print (s.islower()) #lower ma tekseredi
print (s.isupper()) #upper ma tekseredi
print (s.isdecimal())  #ondyk pa tekseredi
print ('2'.isdigit()) #san ba tekseresi
print (s.isnumeric()) #ishinde san bolsa true kaitarady
print ('python3'.isalpha()) #aripter ma tekseredi
print (s.rjust(10,'-')) #on zhagyna symbol kosady
print (s.ljust(10,'-')) #sol zhagyna symbol kosady
print (s.center(20,'*')) #textti center alyp symbol kosady
print (s.find("a")) #isdeu
print (s.replace('a',"A")) #a-ny A-ga auystyrady