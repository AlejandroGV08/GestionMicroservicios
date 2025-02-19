import requests

def test_seguridad_entradas():
    url = 'http://192.168.1.35:5000/usuarios';
    # Intento de inyección SQL
    data = {"id": "1; DROP TABLE usuarios; --", "nombre": "Hacker", "email": "hacker@example.com"}
    response = requests.post(url, json=data)
    
    assert response.status_code == 400, f"Error: {response.status_code} - {response.text}"
    assert "error" in response.json()
    print("Prueba de seguridad (validación de entradas): Éxito")

# Ejecutar la prueba de seguridad
if __name__ == "__main__":
    test_seguridad_entradas()