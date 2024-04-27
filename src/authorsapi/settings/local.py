from .base import * #noqa
from .base import env

SECRET_KEY = env("DJANGO_SCRET", default="RDDR4XSTB8QAqM7IJ9smEh9FczNHHv0r1iyxTg4HdFMjK_xhzlI", )
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGIN = ["http//localhost:8080"]