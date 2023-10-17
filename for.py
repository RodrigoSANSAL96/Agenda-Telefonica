colores = ["azul", "blanco", "amarillo", "blanchedalmond", "rojo"]
for x in colores:
    print(x)

# RANGE, NOS DEVUELVE TODOS LOS NUMEROS ENTRE DOS NUMEROS DADOS

for i in range(4):
    print(i)
for i in range(2,6):
    print(i)

# FOR EN LISTAS

for c in colores:
    print(c)

# EJERCICIOS
 # 1
colores2 = [ "blanco", "blanchedalmond", "violeta", "naranja", "verde" ]

for x in colores2:
    print(x)

# CONDICION IN , SE PUEDE USAR TAMBIEN PARA VER SI UN COLOR ESTA DENTRO DE LA LISTA

esta_blanco_en_la_lista = "blanco" in colores2
print(esta_blanco_en_la_lista) # ESTOS RESULTADOS SON BOOLEANOS, TRUE EN ESTE CASO
esta_azul_en_la_lista = "azul" in colores2
print(esta_azul_en_la_lista) # FALSE EN ESTE

# 2

primarios = [ "azul", "amarillo", "rojo" ]

colores3 = [ "blanco", "azul", "blanchedalmond", "violeta", "rojo", "naranja", "verde", "amarillo" ]

for i in colores3:
    if i not in primarios:
        print(i)

for i in colores3:
    if i in primarios:
        print(i + " está en la lista primarios")
    else:
        print(i + " no está en la lista primarios")

# Hacé un programa que guarde en una lista los primeros X valores de la serie de Fibonacci.

lista = []
x = int(input("Ingresá cuantas cosas vas a agregar a la lista: "))
for i in range(x):
    lista.append(input("Agregá algo a la lista: "))
    print(lista)
