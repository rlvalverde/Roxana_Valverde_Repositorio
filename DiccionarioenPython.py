# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "Nombre": "Juan",
    "Edad": 30,
    "Ciudad": "Ciudad A",
    "Profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["Ciudad"] = "Baños de Agua Santa"

# Agregar una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal["Profesion"] = "Desarrollador"

# Verificar si la clave "telefono" existe en el diccionario y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0996404867"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
