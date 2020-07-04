from tkinter import *
import tkinter

teclado = Tk()
teclado.title("Napster keyboard")
teclado['bg'] = 'powder blue'
teclado.resizable(0, 0)


def select(value):
    if value == ' Space ':
        entry.insert(tkinter.END, ' ')
    elif value == 'Tab':
        entry.insert(tkinter.END, '    ')
    else:
        entry.insert(tkinter.END, value)


label = Label(teclado, text="Teclado en pantalla", font=('arial', 30, 'bold'), bg='dark blue', fg='black')
label.grid(row=0, columnspan=16)

entry = Text(teclado, width=138, font=('arial', 12, 'bold'))
entry.grid(row=1, columnspan=40)

botones = [
    '!', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-', '7', '8', '9', '-',
    'Tab', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
    'SHIFT', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', 'SHIFT', '1', '2', '3', '/',
    ' Space '
]

var_fila = 3
var_column = 0

for boton in botones:
    command = lambda x=boton: select(x)

    if boton != " Space ":
        tkinter.Button(teclado, text=boton, width=5, bg='powder blue', fg='black', activebackground='white',
                       activeforeground='#000990',
                       relief='raised', padx=5, pady=3, bd=12, font=('arial', 10, 'bold'), command=command).grid(
            row=var_fila, column=var_column)

    if boton == " Space ":
        tkinter.Button(teclado, text=boton, width=118, bg='powder blue', fg='black', activebackground='white',
                       activeforeground='#000990',
                       relief='raised', pady=3, bd=12, font=('arial', 10, 'bold'), command=command).grid(
            row=6, columnspan=15)

    var_column += 1

    if var_column > 15 and var_fila == 3:
        var_column = 0
        var_fila += 1

    if var_column > 15 and var_fila == 4:
        var_column = 0
        var_fila += 1

teclado.mainloop()
