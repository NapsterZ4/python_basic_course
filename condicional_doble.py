sueldo_gerente = int(input("Ingrese el salario del gerente general: "))
sueldo_jefe_area = int(input("Ingrese el salario del jefe de area: "))
sueldo_asistente = int(input("Ingrese el salario del jefe de area: "))
sueldo_tecnico = int(input("Ingrese el salario del tecnico: "))
sueldo_practicante = int(input("Ingrese el salario del practicante: "))

if sueldo_gerente > sueldo_jefe_area > sueldo_asistente > sueldo_tecnico > sueldo_practicante:
    print("Cumple una estructura jerarquica")
else:
    print("Fallas en el sistema de pagos")