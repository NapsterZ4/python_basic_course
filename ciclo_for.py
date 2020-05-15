print("inicio")

for a in [1, 2, 3, 4, 5, 6]:
    print("Hola Mundo")

print("fin")

print("Inicio 2")

for a in ["Juan", "Melisa", "Gabriel", 12.5, 23]:
    print(f"Hola, soy {a}")

print("Inicio 3")

cont = 0

for a in "napster":
    if a == "napster":
        cont = cont + 1

    if cont == 2:
        print("El email esta correcto")
    else:
        print("No cumple con los parametros establecidos")

print("Inicio 3")

for i in range(10):
    print(f"Hola Mundo.{i}")

print("Inicio 4")

for i in range(7, 0, -2):
    print(i)
