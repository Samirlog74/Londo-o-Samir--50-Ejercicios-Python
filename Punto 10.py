# 10.Escribe un algoritmo o el respectivo diagrama de flujo que intercambie el valor de dos variables e imprima los valores antes y después del intercambio. Por ejemplo, si a = 1 y b = 3, al intercambiar sus valores serán a = 3 y b = 1 (Consejo: usar variable auxiliar).

print("Intercambiar varibles e imprimir ambas")
print("______________________________________")

Variable1 = input("Ingrese la primera variable: ") #Se le pide al usuario que ingrese la primera variable:
Variable2 = input("Ingrese la segunda variable: ") #Se le pide al usuario que ingrese la segunda variablae.

a = Variable1 # Se define otra variable con la primer variable.
b = Variable2 # Se define otra variable con la segunda variable.

Lista = ["Variables -"+ "Intercambio:", "1er: "+Variable1+" "+"    1er: "+b, "2da: "+Variable2+" "+"    2da: "+ a] # Se crea una lista concadenando varios strings del modo que al imprimirla por medio de un "For" muestra la variable y al frente de este la misma variable pero con el valor de la otra.

for x in Lista: # Se utiliza el for para imprimir la lista de manera que imprima elemento por elemento.
    print(x)