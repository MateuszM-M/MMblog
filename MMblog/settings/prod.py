from MMblog.settings.base import *
import os


DEBUG = False

ALLOWED_HOSTS = ['m-m-blog.herokuapp.com',
                '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dft776ct0j3g73',
        'USER': 'mivehibudwxigh',
        'PASSWORD': os.environ.get('MMBLOG_DB_PASSWORD'),
        'HOST': 'ec2-54-154-101-45.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}


AWS_ACCESS_KEY_ID = os.environ.get('MMBLOG_S3_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('MMBLOG_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'bblog2'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_HOST = "s3.us-east-2.amazonaws.com" 
AWS_S3_REGION_NAME="us-east-2"

AWS_QUERYSTRING_AUTH = False


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

