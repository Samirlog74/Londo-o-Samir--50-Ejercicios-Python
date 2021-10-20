#28.Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y lo convierta a decimal.

num = int(input("Por favor ingrese el número entero que desea comvertir a decimal: "))
num /=100 #Se divide la variable ingresara para que este quede siempre despues del punto siendo decimal.

print("El número decimal sera: ", num)