print("PROGRAMA DE BECAS AL EXTRANJERO")

edad = int(input("Ingrese la edad del estudiante: "))
print(edad)

if edad >= 18:
    print("Usted cumple con el requisito de edad, ingrese su promedio ponderado")
    ponderado = float(input("Promedio ponderado: "))

    if ponderado >= 15.5:
        print("Su promedio cumple con los requisitos del programa")
        print("**************************************************")

        nro_cursos_aprobados = int(input("Ingrese el numero de cursos aprobados"))

        if nro_cursos_aprobados >= 36:
            print("La cantidad de cursos aprobados cumplen el requisito")
            print("**************************************************")

            salario_familiar = int(input("Ingrese el salario familia del estudiante: "))

            if salario_familiar <= 15000:
                print("Puede ingresar a al sistema de becas, cumple los requisitos del salario familiar")
            else:
                print("Si salario es mayor a 15000, por lo tanto no puede aplicar al programa")

        else:
            print("No cumple con el numero de cursos aprobados que es de 36")
    else:
        print("Su promedio no cumple con los requisitos del programa, debe ser mayor de 15.5")
else:
    print("Debe ser mayor de edad para postular.")