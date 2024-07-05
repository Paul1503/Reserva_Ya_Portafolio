#!/usr/bin/env bash
# Exit on error
set -o errexit

# Instalar dependencias del proyecto desde requirements.txt
pip install -r requirements.txt

# Recopilar archivos estáticos
python manage.py collectstatic --no-input

# Aplicar migraciones de la base de datos
python manage.py migrate