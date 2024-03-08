#creando un conjunto con set()

conjunto = set(["Dato 1"])

conjunto2 = set(["Dato1", ("datoenlista1", "datoenlista2")])

#metiendo un conjunto dentro de otro conjunto
conjunto3 = frozenset(["dato 1", "dato 2"])
conjunto4 = {conjunto3, "dato 3"}
print(conjunto4)

# teoria de conjuntos
# subconjunto 
conjunto1= {1,3,5,7}
conjunto2= {1,3,7}

resultado = conjunto2.issubset(conjunto1)
resultado2= conjunto2 <= conjunto1
print(resultado)

# superconjunto
resultado3 = conjunto1.issuperset(conjunto2)
resultado4= conjunto2 < conjunto1

print(resultado3)

#verificar si hay algun resultado en comun
resultado5 = conjunto2.isdisjoint(conjunto1)
print(resultado5)