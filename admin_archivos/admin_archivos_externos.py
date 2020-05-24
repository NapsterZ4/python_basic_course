from io import open

# Escribir en ficheros
archivo = open("fichero01.txt", "w")
frase = "Feliz cumpleanos Juan Carlos!. \nSu cumple es hoy"
archivo.write(frase)
archivo.close()

# Leer ficheros
archivo2 = open("fichero01.txt", "r")
print(archivo2.read(15))
archivo2.seek(1)  # Imprime despues de una posicion
print(archivo2.read())
texto = archivo2.read()
print(texto)

# Lectura desde el parrafo final
archivo2.seek(len(archivo2.readline()))
print(archivo2.read())
archivo2.close()

# Agregar filas al archivo
archivo3 = open("fichero01.txt", "a")
texto2 = archivo3.write("\n Hay que felicitarlo!")
archivo3.close()

# Transformacion a lista
archivo4 = open("fichero01.txt", "r")
lineas_texto = archivo4.readlines()
archivo4.close()
print(lineas_texto[1])
