from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR+'/'+'sqlite3.db',
        'HOST': '',
        'PORT': '', }
}
