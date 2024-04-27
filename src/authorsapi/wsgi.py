"""
WSGI config for authorsapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# TODO: Change inprod
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authorsapi.settings.local")

application = get_wsgi_application()
