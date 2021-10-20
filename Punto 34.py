#34.Escribe un algoritmo o el respectivo diagrama de flujo que, dado un usuario y una contraseña predefinida (por ejemplo usuario=”carlos" y contraseña=”1234”, le permita a un usuario digital su usuario y contraseña y enviar un mensaje de inicio de sesión si lo digitado corresponde al usuario y contraseña predefinida.

print("--Registrarse como nuevo usuario--")
print("__________________________________")
x=0
usu = input("Ingrese su nombre de usuario: ")

while x == 0:
    usu1 = input("Por favor confirme su nombre de usuario: ")
    if usu1 == usu:
        break

contra = input("Ingrese su contraseña: ")
while x == 0:
    contra1 = input("Por favor confirme su contraseña: ")
    if contra1 == contra:
        break

print(" ")
print("--Inicio de sesión--")
print("____________________")


while x==0:
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario==usu and contraseña==contra:
        print("Su sesión se ha iniciado correctamente.")
        break
    
    else:
        print("Usuario o contraseña invalidos.")
        pre = input("¿ Desea intentarlo de nuevo ? ")
        if pre.lower() == "si":
            continue
        elif pre.lower() == "no":
            print("Que tenga un buen día.")
            break
        else:
            print("Que tenga un buen día.")
            break
