from tkinter import *

main = Tk()

main.title("Napster computing")
main.resizable(True, False)
main.geometry("720x480")

# Asignar icono de ventana
# icon = PhotoImage(file="user_interface/napster_logotype.ico")
# main.tk.call('wm', 'iconphoto', main._w, icon)
main.config(bg='black')

# ************************************FRAME******************************************

mi_frame = Frame()
mi_frame.pack(side="left", anchor="n", fill="x", expand=True)
mi_frame.config(width="420", height="210", bg="blue", bd=5, relief="groove")

# Creacion de la ventana
main.mainloop()