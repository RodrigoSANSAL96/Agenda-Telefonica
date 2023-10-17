# def , DEFINIR
# def nombreDeLaFuncion(parámetro de la funcion)

def sumar_dos(numero):
    return print(numero + 2)
sumar_dos(2)

def saludar(nombre, apellido):
    return print("Hola " + nombre + " " + apellido)
saludar("Rodrigo", "Sánchez Salguero")
saludar("Sánchez Salguero", "Rodrigo")
saludar(apellido="Sánchez Salguero", nombre="Rodrigo")

# EJEMPLOS

colores = ["azul", "blanco", "amarillo", "blanchedalmond", "rojo"]
print(colores)
def mostrar_color(i):
    print(colores[i])
mostrar_color(2)

def agregar_color(s):
    colores.append(s)
    print(colores)
agregar_color("violeta")

# EJERCICIOS
# 1)
def division(numero1, numero2):
    if numero2 == 0:
        print("Error")
    else:
        resultado = numero1 / numero2
        print(resultado)
division(numero1 = int(input("Ingrese un numero: ")), numero2 = int(input("Ingrese otro numero: ")))
    
# 2)

def perimetro_triangulo(ladoA, ladoB, ladoC=1): # EN ESTE EJEMPLO PUEDO DEFINIR UN PARAMETRO EN LA FUNCION
    perimetro = ladoA + ladoB + ladoC
    print(perimetro)
perimetro_triangulo(1,3) # Y AQUI PASARLE DOS DATOS DE LOS PARAMETROS FALTANTES



