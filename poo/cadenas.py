# cadena = input("Ingrese una cadena de caracteres: ")
#
# print("La cadena minuscula: ", cadena.lower())
# print("La cadena mayuscula: ", cadena.upper())
# print("La cadena capital: ", cadena.capitalize())


edad = input("Ingrese la edad: ")

while not edad.isdigit():

    edad = input("Ingrese la edad en numeros: ")
    if int(edad) < 18:
        print("Usted no puede ingresar al evento")
    else:
        print("Puede ingresar al evento")
