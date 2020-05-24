import pickle


class Computadora():

    def __init__(self, marca, procesador, mouse, teclado):
        self.marca = marca
        self.procesador = procesador
        self.mouse = mouse
        self.teclado = teclado

        print("Se ha creado un nuevo ordenador de marca", self.marca)

    # Convertir en cadena de texto
    def __str__(self):
        return "{} {} {} {}".format(self.marca, self.procesador, self.mouse, self.teclado)


class ListaPcs():

    pcs = []

    def __init__(self):
        lista_pcs = open("Ordenadores", "ab+")  # --> Agregar informacion binaria
        lista_pcs.seek(0)

        try:
            self.pcs = pickle.load(lista_pcs)
            print("Se cargaron {} numero de computadora en el fichero externo".format(len(self.pcs)))

        except:
            print("El fichero no contiene nada")

        finally:
            lista_pcs.close()
            del lista_pcs

    def agregar_pcs(self, pc):
        self.pcs.append(pc)

    def mostrar_pcs(self):
        for pc in self.pcs:
            print(pc)

    def guardar_pcs(self):
        lista_pcs = open("Ordenadores", "wb")
        pickle.dump(self.pcs, ListaPcs)  # Le enviamos la clase que contiene el constructor con lista_pcs
        lista_pcs.close()
        del lista_pcs

    def mostrar_fichero_ext(self):
        print("La informacion del fichero externo es: ")
        for pc in self.pcs:
            print(pc)


mi_pc = ListaPcs()
pc = Computadora("Lenovo", "Intel i3", "Microsoft", "Dell")
mi_pc.agregar_pcs(pc)

mi_pc.mostrar_fichero_ext()