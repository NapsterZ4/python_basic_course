class carro():
    # Atributos
    marca = "Audi"
    longitud = 2.5
    ruedas = 4
    motor = 2.5
    color = "negro"
    modelo = "q5"

    # Propiedades
    arrancar = True
    frenar = False

    # Instancias y metodos --> nombre_instancia = clase()

    def enmarcha(self):
        self.arrancar = False

    def estado(self):
        if self.arrancar:
            print("El auto esta detenido")
        else:
            print("El auto esta en arranque")


auto = carro()
print("La marca del carro es: ", auto.marca)

auto.estado()