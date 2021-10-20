#39.Escribe un algoritmo o el respectivo diagrama de flujo que lea un número del día de la semana (entre 1 y 7) e indique el nombre del día. Por ejemplo:  1 ---> Lunes ; 5 ---> Viernes

print("Nombrar el día de la semana segun el número ingresado")
print("____________________________________")

list = [" ","Lunes.","Martes.","Miercoles.","Jueves.","Viernes.","Sabado.","Domingo."]

num = int(input("Ingrese el número del día de la semana(entre 1 y 7): "))

if 1 <= num <= 7:
    print("El día de la semana que escogiste fue un "+ list[num])

else:
    print("El número ingresado no esta en el rango entre 1 y 7")