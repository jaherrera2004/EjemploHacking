import jwt
import datetime

SECRET_KEY = 'mi_clave_secreta'

# Genera un JWT con los datos del usuario

def generar_jwt(usuario):
    payload = {
        'username': usuario['username'],
        'email': usuario['email'],
        "id": usuario['id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


# Verifica y decodifica el JWT, retorna el payload si es válido, None si no
def verificar_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except Exception:
        return None

# Obtiene el payload del JWT, retorna None si el token no es válido
def obtener_payload(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except Exception:
        return None
