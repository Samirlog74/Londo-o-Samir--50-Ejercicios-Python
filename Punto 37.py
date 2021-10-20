#37.Escribe un algoritmo o el respectivo diagrama de flujo que dados 3 números, determine si los números se están incrementando, disminuyendo o ninguno de lo anterior de acuerdo con el orden de digitación. Por ejemplo: 1 , 4, 19 --> está incrementando  ;  33, 10 ,1 --> está disminuyendo;   3 , 18 , 10 --> Ni se incrementa ni se disminuyendo.

print("Determinar si incrementa o no la sucesión de números")
print("____________________________________________________")

num = input("Por favor ingrese 3 números separandolos con comas(,): ")
num = num.split(",")

if float(num[0]) < float(num[1]) and float(num[1]) < float(num [2]):
    print("Los números ingresados estan incrementandose.")

elif float(num[0]) > float(num[1]) and float(num[1]) > float(num[2]):
    print("Los números ingresados estan disminuyendose.")

else:
    print("Los números ingresados ni se incrementan ni se disminuyen.")
