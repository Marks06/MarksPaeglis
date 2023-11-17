#mērķis ir uztaisīt programmu , kurā zemūdene spridzina burbuļus
#tiek skaitīti punkti
from tkinter import *
from random import *
from math import *
logs = Tk()
garums = 700
platums = 700
logs.title('Burbuļu spridzinātājs')
a = Canvas(logs, width=platums,height=garums,bg='lightgreen')
a.pack()
kuga_id2 = a.create_oval(10,10,100,100,fill='lightblue',outline='darkgreen', width=8)


mainloop()