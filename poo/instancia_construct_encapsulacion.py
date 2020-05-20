class Computadora():

    def __init__(self):
        self.__ejecutar = None
        self.__marca = "Toshiba"
        self.__procesador = "Intel"
        self.__mouse = 1
        self.__teclado = 1

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
        print(self.__marca, self.__procesador, self.__mouse, self.__teclado)


pc = Computadora()

print(pc.ejecucion(True))
print(pc.estado())

print("*************************************************")

pc2 = Computadora()
pc2.teclado = 2

print(pc2.ejecucion(False))
print(pc2.estado())