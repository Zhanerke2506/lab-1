#Math, random, datetime, Canvas модульдерін қолданып әр модульден 5  функцияны қолданып бағдарлама жазу.

import math
import random
import datetime
from tkinter import *
from turtle import *


#math and random


a = random.randint(10, 20) #случайное целое число N
b = random.random() #случайное число от 0 до 1
c = random.uniform(0, 1) #случайное число с плавающей точкой
d = random.paretovariate(10.5) #распределение Парето
e = random.gauss(20.5, 5.5) #распределение Гаусса

y = math.sqrt(math.pow(a, 2) + math.pow(b, 2) - 2 * a * b * math.cos(c)) #a^2+b^2-ab*cos(c);
x = math.fabs(1 - math.fabs(y)) #|1-|y||

s = math.fabs(math.sin(x) * math.cos(y) + math.cos(x) * math.sin(y)) + 1

z = math.log(d, e)

print(s)
print(z)
print(math.ceil(s)) #округление до ближайшего большего числа.
print(math.trunc(s)) #усекает значение до целого.

#datetime
print("Today is ", datetime.datetime.now())

a = int(input("Күн:"))
b = datetime.datetime.today()
c = datetime.timedelta(days=a)
d = b + c
print(a, "күн өткеннен кейін:", d)

second = datetime.date(2022, 12, 19)
answer = second - datetime.date.today()
print("Сессияға дейін: ", answer)

print(datetime.date(2022, 12, 29).isocalendar())
print(datetime.date.fromisocalendar(2022, 52, 4)) #Возвратите a date соответствуя календарной дате ISO, указанной годом, неделей и днем.

print(datetime.date(2022, 11, 21).ctime())

#canvas
#tkinter
root = Tk()
c = Canvas(width=300, height=300,
           bg='white')
c.focus_set()
c.pack()

points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
ball = c.create_polygon(points, outline='green', fill='red', width=2)

c.bind('<Up>',
       lambda event: c.move(ball, 0, -2))
c.bind('<Down>',
       lambda event: c.move(ball, 0, 2))
c.bind('<Left>',
       lambda event: c.move(ball, -2, 0))
c.bind('<Right>',
       lambda event: c.move(ball, 2, 0))

root.mainloop()
#turtle
color("purple")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

color("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

color("blue")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

color("purple")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

color("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

color("purple")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

color("blue")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()