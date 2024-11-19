from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = 'secret'

# Usuarios simulados
users = {'admin': 'password123'}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username] == password:
        # Generar token con validez de 30 segundos
        token = jwt.encode(
            {'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)},
            SECRET_KEY,
            algorithm='HS256'
        )
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401

@app.route('/validate', methods=['GET'])
def validate_token():
    token = request.headers.get('Authorization')
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'message': 'Token válido'})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Límite de tiempo excedido, token inválido'}), 401
    except Exception as e:
        return jsonify({'message': 'Token inválido'}), 401

if __name__ == '__main__':
    app.run(debug=True)
