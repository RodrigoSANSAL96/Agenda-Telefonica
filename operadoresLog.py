username = "admin"
password = "prueba"

input_username = input("Ingrese un username: ")
input_password = input("Ingrese un password: ")

if (input_username == username and input_password == password):
    print("Usuario y contraseña correctos")
else:
    print("Usuario o contraseña incorrectos")