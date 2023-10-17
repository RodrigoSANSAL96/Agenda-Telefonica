# EJERCICIOS

alumnos = [
    {
        'nombre' : 'Carla',
        'nota' : 12,
        'inasistencias' : 3
    },
    {
        'nombre' : 'Juan',
        'nota' : 8,
        'inasistencias' : 4
    },
    {
        'nombre' : 'Andres',
        'nota' : 10,
        'inasistencias' : 6
    }
]

# 1

alumnos[1]['nota'] = 12
print(alumnos)

# 2
nuevo_alumnos = {
    'nombre' : 'Punku',
    'nota' : 4,
    'inasistencia' : 13
}
alumnos.append(nuevo_alumnos)
print(alumnos)

# 3

nombre = input("Ingresa tu nombre: ")
comentario = input("Ingresa un comentario: ")
diccionario = [{'nombre' : nombre, 'comentario' : comentario}]
print(diccionario)

# 4
diccionario = []
while comentario != "no mas":
    comentario = input("Ingresa un comentario, si no quiere agregar comentarios ponga 'no mas': ")
    if comentario != "no mas":
       diccionario.append(comentario)
print(diccionario)