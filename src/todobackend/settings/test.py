from base import *
import os

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# The convention here is that, say if the 'MYSQL_USER' env variable is not found, then use 'todo' as default
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ.get('MYSQL_DATABASE','todobackend'),
    'USER': os.environ.get('MYSQL_USER','todo'),
    'PASSWORD': os.environ.get('MYSQL_PASSWORD','password'),
    'HOST': os.environ.get('MYSQL_HOST','localhost'),
    'PORT': os.environ.get('MYSQL_PORT','3306'),
  }
}
