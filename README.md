# AMA
## Objectivos

El objetivo de nuestra pagina web es ofrecer arte unico en cada una de sus piezas.

## ejecutar proyecto

python manage.py runserver

### Author 
Brayan Rojas

*Version*
- update
- test
- function
- design
- delete
- error

Commandos

- vercerl link

- git clone 

##  Staick

Django

## Setting the Secret Key

Django requires a secret key for cryptographic signing to be set in the `DJANGO_SECRET_KEY` environment variable. This can be set in the web interface, or by running:

```bash
python manage.py runserver
```

## How it Works

Vercel detects Django's `manage.py` and uses that to find the WSGI entrypoint and the configuration for static files.

## Running Locally

```bash
uv sync
uv run python manage.py runserver
```

Your Django application is now available at `http://localhost:8000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&env=DJANGO_SECRET_KEY&envDescription=Secret%20key%20for%20Django%20cryptographic%20signing&demo-title=Django%20%2B%20Vercel&demo-description=Use%20Django%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)
