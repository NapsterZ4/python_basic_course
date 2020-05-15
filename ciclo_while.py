a = 1

while a < 7:
    print(a)
    a = a + 1

print("Programa ejecutado correctamente")


edad = int(input("Ingrese una edad: "))

while edad < 18 or edad > 70:
    print("Aun no estas apto para realizar la accion")
    edad = int(input("Ingrese una edad nuevamente: "))

print("Gracias por realizar la transaccion")

