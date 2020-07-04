from tkinter import *

root = Tk()
mi_nombre = StringVar()
mi_apellido = StringVar()
mi_password = StringVar()
mi_direccion = StringVar()

# *********************************LABELS******************************************
mi_frame = Frame(root, width=1200, height=680)
mi_frame.pack()
Label(mi_frame, text="Hello World", fg="blue", font=("Arial Black", 28)).place(x=100, y=150)

lbl_nombre = Label(mi_frame, text="Nombre:")
lbl_nombre.grid(row=0, column=0, sticky="w", pady=5)

lbl_apellido = Label(mi_frame, text="Apellido:")
lbl_apellido.grid(row=1, column=0, sticky="w", pady=5)

lbl_password = Label(mi_frame, text="Contraseña:")
lbl_password.grid(row=2, column=0, sticky="w", pady=5)

lbl_direccion = Label(mi_frame, text="Dirección:")
lbl_direccion.grid(row=3, column=0, sticky="w", pady=5)

lbl_comentario = Label(mi_frame, text="Comentario:")
lbl_comentario.grid(row=4, column=0, sticky="w", padx=5, pady=5)
# *********************************ENTRY******************************************

txt_nombre = Entry(mi_frame, textvariable=mi_nombre)
txt_nombre.grid(row=0, column=1, padx=5, pady=5)
txt_nombre.config(fg="blue", justify="left")

txt_apellido = Entry(mi_frame, textvariable=mi_apellido)
txt_apellido.grid(row=1, column=1)
txt_apellido.config(fg="blue", justify="left")

txt_password = Entry(mi_frame, textvariable=mi_password)
txt_password.grid(row=2, column=1)
txt_password.config(show="*")

txt_direccion = Entry(mi_frame, textvariable=mi_direccion)
txt_direccion.grid(row=3, column=1)
txt_direccion.config(fg="blue", justify="left")

# **********************************TEXT*******************************************
txt_comentario = Text(mi_frame, width=40, height=5)
txt_comentario.grid(row=4, column=1, padx=5, pady=5)

# *********************************SCROLLBAR***************************************
scroll_bar = Scrollbar(mi_frame, command=txt_comentario.yview)
scroll_bar.grid(row=4, column=2, sticky="nsew")
txt_comentario.config(yscrollcommand=scroll_bar.set)

# *******************************BUTTON**************************************


def cmd_btn_enviar():
    mi_nombre.set("Jorge")
    mi_apellido.set("Godoy")
    mi_password.set("universitario")
    mi_direccion.set("Rohrmoser")


button_enviar = Button(root, text="Enviar", command=cmd_btn_enviar())
button_enviar.pack()

root.mainloop()