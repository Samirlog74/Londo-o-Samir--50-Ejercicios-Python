#35.Escribe un algoritmo o el respectivo diagrama de flujo que dado un número entre 0 y 10, imprima el nombre del número. Ejemplo: 1 ---> UNO

print("Nombrar el número escogido de 0 a 10")
print("____________________________________")

list = ["Cero.","Uno.","Dos.","Tres.","Cuatro.","Cinco.","Seis.","Siete.","Ocho.","Nueve.","Diez."]
num = int(input("Ingrese un número entero del 0 al 10: "))

if 0 <= num <= 10:
    print("El número ingresado fue un "+ list[num])

else:
    print("El número ingresado no esta en el rango entre 0 y 10")