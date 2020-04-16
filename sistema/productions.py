from .settings import *

DEBUG = False

ALLOWED_HOSTS += ['157.245.212.104']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projeto_wololo',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': 'localhost',
        'PORT': '3306', }
}