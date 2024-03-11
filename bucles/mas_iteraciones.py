# Creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Lorenzo"
numeros = [2,5,8,10]

# evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f'Me voy a comer una: {fruta}')

#  evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f'Me voy a comer una: {fruta}')
    if fruta == "pera":
        break
else:
     print("terminado")

# recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)