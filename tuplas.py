# listas que no pueden modificarse

a = (1, 4, 5.6, "Juan", 6, "Maria")
b = ["Jorge", 5, "Peru", 90]
tup2 = 34, "Javier", 9.6, "Murillo"

c = tuple(b)  # Convirtiendo la lista en tupla
d = list(a)  # Conviertiendo la tupla en una lista

print(tup2)
print(a)
print(c)  # Resultado de la lista convertida en tupla
print(d)  # Resultado de la tupla convertida en lista
print("Elementos de la tupla: ", len(a))  # Contar elementos de la tupla
print("Posicion de un elemento en la tupla: ", d[4])
