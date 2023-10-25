contactos = []

def agregarContactos():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingresa el numero de telefono: ")
    nuevo_contacto = {
        'nombre' : nombre.capitalize(),
        'apellido' : apellido.capitalize(),
        'telefono' : telefono
        }
    contactos.append(nuevo_contacto)
    print("Contacto Guardado")

def buscarContacto():
    nombreIngresado = input("Ingrese el nombre del contacto que busca: ")
    apellidoIngresado = input("Ingrese el apellido del contacto que busca: ")
    contacto_encontrado = False  
    for i in contactos:
        if i['nombre'] == nombreIngresado and i['apellido'] == apellidoIngresado:
            print("Contacto encontrado")
            print(i)
            contacto_encontrado = True
            if x == 3:
                i['nombre'] = input("Ingrese el nuevo nombre: ")
                i['apellido'] = input("Ingrese el nuevo apellido: ")
                i['telefono'] = input("Ingrese el nuevo numero de telefono: ")
                print(contactos)
            if x == 4:
                contactos.remove(i)
                print(contactos)
    if not contacto_encontrado:
        print("No existe ese contacto")

x = 0
while x !=6:
    print("1) Agregar contacto")
    print("2) Buscar contacto")
    print("3) Editar contacto")
    print("4) Eliminar contacto")
    print("5) Ver contactos")
    print("6) Salir")
    x = int(input("Ingrese el numero de la opción que desea hacer: "))
    if x == 1:
        agregarContactos()
    elif x == 2 or x == 3 or x == 4:
        buscarContacto()
    elif x == 5:
        print(contactos)
    else:
        print("Eligio salir")