from tkinter import *

root = Tk()

mi_frame = Frame(root)
root.geometry("350x460")
root.title("Napster calculator")
mi_label = Label(root, text="CALCULADORA", bg="white", font=("Terminator", 15, 'bold'))
mi_label.pack(side=TOP)
mi_label.config(background="Dark gray")

txt = StringVar()
operator = ""


def clicnum(number):
    global operator
    operator = operator + str(number)
    txt.set(operator)


def opbut():
    global operator
    add = str(eval(operator))
    txt.set(add)
    operator = ""


def clear():
    txt.set('')


text = Entry(root, font=("Courier sans", 12, 'bold'), width=25, bd=5, bg="powder blue", textvar=txt)
text.pack()

# Fila 1
btn1 = Button(root, padx=14, pady=14, bd=4, bg="white", text="1", font=("Courier new", 16, 'bold'), command=lambda: clicnum(1))
btn1.place(x=10, y=100)

btn4 = Button(root, padx=14, pady=14, bd=4, bg="white", text="4", font=("Courier new", 16, 'bold'), command=lambda: clicnum(4))
btn4.place(x=75, y=100)

btn7 = Button(root, padx=14, pady=14, bd=4, bg="white", text="7", font=("Courier new", 16, 'bold'), command=lambda: clicnum(7))
btn7.place(x=140, y=100)

btn_plus = Button(root, padx=14, pady=14, bd=4, bg="white", text="+", font=("Courier new", 16, 'bold'), command=lambda: clicnum("+"))
btn_plus.place(x=205, y=100)

# Fila 2
btn2 = Button(root, padx=14, pady=14, bd=4, bg="white", text="2", font=("Courier new", 16, 'bold'), command=lambda: clicnum(2))
btn2.place(x=10, y=170)

btn5 = Button(root, padx=14, pady=14, bd=4, bg="white", text="5", font=("Courier new", 16, 'bold'), command=lambda: clicnum(5))
btn5.place(x=75, y=170)

btn8 = Button(root, padx=14, pady=14, bd=4, bg="white", text="8", font=("Courier new", 16, 'bold'), command=lambda: clicnum(8))
btn8.place(x=140, y=170)

btn_minus = Button(root, padx=14, pady=14, bd=4, bg="white", text="-", font=("Courier new", 16, 'bold'), command=lambda: clicnum("-"))
btn_minus.place(x=205, y=170)

# Fila 3
btn3 = Button(root, padx=14, pady=14, bd=4, bg="white", text="3", font=("Courier new", 16, 'bold'), command=lambda: clicnum(3))
btn3.place(x=10, y=240)

btn6 = Button(root, padx=14, pady=14, bd=4, bg="white", text="6", font=("Courier new", 16, 'bold'), command=lambda: clicnum(6))
btn6.place(x=75, y=240)

btn9 = Button(root, padx=14, pady=14, bd=4, bg="white", text="9", font=("Courier new", 16, 'bold'), command=lambda: clicnum(9))
btn9.place(x=140, y=240)

btn_multiply = Button(root, padx=14, pady=14, bd=4, bg="white", text="x", font=("Courier new", 16, 'bold'), command=lambda: clicnum("*"))
btn_multiply.place(x=205, y=240)

# Fila 4
btn0 = Button(root, padx=14, pady=14, bd=4, bg="white", text="0", font=("Courier new", 16, 'bold'), command=lambda: clicnum(0))
btn0.place(x=10, y=310)

btn_point = Button(root, padx=47, pady=14, bd=4, bg="white", text=".", font=("Courier new", 16, 'bold'), command=lambda: clicnum("."))
btn_point.place(x=75, y=310)

btn_div = Button(root, padx=14, pady=14, bd=4, bg="white", text="/", font=("Courier new", 16, 'bold'), command=lambda: clicnum("/"))
btn_div.place(x=205, y=310)

# Parte 5
btn_ce = Button(root, padx=14, pady=119, bd=4, bg="white", text="CE", font=("Courier new", 16, 'bold'), command=clear)
btn_ce.place(x=270, y=100)

btn_equal = Button(root, padx=151, pady=14, bd=4, bg="white", text="=", font=("Courier new", 16, 'bold'), command=opbut)
btn_equal.place(x=10, y=380)

root.mainloop()