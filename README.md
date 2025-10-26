# Proyecto Flask dockerizado

Este proyecto es una plantilla mínima de una aplicación Flask empaquetada para Docker.

Archivos principales:

- `app.py` - aplicación Flask mínima que sirve templates desde `templates/`.
- `requirements.txt` - dependencias (Flask + gunicorn).
- `Dockerfile` - construye la imagen usando `python:3.11-slim` y arranca con gunicorn.
- `docker-compose.yml` - orquesta el servicio `web` y mapea el puerto 5000.
- `templates/` - contiene `base.html` e `index.html`.

Cómo ejecutar (PowerShell):

# Construir y arrancar con docker-compose (recomendado)
```powershell
docker compose up --build
```

# O construir imagen manualmente y ejecutar
```powershell
docker build -t ejemplo-flask .
docker run -p 5000:5000 ejemplo-flask
```

Luego abre en el navegador: http://localhost:5000

Notas:
- Para desarrollo rápido puedes editar archivos localmente porque `docker-compose.yml` monta la carpeta en `/app`.
- Si ves advertencias del editor sobre `import flask` es normal si no tienes las dependencias instaladas en tu entorno local; Docker instala las dependencias dentro del contenedor.
