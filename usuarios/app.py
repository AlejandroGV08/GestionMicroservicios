from flask import Flask, jsonify, request

app = Flask(__name__)

# Cambiar para vincular a SQL
usuarios = []

@app.route('/usuarios', methods=['POST'])
def crearUsuario():
    usuario = request.json
    usuarios.append(usuario)
    return jsonify(usuario), 201

@app.route('/usuarios/<int:idUsuario>', methods=['GET'])
def mostrarUsuario(idUsuario):
    usuario = next((i for i in usuarios if i['id'] == idUsuario), None)
    return jsonify(usuario) if usuario else ('', 404)

if __name__ == '__main__':
    app.run(port=5001)
