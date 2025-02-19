import requests

BASE_URL_USUARIOS = "http://127.0.0.1:5000"
BASE_URL_TAREAS = "http://127.0.0.1:5001"
BASE_URL_NOTIFICACIONES = "http://127.0.0.1:5002"

def verificarUsuario(idUsuario):
    response = requests.get(f"{BASE_URL_USUARIOS}/usuarios/{idUsuario}")
    if response.status_code == 200:
        return True
    else:
        print(f"Error al verificar el usuario: {response.text}")
        return False

def verificarTarea(idTarea):
    response = requests.get(f"{BASE_URL_TAREAS}/tareas/{idTarea}")
    if response.status_code == 200:
        return True
    else:
        print(f"Error al verificar la tarea: {response.text}")
        return False

def menuUsuarios():
    while True:
        print("\nUSUARIOS")
        print("1. Crear usuario")
        print("2. Eliminar usuario")
        print("3. Mostrar usuario")
        print("4. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            idUsuario = input("Ingrese ID del usuario: ")
            nombre = input("Ingrese nombre: ")
            email = input("Ingrese email: ")
            data = {"id": idUsuario, "nombre": nombre, "email": email}
            response = requests.post(f"{BASE_URL_USUARIOS}/usuarios", json=data)
            if response.status_code == 200 or response.status_code == 201:
                print(response.json())
            else:
                print(f"Error al crear usuario: {response.text}")

        elif opcion == "2":
            idUsuario = input("Ingrese ID del usuario a eliminar: ")
            if not verificarUsuario(idUsuario):
                print("El usuario con ese ID no existe.")
                continue
            response = requests.delete(f"{BASE_URL_USUARIOS}/usuarios/{idUsuario}")
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"Error al eliminar usuario: {response.text}")

        elif opcion == "3":
            idUsuario = input("Ingrese ID del usuario para mostrar: ")
            if not verificarUsuario(idUsuario):
                print("El usuario con ese ID no existe.")
                continue
            response = requests.get(f"{BASE_URL_USUARIOS}/usuarios/{idUsuario}")
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"Error al obtener usuario: {response.text}")

        elif opcion == "4":
            break
        else:
            print("Opcion invalida.")

def menuTareas():
    while True:
        print("\nTAREAS")
        print("1. Crear tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tarea")
        print("4. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            idTarea = input("Ingrese ID de la tarea: ")
            titulo = input("Ingrese titulo: ")
            descripcion = input("Ingrese descripcion: ")
            asignadoA = input("Ingrese ID del usuario asignado: ")

            if not verificarUsuario(asignadoA):
                print("El usuario asignado no existe.")
                continue

            data = {"id": idTarea, "titulo": titulo, "descripcion": descripcion, "asignadoA": asignadoA}
            response = requests.post(f"{BASE_URL_TAREAS}/tareas", json=data)
            if response.status_code == 200 or response.status_code == 201:
                print(response.json())
            else:
                print(f"Error al crear tarea: {response.text}")

        elif opcion == "2":
            idTarea = input("Ingrese ID de la tarea a eliminar: ")
            if not verificarTarea(idTarea):
                print("La tarea con ese ID no existe.")
                continue
            response = requests.delete(f"{BASE_URL_TAREAS}/tareas/{idTarea}")
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"Error al eliminar tarea: {response.text}")

        elif opcion == "3":
            idTarea = input("Ingrese ID de la tarea para mostrar: ")
            if not verificarTarea(idTarea):
                print("La tarea con ese ID no existe.")
                continue
            response = requests.get(f"{BASE_URL_TAREAS}/tareas/{idTarea}")
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"Error al obtener tarea: {response.text}")

        elif opcion == "4":
            break
        else:
            print("Opcion invalida.")

def mostrarNotificaciones():
    idUsuario = input("Ingrese ID del usuario para ver sus notificaciones: ")
    if not verificarUsuario(idUsuario):
        print("El usuario con ese ID no existe.")
        return

    response = requests.get(f"{BASE_URL_NOTIFICACIONES}/notificaciones/{idUsuario}")
    if response.status_code == 200:
        notificaciones = response.json()

        if not notificaciones:
            print("No hay notificaciones.")
        else:
            print("\nNotificaciones:")
            for n in notificaciones:
                print(f"- {n['mensaje']} (Tarea {n['idTarea']}, Fecha: {n['fecha']})")
    else:
        print(f"Error al obtener notificaciones: {response.text}")

def menuPrincipal():
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Administrar usuarios")
        print("2. Administrar tareas")
        print("3. Mostrar notificaciones")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menuUsuarios()
        elif opcion == "2":
            menuTareas()
        elif opcion == "3":
            mostrarNotificaciones()
        elif opcion == "4":
            print("Saliendo del sistema")
            break
        else:
            print("Opcion invalida.")

# Ejecutar menu
menuPrincipal()