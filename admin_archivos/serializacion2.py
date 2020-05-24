import pickle


class Computadora():

    def __init__(self, __marca, __procesador, __mouse, __teclado):
        self.__ejecutar = None
        self.__marca = __marca
        self.__procesador = __procesador
        self.__mouse = __mouse
        self.__teclado = __teclado

        self.__suspendido = False

    def ejecucion(self, ejecucion):
        self.__suspendido = ejecucion

        if self.__ejecutar:
            update = self.__actualizacion_automatica()

        if self.__ejecutar and update:
            print("El equipo esta suspendido.")

        if self.__suspendido:
            print("El equipo esta suspendido.")
        else:
            print("El equipo esta en ejecucion.")

    def __actualizacion_automatica(self):
        print("El equipo se esta actualizando.")

        self.servupdate = "Activado"

        if self.servupdate == "Activado":
            return True
        else:
            return False

    def estado(self):
        print("La marca es:", self.__marca, "Procesador:", self.__procesador, "Mouse:", self.__mouse, "Teclado:", self.__teclado)


pc1 = Computadora("Toshiba", "AMD", "HP", "Genius")
pc2 = Computadora("Lenovo", "Intel i3", "Genius", "Microsoft")
pc3 = Computadora("Sony Vaio", "Core i7", "Lenovo", "HP")

pc = [pc1, pc2, pc3]

fichero = open("Equipo TI", "wb")
pickle.dump(pc, fichero)
fichero.close()
del fichero  # Elimina el fichero en memoria


archivo = open("Equipo TI", "rb")
lista = pickle.load(archivo)
archivo.close()

for c in lista:
    print(c.estado())