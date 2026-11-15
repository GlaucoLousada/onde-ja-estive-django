# Onde Já Estive (Django)

Blog de viagens feito com Django para a segunda entrega de laboratório de
PMR3304 - Sistemas de Informação. Aplicação CRUD de posts, com comentários
e categorias.

## Como rodar localmente

```
python -m venv .venv
.venv\Scripts\activate            (Windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata seed    (opcional: dados de exemplo)
python manage.py createsuperuser
python manage.py runserver
```

O site fica em http://127.0.0.1:8000/ e o administrador em
http://127.0.0.1:8000/admin/.

## Implantação no Render

- Build Command: `./build.sh`
- Start Command: `gunicorn blogsite.wsgi`
- Variáveis de ambiente: `PYTHON_VERSION`, `SECRET_KEY`,
  `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_PASSWORD`,
  `DJANGO_SUPERUSER_EMAIL` e, se usar PostgreSQL, `DATABASE_URL`.
