from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

def obtenerConexion():
    return pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-EMIMIIB\\SQLEXPRESS;DATABASE=PROYECTO;UID=sa;PWD=000000')

@app.route('/notificaciones/<int:idUsuario>', methods=['GET'])
def obtenerNotificaciones(idUsuario):
    conn = obtenerConexion()
    cursor = conn.cursor()
    cursor.execute("SELECT idTarea, mensaje, fecha FROM notificaciones WHERE asignado = ?", (idUsuario,))
    notificaciones = cursor.fetchall()
    conn.close()

    resultado = [{"idTarea": n[0], "mensaje": n[1], "fecha": str(n[2])} for n in notificaciones]
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
