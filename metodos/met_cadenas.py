#Los metodos son funciones aplicadas a objetos

cadena1 = "Hola soy Lorenzo"
cadena2= "Bienvenido!"

#DIR - Devuelve la lista de atributos válidos del objeto pasado. Es una funcion, no un metodo

#UPPER - Convierte a mayuscula
resultado = cadena1.upper()

#LOWER - Convierte a minuscula
resultado2 = cadena1.lower()

#CAPITALIZE - Primera en mayuscula
resultado3 = cadena1.capitalize()

#FIND - Método encuentra la primera aparición del valor especificado de una cadena dentro de una cadena
#devuelve el caracter donde se encuentra la coincidencia, sino devuelve -1
resultado4 = cadena1.find("Hola")

#INDEX - Método encuentra la primera aparición del valor expecificado de una cadena dentro de una cadena
#devuelve el caracter donde se encuentra la coincidencia, sino devuelve una excepción
resultado5 = cadena1.index("Hola")

#ISNUMERIC - Si es numerico devuelve true
es_numerico = cadena1.isnumeric()

#ISALPHA - Si es alfa numérico devuelve true. Los espacios no son alfa numericos
es_alfa_numerico = cadena1.isalpha()

#COUNT - Devuelve coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
resultado6 = cadena1.count("o")

#LEN - Cuenta los caracteres de una cadena. es una funcion, no un metodo
resultado7 = len(cadena1)

#ENDSWITH - Verifica si una cadena comienza con
resultado8 = cadena1.endswith("o")

#STARTSWITH - Verifica si una cadena termina con
resultado9 = cadena1.startswith("H")

#REPLACE - Remplaza un valor de la cadena dada por otro
resultado10 = cadena1.replace("la", "lu")

#SPLIT - Separa por el parametro dado. nos devuelve una matriz o lista
resultado11= cadena1.split(",")
print(resultado11)