from production import *



#MIDDLEWARE_CLASSES += ['base.settings.middleware.LatencySimulator']

DEBUG = True
TEMPLATE_DEBUG = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'base',
        'USER': 'baseuser',
        'PASSWORD': 'baseuserpass',
        'HOST': 'localhost',
        'PORT': ''
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)
