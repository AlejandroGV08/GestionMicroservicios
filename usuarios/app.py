from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

def obtenerConexion():
    return pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-EMIMIIB\\SQLEXPRESS;DATABASE=PROYECTO;UID=sa;PWD=000000')

def verificarUsuario(id):
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario is not None

@app.route('/usuarios', methods=['POST'])
def crearUsuario():
    data = request.json
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (id, nombre, email) VALUES (?, ?, ?)", 
                   (data['id'], data['nombre'], data['email']))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Usuario creado correctamente"}), 201

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtenerUsuario(id):
    if not verificarUsuario(id):
        return jsonify({"error": "Usuario no encontrado"}), 404

    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    conn.close()

    return jsonify({"id": usuario[0], "nombre": usuario[1], "email": usuario[2]})

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminarUsuario(id):
    if not verificarUsuario(id):
        return jsonify({"error": "Usuario no encontrado"}), 404

    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Usuario eliminado correctamente"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
