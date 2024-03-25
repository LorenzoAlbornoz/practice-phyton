# Creando una funcion simple
# def saludar():
# Ejecutando la funcion simpre
    # print("Hola Lorenzo")

# Crear una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = 'amor'
    

    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")

saludar("Lorenzo", "hombre")
saludar("Belen", "mujer")
saludar("Carlos", "no binario")

# Crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    # convertimos a num en una cadena de texto
    num_entero = str(num)
    # convertimos a entero y obtenemos el primer numero
    num = int (num_entero[0])
    # calculamos 3 indices
    c1 = num - 2
    c2 = num
    c3 = num - 5
    # Concatenamos los caracteres seleccionados
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num

password,primer_numero = crear_contraseña_random(981)
# Mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El número utilizado para crearla fue: {primer_numero}")
