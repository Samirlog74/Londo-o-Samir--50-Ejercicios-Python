#36.Escribe un algoritmo o el respectivo diagrama de flujo que dado un número menor a un 100.000 determine la cantidad de dígitos que tiene. Por ejemplo 1093 tiene 4 dígitos.

print("Contar digitos de un número menor a 100.000")
print("___________________________________________")
digi = input("Por favor ingrese un número: ")

digi1 = digi.split(".")
digi1 = int("".join(digi1))

if digi1 < 100000:
    print(digi, "tiene", len(str(digi1)),"digitos.")

else:
    print("El número ingresado es mayor que 100.000.")
