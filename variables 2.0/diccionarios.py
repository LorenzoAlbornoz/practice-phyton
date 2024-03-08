#creando diccionarios con dict()
diccionario = dict(nombre="lucas", apelllido="dalto")

#las listas no pueden ser claves porque son mutables y usamos frozenset para meter conjuntos
diccionario= {("dalto", "rancio"): "jajas"}

#creando diccionarios con fronkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

#creando diccionarios con fronkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")
print(diccionario)