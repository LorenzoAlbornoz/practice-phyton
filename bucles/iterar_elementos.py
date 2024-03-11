# For in 
animales = {"perro", "gato", "loro", "cocodrilo"}
numeros = {52, 16, 14, 72}

# Recorriendo el conjuto animales
for animal in animales:
    print(f'ahora la variable animas es igual a: {animal}')

# Recorriendo el conjuto numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

# Recorriendo dos conjutos del mismo tamaño al mismo tiempo
for numero, animal in zip(animales,numeros):
    print(f"Recorriendo conjuto 1: {numero}")
    print(f"Recorriendo conjuto 2: {animal}")

# Forma correcta de recorrer un conjuto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

# Usando el for/else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")

# Todo lo anterior funciona exactamente igual para tuplas y conjutos