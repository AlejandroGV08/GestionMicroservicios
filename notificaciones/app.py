from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/notificacion', methods=['POST'])
def notificacion():
    datosNotificacion = request.json
    # Cambiar para vincular a SQL
    print(f"Notificación: {datosNotificacion}")
    return jsonify(datosNotificacion), 200

if __name__ == '__main__':
    app.run(port=5003)
