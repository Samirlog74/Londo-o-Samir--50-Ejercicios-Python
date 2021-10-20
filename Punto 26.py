#26.Escribe un algoritmo o el respectivo diagrama de flujo que lea las cinco notas obtenidas por un estudiante y calcule su nota final, sabiendo que las cada nota tiene el siguiente valor: n1 (15 %), n2 (20%), n3 (15%), n4 (30%), n5 (20%). Si la nota obtenida es menor a 2, 0 deberá indicarle al estudiante que no puede habilitar, si la nota obtenida es menor a 3 deberá indicar que reprobó, si la nota es mayor o igual a 3 deberá indicar que aprobó y si es mayor a 4, 5 extenderá un mensaje de felicitación al estudiante.

print("Evaluar nota final del estudiante")
print("_________________________________")
print("""Recuerde que solo puede ingresar valores entre 0.0 y 5.0""")
print("_________________________________")
notas = []
contador = 0

while contador < 5: # Por medio de este ciclo while se le pedira al usuario que ingrese una nueva nota 5 veces.
    nota = float(input("Por favor ingrese la nota del estudiante: "))
    if nota < 0.0 or nota > 5.0: #Si la nota ingresada es mayor a 5.0 o menor a 0.0 se rompera el programa.
        break
    notas.append(nota) # Se agrega la variable nota la lista vacia "notas" creada anterioemnte.
    contador +=1

notafinal = notas[0]*0.15 + notas[1]*0.2 + notas[2]*0.15 + notas[3]*0.3 + notas[4]*0.2 #Se promedia las notas segun los porcentajes establecidos

if 2.0 <= notafinal < 3.0: # si el promedio es mayor o igual a 2  y menor que 3 el se imprimira la nota final y diciendo que reprobo, tambien si es menor que 2.0 se imprimira la nota final, que reprobo y que no puede habilitar, de lo contrario a esto se imprimira la nota final y que aprobo pero si esta es mayor a 4.5 ademas de lo anterior se imprimira un mensaje de felicitaciones.
    print("La nota final del etudiante es:","{0:.2f}".format(notafinal),"por lo que el estudiante reprobó el curso.") # se usa "{0:.2f}".format(notafinal) solo para imrpimir 2 decimales en el resultado final.

elif notafinal < 2.0:
    print("La nota final del etudiante es:","{0:.2f}".format(notafinal),"por lo que el estudiante reprobó el curso y no podra habilitar.")

else:
    print("La nota final del etudiante es:","{0:.2f}".format(notafinal),"por lo que el estudiante aprobó el curso.")
    if notafinal > 4.5:
        print("Felicitaciones por tu esfuerzo, sigue así.")
