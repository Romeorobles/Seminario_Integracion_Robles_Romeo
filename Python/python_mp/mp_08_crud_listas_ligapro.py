# mp 08 - CRUD de listas con tema LigaPro
# Autor: Romeo Robles

print("CRUD DE EQUIPOS LIGAPRO")
equipos = [
    {"id": 1, "nombre": "Liga de Quito", "ciudad": "Quito", "puntos": 55},
    {"id": 2, "nombre": "Barcelona SC", "ciudad": "Guayaquil", "puntos": 52},
    {"id": 3, "nombre": "Independiente del Valle", "ciudad": "Sangolqui", "puntos": 50},
]
id_publico = 4


def create():
    global id_publico
    print("Registrar equipo")
    nombre = input("Nombre del equipo: ")
    ciudad = input("Ciudad: ")
    puntos = int(input("Puntos: "))
    nuevo_equipo = {
        "id": id_publico,
        "nombre": nombre,
        "ciudad": ciudad,
        "puntos": puntos,
    }
    equipos.append(nuevo_equipo)
    id_publico += 1
    print("Equipo registrado")


def read():
    print("Tabla de equipos")
    for equipo in equipos:
        print(f"{equipo['id']} - {equipo['nombre']} ({equipo['ciudad']}) - {equipo['puntos']} pts")


def update():
    print("Actualizar equipo")
    id_update = int(input("Id a modificar: "))
    for equipo in equipos:
        if equipo["id"] == id_update:
            equipo["nombre"] = input("Nuevo nombre: ")
            equipo["ciudad"] = input("Nueva ciudad: ")
            equipo["puntos"] = int(input("Nuevos puntos: "))
            print("Equipo actualizado")
            return
    print("No existe un equipo con ese id")


def delete():
    print("Eliminar equipo")
    id_delete = int(input("Id a eliminar: "))
    for equipo in equipos:
        if equipo["id"] == id_delete:
            equipos.remove(equipo)
            print("Equipo eliminado")
            return
    print("No existe un equipo con ese id")


def menu():
    while True:
        print("=== LigaPro ===")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        option = input("Seleccione 1 al 5: ")
        if option == "1":
            create()
        elif option == "2":
            read()
        elif option == "3":
            update()
        elif option == "4":
            delete()
        elif option == "5":
            print("Cerrando sistema")
            break
        else:
            print("Ingrese una opcion valida")


menu()
