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
    agregarOtro = input("Desea agregar otro contacto? ")
    if agregarOtro.capitalize() == "Si":
        agregarContactos()
    else:
        print("Contacto guardado")
agregarContactos()
print(contactos) 

def buscarContacto():
    nombreIngresado = input("Ingrese el nombre del contacto que busca: ")
    apellidoIngresado = input("Ingrese el apellido del contacto que busca: ")
    contacto_encontrado = False  
    for i in contactos:
        if i['nombre'] == nombreIngresado.capitalize() and i['apellido'] == apellidoIngresado.capitalize():
            print("Contacto encontrado")
            print(i)
            contacto_encontrado = True
            editarContacto = input("Desea editar el contacto? ")
            if editarContacto.capitalize() == "Si":
                i['nombre'] = input("Ingrese el nuevo nombre: ")
                i['apellido'] = input("Ingrese el nuevo apellido: ")
                i['telefono'] = input("Ingrese el nuevo numero de telefono: ")
                print(contactos)
            eliminarContacto = input("Desea eliminar el contacto? ")
            if eliminarContacto.capitalize() == "Si":
                contactos.remove(i)
                print(contactos)
    if not contacto_encontrado:
        print("No existe ese contacto")
buscarContacto()

    
