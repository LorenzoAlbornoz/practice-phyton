numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

# Una forma de crear una funcion anonima
multiplicar_por_dos = lambda x : x*2

# Creando una funcion comun que diga si es par o no
# def es_par(num):
#     if(num%2==0):
#         return True

#  Usando filter con una funcion comun
# numeros_pares = filter(es_par,numeros)

# Creando lo mismo que antes pero con lambda

numeros_pares = filter(lambda numero:numero%2 == 0,numeros)

print(list(numeros_pares))