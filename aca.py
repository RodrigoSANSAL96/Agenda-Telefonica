def buscarContacto():
    nombreIngresado = input("Ingrese el nombre del contacto que busca: ")
    apellidoIngresado = input("Ingrese el apellido del contacto que busca: ")
    for i in contactos:
        if contactos[i][nombre] == nombreIngresado.capitalize:
            for j in contactos:
                if contactos[i][j][apellido] == apellidoIngresado.capitalize:
                    print(contacto[i][j])
                else:
                    print("No existe el contacto que busca")
        else: 
            print("No existe el contacto que busca")
buscarContacto()