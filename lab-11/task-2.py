#Canvas модулін (оның ішінде Tkinter) қолданып, әр студент өз атын өрнектеп  логотип жасап келсін

from tkinter import *
root = Tk()

c = Canvas(root, width=1000, height=500, bg='white')
c.pack()

#Ж
c.create_rectangle(60, 80, 80, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(80, 130, 100, 150,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(100, 80, 120, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(120, 130, 140, 150,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(140, 80, 160, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))

#a
c.create_oval(180, 100, 280, 200, fill='yellow',
                   outline='green', width=2)
c.create_rectangle(270, 100, 290, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))

#н
c.create_rectangle(310, 100, 330, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(330, 140, 350, 160,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(350, 100, 370, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))

#E
c.create_rectangle(390, 100, 410, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(410, 100, 450, 120,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(410, 140, 450, 160,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(410, 180, 450, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
#P
c.create_oval(470, 100, 550, 170, fill='yellow',
                   outline='green', width=2)
c.create_rectangle(470, 100, 490, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))

#K
c.create_line(580, 150, 640, 105,
              width=20,
              fill='yellow')
c.create_line(580, 150, 640, 195,
              width=20,
              fill='yellow')
c.create_rectangle(570, 100, 590, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))

#E
c.create_rectangle(660, 100, 680, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(680, 100, 720, 120,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(680, 140, 720, 160,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
c.create_rectangle(680, 180, 720, 200,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))

root.mainloop()














