
# Simulación de Broken Access Control

Este proyecto es una simulación educativa para demostrar el concepto de Broken Access Control en aplicaciones web usando Flask y JWT.

## ¿Cómo funciona?

La aplicación tiene dos formas de mostrar los datos de usuario:

- **Datos no protegidos:** Cualquier usuario puede ver los datos de cualquier otro usuario simplemente cambiando el ID en la URL, sin autenticación.
- **Datos protegidos:** Solo el usuario autenticado puede ver sus propios datos. Se utiliza JWT para validar la identidad y el backend verifica que el ID solicitado coincida con el del token.

### Flujo
1. El usuario inicia sesión con su usuario y contraseña. Si son correctos, recibe un JWT y su ID, que se guardan en el navegador.
2. En el dashboard, puede elegir ver sus datos protegidos (requiere JWT) o no protegidos (sin autenticación).
3. Si intenta acceder a datos protegidos de otro usuario, el backend rechaza la petición y muestra una página de error.
4. Los datos no protegidos pueden ser accedidos por cualquiera, demostrando el riesgo de Broken Access Control.

## Archivos principales

- `app.py` - Lógica de rutas, autenticación y control de acceso.
- `middleware/jwt_middleware.py` - Métodos para generar y verificar JWT.
- `templates/` - Vistas para login, dashboard, datos protegidos/no protegidos y error de acceso.

## Ejecución

Construir y arrancar con docker-compose (recomendado):
```powershell
docker compose up --build
```

O construir imagen manualmente y ejecutar:
```powershell
docker build -t ejemplo-flask .
docker run -p 5000:5000 ejemplo-flask
```

Luego abre en el navegador: http://localhost:5000

## Notas
- Puedes editar archivos localmente porque `docker-compose.yml` monta la carpeta en `/app`.
- Si ves advertencias del editor sobre `import flask` es normal si no tienes las dependencias instaladas en tu entorno local; Docker instala las dependencias dentro del contenedor.
