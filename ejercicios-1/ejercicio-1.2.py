frase = input('Decime una frase y te calculo cuando tardarias si tuvieras que decirla: ')
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlos')
print(f'Dalton lo diria en {cantidad_de_palabras * 100 // 2 *1.3 / 100} segundos')
if cantidad_de_palabras > 120:
    print("Te excediste de la cantidad de palabras")