from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

servicioUsuarios = "http://localhost:5001"
servicioTareas = "http://localhost:5002"
servicioNotificaciones = "http://localhost:5003"

@app.route('/usuarios', methods=['POST'])
def crearUsuario():
    respuesta = requests.post(f"{servicioUsuarios}/usuarios", json=request.json)
    return jsonify(respuesta.json()), respuesta.status_code

@app.route('/tareas', methods=['POST'])
def crearTarea():
    respuestaTarea = requests.post(f"{servicioTareas}/tareas", json=request.json)
    
    if respuestaTarea.status_code == 201:
        datosTarea = respuestaTarea.json()
        datosNotificacion = {
            "idTarea": datosTarea["id"],
            "asignado": datosTarea["asignado"],
            "mensaje": f"Nueva tarea asignada: {datosTarea['titulo']}"
        }
        requests.post(f"{servicioNotificaciones}/notificacion", json=datosNotificacion)
    
    return jsonify(respuestaTarea.json()), respuestaTarea.status_code

@app.route('/tareas/<int:idTarea>', methods=['GET'])
def mostrarTarea(idTarea):
    respuesta = requests.get(f"{servicioTareas}/tareas/{idTarea}")
    return jsonify(respuesta.json()), respuesta.status_code

if __name__ == '__main__':
    app.run(port=5000)
