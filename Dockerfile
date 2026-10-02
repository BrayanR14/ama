# Usa la imagen base de Python que ya tienes
FROM python:3.14

# Variables de entorno para optimizar Python en Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crea y establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia los requerimientos primero (ayuda a que el despliegue sea más rápido si no cambias dependencias)
COPY requirements.txt /usr/src/app/

# Instala las dependencias y desactiva la advertencia de root
RUN pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

# Copia el resto de tu código al contenedor
COPY . /usr/src/app/

# Expone el puerto 8000 (estándar para Gunicorn)
EXPOSE 8000

# Comando de inicio usando Gunicorn (formato JSON [ ] para evitar la advertencia de OS signals)
CMD ["gunicorn", "ama.wsgi:application", "--bind", "0.0.0.0:8000"]