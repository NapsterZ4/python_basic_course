def suma(n1, n2, n3) -> int:
    return n1 + n2 + n3


def resta(n1, n2, n3) -> int:
    return n1 - n2 - n3


def multiplicacion(n1, n2, n3) -> int:
    return n1 * n2 * n3


def division(n1, n2, n3):
    # Validar division entre 0
    try:
        return n1 / n2 / n3
    except ZeroDivisionError:
        print("No es divisible entre 0")

while True:
    try:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        c = int(input("Ingrese el tercer numero: "))

        operacion = int(input("Introduce el numero de operacion "
                              " 1. Suma"
                              " 2. Resta"
                              " 3. Multiplicacion"
                              " 4. Division: "))
        break
    except ValueError:
        print("Ingrese datos validos")

if operacion == 1:
    print("La suma es: ", suma(a, b, c))
elif operacion == 2:
    print("La resta es: ", resta(a, b, c))
elif operacion == 3:
    print("La multiplicacion es: ", multiplicacion(a, b, c))
elif operacion == 4:
    print("La division es: ", division(a, b, c))
else:
    print("La operacion no fue realizada con exito, ingrese un numero entre 1 y 4")
