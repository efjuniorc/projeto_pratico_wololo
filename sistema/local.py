from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.getcwd(), 'sqlite3.db'),
        'HOST': '',
        'PORT': '', }
}
