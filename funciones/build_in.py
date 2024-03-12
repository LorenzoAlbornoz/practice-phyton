# Una funcion es un fragmento de codigo que podemos utilizar 
# reutilizar en cualqueir otro momento sin necesidad de escribir de nuevo esa funcion
numeros = [4,7,1,42,15]

# Encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# Encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondeando a 6 decimales
numero = round(12.345678,2)

# Retorna False -> 0, vacio, False, None \ True -> distinto a 0, true, cadena, datos no vacios
resultado = bool(None)

# Retorna True, si todos los valores son verdaderos
resultado_all = all([234,"true",[344,23]])

# Suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)