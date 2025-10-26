from flask import Flask, render_template, request, jsonify
from usuarios import obtener_usuarios
from middleware.jwt_middleware import generar_jwt
from middleware.jwt_middleware import obtener_payload


app = Flask(__name__, template_folder='templates')

usuarios = obtener_usuarios()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/datos-protegidos/')
def datos_protegidos():
    return render_template('verDatosProtegido.html')

@app.route('/datos-no-protegidos')
def datos_no_protegidos():
    return render_template('verDatosNoProtegido.html')

@app.route('/sin-permiso')
def no_permitido():
    return render_template("sinPermiso.html")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    usuario = next((u for u in usuarios if u['username'] == username and u['password'] == password), None)
    if usuario:
        token = generar_jwt(usuario)
        return jsonify({'jwt': token, 'id_usuario': usuario['id']})
    else:
        return jsonify({'jwt': None}), 401
    
@app.route('/usuario-no-protegido/<int:id>', methods=['GET'])
def obtener_usuario_no_protegido(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

@app.route('/usuario-protegido/<int:id>', methods=['GET'])
def obtener_usuario_protegido(id):
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({'error': 'Token JWT requerido'}), 401
    
    try:
        token = auth_header.split(" ")[1]
    except IndexError:
        return jsonify({'error': 'Formato de Authorization incorrecto'}), 401
    
    payload = obtener_payload(token)
    if not payload:
        return jsonify({'error': 'Token inválido'}), 401
    
    if int(payload.get('id')) != id:
        return jsonify({'error': 'No tienes permiso para ver estos datos'}), 403
    
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404
