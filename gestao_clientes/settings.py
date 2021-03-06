import os
from decouple import config
from dj_database_url import parse as dburl

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['gestao-clientes-rrgaya.herokuapp.com', 'localhost', '127.0.0.1']


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.google',
    'rest_framework',
    'bootstrapform',
    'cloudinary',

    'clientes',
    'home',
    'produtos',
    'vendas',
    'api',
    'accounts',
]

CLOUD_NAME_CLOUDINARY = config("CLOUD_NAME_CLOUDINARY")
API_KEY_CLOUDINARY = config("API_KEY_CLOUDINARY")
API_SERVICE_CLOUDINARY = config("API_SERVICE_CLOUDINARY")

CLOUDINARY = {
    'cloud_name' : CLOUD_NAME_CLOUDINARY,
    'api_key' : API_KEY_CLOUDINARY,
    'api_secret': API_SERVICE_CLOUDINARY
}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Meu Middleware
    'mymiddlewares.MetaData.MetaData'
]

ROOT_URLCONF = 'gestao_clientes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestao_clientes.wsgi.application'

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}


# DATABASES = {
#     'default': {
#     'ENGINE': config('DB_ENGINE'),
#     'NAME': config('DB_NAME'),
#     'USER': config('DB_USER'),
#     'PASSWORD': config('DB_PASSWORD'),
#     'HOST': config('DB_HOST'),
#     'PORT': config('DB_PORT'),
#   }
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    'statics',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL= '/clientes/list'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}

SENDGRID_API_KEY = config("SENDGRID_API_KEY")
SENDGRID_API_ID = config("SENDGRID_API_ID")

# EMAIL SETTINGS

# EMAIL_HOST = "smtp.sendgrid.net"
# EMAIL_HOST_USER = 'rrgaya'
# EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER =  config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_FROM = EMAIL_HOST_USER
EMAIL_SUBJECT_PREFIX = "[Project] "
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


# MANAGERS
ADMINS = [('Website Admin', 'rrgaya@gmail.com')]
MANAGERS = ADMINS + [('Website Manager', 'rrgaya@gmail.com')]