class Gerente():

    def marcacion(self):
        print("Marca asistencia solo una vez al dia")


class Subgerente():

    def marcacion(self):
        print("Marca asistencia solo dos veces al dia")


class Jefearea():

    def marcacion(self):
        print("Marca asistencia solo cuatro veces al dia")


class Asistente():

    def marcacion(self):
        print("Marca asistencia solo 4 veces al dia y firma en el padron")


def marcacionTrabajador(trabajador):
    trabajador.marcacion()


mTrabajador = Subgerente()
marcacionTrabajador(mTrabajador)