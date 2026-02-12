import time
import numpy as np 

n = 1_000_000
lista = list(range(n))
array = np.array(lista)

tiempo_inicio = time.time()
lista_resultado = []
for x in lista:
    lista_resultado.append(x * 3)
tiempo_lista = time.time () - tiempo_inicio
 
tiempo_inicio = time.time ()
array_resultado = array * 3
tiempo_array = time.time () - tiempo_inicio 

print("tiempo con lista:", tiempo_lista, "segundos")
print("tiempo con numpy:", tiempo_array, "segundos")

# problema 2

notas = [3.0, 2.9, 4.5, 3.8, 2.5, 1.8, 2.9, 4.2, 5.0, 2.9]

notas_mejoradas = []

for nota in notas:
    if nota == 2.9:
        notas_mejoradas.append (nota + 0.3)
    else:
        notas_mejoradas.append(nota)

suma = 0
for n_m in notas_mejoradas:
    suma += n_m

aprobados = 0
reprobados = 0

for nota in notas_mejoradas:
    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1    


print ("estudiantes aprobados:", aprobados)
print ("estudiantes reprobados:", reprobados)

for i, nota in enumerate(notas):
    print(f"Estudiante: {i} {nota}")