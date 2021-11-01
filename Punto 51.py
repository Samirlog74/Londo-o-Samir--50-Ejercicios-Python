#51.Construye un algoritmo y el respectivo diagrama de flujo que le solicite al usuario un número entero positivo, si el usuario digita un valor no permito, le debe volver a pedir el número. Una vez ingrese un valor válido deberá imprimir dicho valor.

print("Imprimir un número entero positivo")
print("__________________________________")

contador = 0

while contador==0:
    try:
        num = int(input("Por favor ingrese un número entero positivo: "))
    
        if num > 0:
            print("El número entero positivo ingresado fue un ",num)
            break
    
        else:
            print("El número ingresado es invalido.")
            continue
    
    except ValueError:
        print("El dato ingresado es invalido.")
