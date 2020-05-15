def evaluacion(nota):
    estado = "Promovido"

    if nota < 11:
        estado = "Sustitutorio"
    return estado


print('Calificacion del primer semestre')
nota = int(input('Ingrese la nota: '))
print(evaluacion(nota))