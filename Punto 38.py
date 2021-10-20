#38.Escribe un algoritmo o el respectivo diagrama de flujo que, dados dos números, verifique si ambos están entre 0 y 5 o retorne false sino es cierto. Por ejemplo 1 y 2 ---> true ; 1 y 8 ---> false

print("Verificar si los números estan entre 0 y 5")
print("__________________________________________")

num = float(input("Ingrese un número: "))
num1 = float(input("Por favor ingrese otro número: "))

if 0 <= num <= 5 and 0 <= num1 <= 5:
    print("Los números ingresados estan entre 0 y 5.")

else:
    if 0 <= num <=5:
        print("Solo el primer número ingresado esta entre 0 y 5.")
        
    elif  0 <= num1 <= 5:
        print("Solo el segundo número ingrsado esta entre 0 y 5.")
    
    else:
        print("Ninguno de los dos números ingresados esta entre 0 y 5.")
