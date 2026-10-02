# syntax=docker/dockerfile:1

# Imagen base: Python slim (más liviana que python:3.14 completo)
FROM python:3.14-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PORT=8000

WORKDIR /app

# Copia los requerimientos primero (capa cacheada: si no cambian deps, no reinstala)
COPY requirements.txt ./

# Instala dependencias
RUN pip install -r requirements.txt --root-user-action=ignore

# Copia el código
COPY . .

# Asegura permisos de ejecucion (el host es Windows y el contexto puede perder el bit +x)
RUN chmod +x /app/entrypoint.sh

# Genera los archivos estáticos en tiempo de build.
# whitenoise los sirve en runtime, asi que no se necesita nginx ni volumen extra.
RUN DJANGO_SECRET_KEY=build-time-placeholder \
    DJANGO_DEBUG=False \
    python manage.py collectstatic --noinput

# Puerto que espera el proxy de Seenode
EXPOSE 8000

# Arranque: aplica migraciones y luego levanta gunicorn
CMD ["/app/entrypoint.sh"]