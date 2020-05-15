# Diccionarios


dic1 = {"Juan": "Ingeniero", "Jose": "Medico", "Maria": "Abogado", 55: 99, "Javier": 88}
print(dic1)
print(dic1["Jose"])  # Buscar por posicion el valor del parametro


# Combinamos lista con diccionario
lis = ["Lenovo", "Dell", "Sony", "Samsung"]
dict_combinar = {lis[0]:"laptop", lis[1]:"All in one", lis[2]:"Equipo", lis[3]:"PC"}
print(dict_combinar)
print(dict_combinar["Dell"])


#Combinar tupla con diccionario
tup = "Lenovo", "Dell", "Sony", "Samsung"
dict_combinar2 = {tup[0]:"laptop", tup[1]:"All in one", tup[2]:"Equipo", tup[3]:"PC"}
print(dict_combinar2)