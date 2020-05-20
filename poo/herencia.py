class Persona():

    def __init__(self, nombre, apellido, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

        self.hablar = False

    def hablar(self):
        self.hablar = True

    def estado(self):
        print("\nNombre: ", self.nombre,
              "\nApellido: ", self.apellido,
              "\nSexo: ", self.sexo,
              "\nHablar: ", self.hablar)


class Supervisor(Persona):
    objetivo = ""

    def objetivos(self):
        self.objetivo = "Tiene que cumplir con las metas mensuales"

    def herencia(self):
        print("\nObjetivo: ", self.objetivo)


class Obrero(Persona):
    manejarMaq = ""

    def manejar(self):
        self.manejarMaq = "Tiene que descargar 80 containers al mes."

    def herencia2(self):
        print("\nMaquinaria: ", self.manejarMaq)


print("\n******************DATOS SUPERVISOR**********************")

miSupervisor = Supervisor("Juan", "Gonzalez", "Masculino")
miSupervisor.estado()
miSupervisor.objetivos()
miSupervisor.herencia()

print("\n*****************DATOS OBRERO***************************")

miObrero = Obrero("Juan", "Gonzalez", "Masculino")
miObrero.estado()
miObrero.manejar()
miObrero.herencia2()