x = 0
while x !=5:
    print("1) Agregar contacto")
    print("2) Buscar contacto")
    print("3) Editar contacto")
    print("4) Eliminar contacto")
    print("5) Salir")
    x = int(input("Ingrese el numero de la opción que desea hacer: "))
    if x == 1:
        print("Agregar contacto")
    elif x == 2 or x == 3 or x == 4:
        print("buscar contacto")
    else:
        print("Eligio salir")