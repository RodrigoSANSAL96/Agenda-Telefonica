#ESTRUCTURA DEL IF 
# if (condicion):
#   codigo()
# else if:
#   codigo()
# else:
#   codigo()

username = "admin"
password = "prueba"

if (input("nombre de usuario: ") == username):
    if (input("password: ") == password):
        print("usuario y contraseña correcta")
    else:
        print("Error")
else:
    print("Error")

#################################################

colorFavorito = "Verde"
colorFavoritoUsuario = input("Cual es tu color favorito? ")

if (colorFavorito == colorFavoritoUsuario.capitalize()): #Aqui pongo capitalize para que tome como True los valores verde y Verde EL CAPITALIZE PONE LA PRIMERA LETRA EN MAYUSCULA
    print("Mi color favorito es el mismo que el tuyo")
else:
    print("Mi color favorito es otro")

###########################################

n1 = float(input("numero 1 ")) # float , para poner numero decimal
n2 = float(input("numero 2 "))

if (n1>n2):
    print("n1 es mas grande")
else:
    print("n2 es mas grande")