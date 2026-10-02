#!/bin/sh
set -e

PORT="${PORT:-8000}"
WORKERS="${WEB_CONCURRENCY:-3}"

echo "[entrypoint] Python: $(python --version 2>&1)"
echo "[entrypoint] Puerto: $PORT | Workers: $WORKERS"
echo "[entrypoint] Working dir: $(pwd)"

# Las migraciones deben correr antes de aceptar trafico,
# si no /admin/ y /accounts/signup/ devuelven 500 por tablas faltantes.
echo "[entrypoint] Aplicando migraciones..."
python manage.py migrate --noinput

#collectstatic tambien se ejecuta aqui (y no solo en el build) para que el
# script sea autonomo: asi los .css sirven aunque la plataforma no haya
# corrido los pasos del Dockerfile. Es idempotente y rapido si ya existe.
# No bloquea el arranque si falla (el sitio queda sin estilos, no caido).
echo "[entrypoint] Recolectando archivos estaticos..."
python manage.py collectstatic --noinput \
  || echo "[entrypoint] AVISO: collectstatic fallo, los .css podrian no cargar."

# Opcional: crea el superusuario la primera vez (DJANGO_SUPERUSER_USERNAME/PASSWORD/EMAIL)
if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
  echo "[entrypoint] Verificando superusuario..."
  python manage.py createsuperuser --noinput || echo "[entrypoint] Superusuario ya existe."
fi

echo "[entrypoint] Iniciando Gunicorn..."

exec gunicorn config.wsgi:application \
  --bind "0.0.0.0:${PORT}" \
  --workers "${WORKERS}" \
  --timeout "${GUNICORN_TIMEOUT:-60}" \
  --graceful-timeout 30 \
  --keep-alive 5 \
  --access-logfile - \
  --error-logfile - \
  --capture-output \
  --forwarded-allow-ips="*"