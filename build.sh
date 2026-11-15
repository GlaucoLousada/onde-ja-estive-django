#!/usr/bin/env bash
# Script de build usado pelo Render
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
# Carrega os dados de exemplo (posts, comentários, categorias e usuários)
python manage.py loaddata seed
# Cria o superusuário a partir das variáveis DJANGO_SUPERUSER_* (se definidas)
python manage.py createsuperuser --no-input || true
