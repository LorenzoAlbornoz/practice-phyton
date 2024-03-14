# Creando una funcion de 3 parametros 
# def frase(nombre,apellido,adjetivo):
#     return f"Hola {nombre} {apellido}, soy muy {adjetivo}"

# Utilizando keyword argumentos
# frase_resultado = frase(adjetivo="capo", nombre= "Lorenzo",apellido = "Albornoz")
# print(frase_resultado)

# Creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, soy muy {adjetivo}"

frase_resultado = frase("Lorenzo", "Albornoz", "inteligente")
print(frase_resultado)