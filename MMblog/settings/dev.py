from MMblog.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['m-m-blog.herokuapp.com', 
                '127.0.0.1',
                '.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

