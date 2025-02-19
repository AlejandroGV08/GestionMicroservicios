from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

def obtenerConexion():
    return pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-EMIMIIB\\SQLEXPRESS;DATABASE=PROYECTO;UID=sa;PWD=000000')

def verificarTarea(id):
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tareas WHERE id = ?", (id,))
    tarea = cursor.fetchone()
    conn.close()
    return tarea is not None

def verificarUsuario(id):
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario is not None

@app.route('/tareas', methods=['POST'])
def crearTarea():
    data = request.json
    if not verificarUsuario(data['asignadoA']):
        return jsonify({"error": "El usuario asignado no existe"}), 400
    
    conn = obtenerConexion()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO tareas (id, titulo, descripcion, asignadoA) VALUES (?, ?, ?, ?)", 
                   (data['id'], data['titulo'], data['descripcion'], data['asignadoA']))
    conn.commit()
    
    mensaje = f"Tarea '{data['titulo']}' asignada a usuario {data['asignadoA']}"
    cursor.execute("INSERT INTO notificaciones (idTarea, mensaje, asignado, fecha) VALUES (?, ?, ?, GETDATE())", 
                   (data['id'], mensaje, data['asignadoA']))
    conn.commit()

    conn.close()
    return jsonify({"mensaje": "Tarea creada correctamente"})

@app.route('/tareas/<int:id>', methods=['GET'])
def obtenerTarea(id):
    if not verificarTarea(id):
        return jsonify({"error": "Tarea no encontrada"}), 404

    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, descripcion, asignadoA FROM tareas WHERE id = ?", (id,))
    tarea = cursor.fetchone()
    conn.close()

    return jsonify({"id": tarea[0], "titulo": tarea[1], "descripcion": tarea[2], "asignadoA": tarea[3]})

@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminarTarea(id):
    if not verificarTarea(id):
        return jsonify({"error": "Tarea no encontrada"}), 404

    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Tarea eliminada correctamente"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
