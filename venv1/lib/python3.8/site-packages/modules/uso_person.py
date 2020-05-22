import modules.modulo_persona as module_person


print("\n******************DATOS SUPERVISOR**********************")

miSupervisor = module_person.Supervisor("Juan", "Gonzalez", "Masculino")
miSupervisor.estado()
miSupervisor.objetivos()
miSupervisor.herencia()

print("\n*****************DATOS OBRERO***************************")

miObrero = module_person.Obrero("Juan", "Gonzalez", "Masculino")
miObrero.estado()
miObrero.manejar()
miObrero.herencia2()