# metodos que podemos aplicar a listas para operarlas

#LIST - Crea una lista. es una funcion, no un metodo

lista = list([40, 55, 29])

#LEN - Cuenta la cantidad de elementos de una lista
resultado = len(lista)

#APPEND - Agrega un elemento a la lista
lista.append(65)

#INSERT - Agrega un elemento a la lista en el indice especificado
lista.insert(2, "TOMA MAMA")

#EXTEND - Agrega varios elementos a la lista
lista.extend([False, 2030])

#POP - Elimina un elemento de una lista, pide indice y devuelve valor
lista.pop(0) #-1 para eliminar el utimo, -2 para eliminar el anteultimo, y asi sucesivamente

#REMOVE - Remueve un elemento de una lista, pide valor
lista.remove("TOMA MAMA")

#SORT - Ordena una lista de forma ascendente a descendente
lista.sort() #solo funciona con numeros, tambien aqui se puede usar reverse

#REVERSE - Invierte los elementos de una lista
lista.reverse()

# #CLEAR - Elimina todos los elementos de una lista
# lista.clear()

elemento_encontrado = lista.index(55)
print(elemento_encontrado)

#con las tuplas solo podemos buscar elementos y contarlos