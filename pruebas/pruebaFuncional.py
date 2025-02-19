import requests

# Configuración de URLs
BASE_URL_USUARIOS = "http://127.0.0.1:5000"
BASE_URL_TAREAS = "http://127.0.0.1:5001"

# Prueba 1: Creación de usuario
def test_crear_usuario():
    url = f"{BASE_URL_USUARIOS}/usuarios"
    data = {"id": 10000, "nombre": "Juan Perez", "email": "juan@example.com"}
    response = requests.post(url, json=data)
    
    assert response.status_code == 201, f"Error: {response.status_code} - {response.text}"
    assert response.json()["mensaje"] == "Usuario creado correctamente"
    print("Prueba de creación de usuario: Éxito")

# Prueba 2: Eliminación de tarea
def test_eliminar_tarea():
    # Crear una tarea primero
    url_crear = f"{BASE_URL_TAREAS}/tareas"
    data_tarea = {"id": 10000, "titulo": "Tarea de prueba", "descripcion": "Descripción de prueba", "asignadoA": 10000}
    response_crear = requests.post(url_crear, json=data_tarea)
    
    assert response_crear.status_code == 200 or response_crear.status_code == 201, f"Error al crear tarea: {response_crear.status_code} - {response_crear.text}"

    # Eliminar la tarea
    url_eliminar = f"{BASE_URL_TAREAS}/tareas/10000"
    response_eliminar = requests.delete(url_eliminar)
    
    assert response_eliminar.status_code == 200, f"Error: {response_eliminar.status_code} - {response_eliminar.text}"
    assert response_eliminar.json()["mensaje"] == "Tarea eliminada correctamente"
    print("Prueba de eliminación de tarea: Éxito")

if __name__ == "__main__":
    test_crear_usuario()
    test_eliminar_tarea()
