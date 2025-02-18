from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URLs de los microservicios
servicioUsuarios = "http://localhost:5001"
servicioTareas = "http://localhost:5002"

@app.route('/usuarios', methods=['POST'])
def crearUsuario():
    respuesta = requests.post(f"{servicioUsuarios}/usuarios", json=request.json)
    return jsonify(respuesta.json()), respuesta.status_code

@app.route('/tareas', methods=['POST'])
def crearTarea():
    respuestaTarea = requests.post(f"{servicioTareas}/tareas", json=request.json)
    return jsonify(respuestaTarea.json()), respuestaTarea.status_code

@app.route('/tareas/<int:idTarea>', methods=['GET'])
def mostrarTarea(idTarea):
    respuesta = requests.get(f"{servicioTareas}/tareas/{idTarea}")
    return jsonify(respuesta.json()), respuesta.status_code

if __name__ == '__main__':
    app.run(port=5000)