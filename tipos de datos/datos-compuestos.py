# un dato compuesto esta compuesto por otros datos, ya sean datos simples o compuestos 

# las listas si se pueden modificar, nos ayudan a agrupar datos, es un tipo de matriz
lista = ["Lorenzo Albornoz", "Lolo", True, 1.72]

# las tuplas no se pueden modificar
tupla = ("Lorenzo Albornoz", "Lolo", True, 1.72)

# esto es valido
lista[3] = "Maquinola"

# esto no es valido
#tupla[3] = "Maquinola"

#creando un conjunto (set), (no se puede acceder a cada uno de los elementos por un indice, no almacena datos duplicados)

conjunto = {"Lorenzo Albornoz", "Lolo", True, 1.72}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict) seria como el json de js, se accede a cada elemento por su nombre
diccionario = {
    'nombre': 'Lorenzo',
    'apellido': 'Albornoz',
    'edad': 29,
    'talla': 1.72
}

print(diccionario['apellido'])