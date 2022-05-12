from ast import Expression
from cgitb import text
from tkinter import *
from tkinter import font
from tkinter.font import *
from tokenize import String


gui = Tk()
gui.configure(background="red")
gui.title("calculator")
gui.geometry("2048x1024")

lbl = Label(gui,text="bonjour tous le monde",bg="red")
lbl.place(x=0,y=0)


lbl = LabelFrame(gui,text="fghjgkfgh",bg="blue",height=500,width=500)
lbl.place(x=100,y=200)

lbl2 = LabelFrame(gui,text="fghjgkfgh",bg="purple",height=200,width=300)
lbl2.place(x=600,y=500)

button1=Button(lbl,bg='dark blue',height=3,width=5,highlightbackground="green")
button1.place(x=10,y=10)


"""expression =""

def press(num):
    global expression
    expression= expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    total= str(eval(expression))
    equation.set(total)
    expression

def clear():
    global expression
    expression=""
    equation.set("")


equation=StringVar()
#font= Font(family='Helvetica', style=20,weight='bold')

expression_fiel=Entry(gui, textvariable=equation)
#expression_fiel['font'] = font
expression_fiel.grid(row=0, column=4, ipady=30,ipadx=80)

button1=Button(gui,text='1', fg='write',bg='dark blue', command=lambda: press(1),height=3,widht=14)
#button1['font']= font
button1.grid(row=2,column=0)

button2=Button(gui,text='2', fg='write',bg='dark blue', command=lambda: press(2),height=3,widht=14)
#button2['font']= font
button2.grid(row=2,column=1)

button3=Button(gui,text='3', fg='write',bg='dark blue', command=lambda: press(3),height=3,widht=14)
#button3['font']= font
button3.grid(row=2,column=2)

button4=Button(gui,text='4', fg='write',bg='dark blue', command=lambda: press(4),height=3,widht=14)
#button4['font']= font
button4.grid(row=3,column=0)

button5=Button(gui,text='5', fg='write',bg='dark blue', command=lambda: press(5),height=3,widht=14)
#button5['font']= font
button5.grid(row=3,column=1)

button6=Button(gui,text='6', fg='write',bg='dark blue', command=lambda: press(6),height=3,widht=14)
#button6['font']= font
button6.grid(row=3,column=2)

button7=Button(gui,text='7', fg='write',bg='dark blue', command=lambda: press(7),height=3,widht=14)
#button7['font']= font
button7.grid(row=4,column=0)

button8=Button(gui,text='8', fg='write',bg='dark blue', command=lambda: press(8),height=3,widht=14)
#button8['font']= font
button8.grid(row=4,column=1)

button9=Button(gui,text='9', fg='write',bg='dark blue', command=lambda: press(9),height=3,widht=14)
#button9['font']= font
button9.grid(row=4,column=2)

plus=Button(gui,text='+', fg='write',bg='dark blue', command=lambda: press('+'),height=3,widht=14)
#plus['font']= font
plus.grid(row=2,column=3)

minus=Button(gui,text='-', fg='write',bg='dark blue', command=lambda: press('-'),height=3,widht=14)
#minus['font']= font
minus.grid(row=3,column=3)

multiply = Button(gui,text='*',fg='write',bg='dark blue', command=lambda: press('*'),height=3,widht=14)
#multiply['font']= font
multiply.grid(row=4,column=3)

divide = Button(gui, text='/' ,fg='write',bg='dark blue', command=lambda: press('/'),height=3,widht=14)
#divide['font']=font
divide.grid(row=5, column=3)

equal = Button(gui, text='=' ,fg='write',bg='dark blue', command=lambda: press('='),height=3,widht=14)
#equal['font']=font
equal.grid(row=5, column=2)

point = Button(gui, text='.' ,fg='write',bg='dark blue', command=lambda: press('.'),height=3,widht=14)
#point['font']=font
point.grid(row=6, column=0)"""


gui.mainloop()


