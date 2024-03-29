# promedio de duracion
otros_cursos_min = 2.5 
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duracion

diferenia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferenia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferenia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calculando el porcentaje de tiempo vacio 
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#Mostrando las diferencias de duración (ejercicio A)
print('-----------------')
print('El curso de dalto dura:')
print(f' - un {diferenia_con_min}% menos que el más rapido')
print(f' - un {diferenia_con_max}% menos que el más lento')
print(f' - un {diferenia_con_promedio}% menos que el promedio')
print('-----------------')

#Mostrando la cantidad de espacios vacios que se remueben (ejercicio B)
print(f' - El curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f' - El curso elimino un {tiempo_vacio_dalto}% de tiempo vacio')
print('-----------------')

#Mostrando diferencia si los cursos duraran 10 horas (ejercicio C)
print(f' - Ver 10 horas de este curso equivale a ver {otros_cursos_promedio *100 // dalto_curso / 10} horas de otros cursos')
print(f' - Ver 10 horas de otros cursos equivale a ver {dalto_curso *100 // otros_cursos_promedio / 10} horas de este cursos')
print('-----------------')