from flask import Flask, jsonify, request

app = Flask(__name__)

# Cambiar para vincular a SQL
tareas = []

@app.route('/tareas', methods=['POST'])
def crearTarea():
    tarea = request.json
    tareas.append(tarea)
    return jsonify(tarea), 201

@app.route('/tareas/<int:idTarea>', methods=['GET'])
def mostrarTarea(idTarea):
    tarea = next((i for i in tareas if i['id'] == idTarea), None)
    return jsonify(tarea) if tarea else ('', 404)

if __name__ == '__main__':
    app.run(port=5002)
