# Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    # Escribir notas personales en el archivo
    file.write("Nota 1: Hoy fue un día productivo.\n")
    file.write("Nota 2: Necesito comprar mercaderia para mi local.\n")
    file.write("Nota 3: No olvidar que tengo una reparación.\n")

# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    # Leer y mostrar el contenido del archivo línea por línea
    for line in file.readlines():
        print(line.strip())  # Eliminar el carácter de nueva línea al final de cada línea

# Cerrar Archivo
file.close()
