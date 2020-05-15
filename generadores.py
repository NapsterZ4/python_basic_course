# Ejemplo con funciones

def dispares(limite):
    num = 1
    mi_lista = []

    while num < limite:
        mi_lista.append(num * 2)
        num = num + 1

    return mi_lista


print(dispares(8))

# Ejemplo con generadores y reemplaza la lista


def dispares(limite):
    num = 1

    while num < limite:
        yield num * 2
        num = num + 1


pares = dispares(8)

for i in pares:
    print(i)


# Elementos especificos
print(next(pares))
print("puede ingresar aqui....")
