colores = ["blanco", "azul", "verde", "naranja", "marron"]

# MODIFICAR UN VALOR
colores[0] = "violeta"
print(colores)

# APPEND , QUE ES CONCATENAR. AGREGAR ELEMENTO

colores.append("rosado")
print(colores)

# INSERT, AGREGAR UN ELEMENTO EN ALGUNA POSICION

colores.insert(2, "purpura") # EL NUMERO 2 SIGNIFICA LA POSICION QUE INSERTAMOS EL COLOR
print(colores)

# REMOVE, ELIMINA EL ELEMENTO DE LA LISTA QUE LE INDIQUEMOS

colores.remove("purpura")
print(colores)

# LEN , MUESTRA LA CANTIDAD DE ELEMENTOS QUE TIENE LA LISTA
print(len(colores))

#IN , BUSCAR ALGUN ELEMENTO EN LA LISTA
print("violeta" in colores) # True, MUESTRA UN RESULTADO BOOLEANO
print("rojo" in colores) # False
print(colores[0:3]) 
print(colores[:3])
print(colores[3:])

# lista.metodo() 

# EXTEND , UNIR UNA LISTA CON OTRA
colores2 = ["celeste", "dorado"]
colores.extend(colores2)
print(colores)


# POP , ELIMINA UN ELEMENTO DE LA LISTA
colores.pop(2)
print(colores)

# EJERCICIOS

primarios = ["azul", "amarillo", "rojo"]
colores3 = ["blanco", "rojo", "blanchedalmond", "violeta", "naranja", "verde"]

# 1 
colores3.extend(primarios)
print(colores3)

# 2
primarios.pop(-1)
print(primarios)

# 3
colores3.pop(-3)
print(colores3)

# 4
colores3.insert(-3, "azul")
print(colores3)

colores3.append("azul")
print(colores3)