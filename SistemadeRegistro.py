# Lista de estudiantes (cada estudiante es un diccionario)
estudiantes = [
    {"id": 1, "nombre": "Ana Pérez", "edad": 20},
    {"id": 2, "nombre": "Luis Gómez", "edad": 22},
    {"id": 3, "nombre": "Marta Rodríguez", "edad": 21},
]

def mostrar_lista_estudiantes():
    print("Lista de estudiantes:")
    for idx, estudiante in enumerate(estudiantes):
        print(f"{idx + 1}. {estudiante['nombre']} (Edad: {estudiante['edad']})")

def seleccionar_estudiante():
    while True:
        try:
            eleccion = int(input("Ingrese el número del estudiante que desea actualizar o eliminar: "))
            if 1 <= eleccion <= len(estudiantes):
                return eleccion - 1
            else:
                print("Número no válido. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def actualizar_estudiante(indice):
    nombre = input("Ingrese el nuevo nombre del estudiante: ")
    edad = int(input("Ingrese la nueva edad del estudiante: "))
    estudiantes[indice]['nombre'] = nombre
    estudiantes[indice]['edad'] = edad
    print("Estudiante actualizado.")

def eliminar_estudiante(indice):
    estudiantes.pop(indice)
    print("Estudiante eliminado.")

def menu():
    while True:
        print("\nOpciones:")
        print("1. Mostrar lista de estudiantes")
        print("2. Actualizar estudiante")
        print("3. Eliminar estudiante")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            mostrar_lista_estudiantes()
        elif opcion == "2":
            mostrar_lista_estudiantes()
            indice = seleccionar_estudiante()
            actualizar_estudiante(indice)
        elif opcion == "3":
            mostrar_lista_estudiantes()
            indice = seleccionar_estudiante()
            eliminar_estudiante(indice)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Ejecutar el menú
menu()
