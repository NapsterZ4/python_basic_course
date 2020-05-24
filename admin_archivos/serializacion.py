import pickle

carreras = ["Ingenieria de sistemas", "Medicina", "Astrofisica", "Administracion", "Matematicas", "Arquitectura"]
fichero = open("carreras", "wb")  # Permiso de escritura en binario
pickle.dump(carreras, fichero)

lectura = open("carreras", "rb")
lista = pickle.load(lectura)
print(lista)