class Persona():

    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def estado(self):
        print("Nombre: ", self.nombre,
              "\nEdad: ", self.edad,
              "\nResidencia: ", self.residencia)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre, edad, residencia):

        super().__init__(nombre=nombre, edad=edad, residencia=residencia)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().estado()
        print("Salario: ", self.salario,
              "\nAntiguedad: ", self.antiguedad)


emp = Empleado(3000, 5, "Juan", 23, "Peru")
emp.descripcion()

print(isinstance(emp, Empleado))