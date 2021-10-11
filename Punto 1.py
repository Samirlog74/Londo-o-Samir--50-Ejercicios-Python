#1.Escribe un algoritmo o el respectivo diagrama de flujo para imprimir tu nombre y se le adicione un calificativo ingresado por el usuario. Por ejemplo: Carlos el crack o Juliana la mejor.

# Se le pide al usuario que ingrese un nombre cualquiera.
name = input("Ingrese el nombre de una persona: ") 
#Se define una variable la cual va a ser usada en el siguiente input para pedirle una cualidad del nombre de la persona ingresado anteriormente.
names = "¿Qué cualidad tiene "+ name.capitalize() +"?"

cualidad = input (names)

print(name.capitalize()+" "+ cualidad.lower()+".")