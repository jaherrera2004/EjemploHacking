FROM python:3.11-slim

WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la app
COPY . .

ENV FLASK_APP=app.py

# Ejecutar con gunicorn en producción
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
