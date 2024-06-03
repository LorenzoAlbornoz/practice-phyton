diccionario = {
    "nombre": "Lorenzo",
    "apellido": "Albornoz",
    "subs": 1000000
}

#keys() devuelve las claves (tambien nos sirve para iterar)
claves = diccionario.keys()

#get() devuelve el valo de una clave (si no encuenta nada el programa continua)
valor_nombre = diccionario.get('nombre')

#clear() elimina todos los elementos
# diccionario.clear()

#pop() elimina un elemento del diccionario (por su clave)
diccionario.pop('subs')

#items() para iterar el diccionario
diccionario_iterable = diccionario.items()

print(diccionario_iterable)