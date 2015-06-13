from production import *



MIDDLEWARE_CLASSES += ['base.settings.middleware.LatencySimulator']

DEBUG = True
TEMPLATE_DEBUG = True

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
    'localhost:9000',
)
