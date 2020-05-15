# Funcion sin parametros
def mensajes():
    print("Este es el primer ejemplo")
    print("Este es el segundo mensaje")


mensajes()


def operaciones_basicas():
    a = 12
    b = 7
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)


operaciones_basicas()


#Operaciones con parametros
def operaciones_basicas_parametros(a, b):
    print(a*b)
    print(a+b)
    print(a-b)
    print(a/b)


operaciones_basicas_parametros(6,7)


def operaciones_basicas_return(x,y):
    suma = x + y
    return suma


suma = operaciones_basicas_return(4,5)
print(suma)