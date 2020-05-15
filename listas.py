a = ["Juan", "Jose", "Carlos",  "Ernesto", "Maria", "Ana"]
b = [1,2,3,4,5,6,7,8,9]

a.insert(4, "Nicole") #Insertar valor en la posicion indicada
a.append("Ricardo") #Insertar al final de la lista
a.extend(["Javier", "Carlos", "Sara", "Karina", "Raul"]) #Insertar muchos elementos al final
a.remove("Carlos") #Remover valor de la lista

print(a)
print(a[1:4])
print(b)