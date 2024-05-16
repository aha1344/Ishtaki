import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')
SECRET_KEY = 'django-insecure-8cr-kuy3&(zdhhv0u1%zuc9z#m_l)3=9+a6fcudcs8z2woh(hs''django-insecure-8cr-kuy3&(zdhhv0u1%zuc9z#m_l)3=9+a6fcudcs8z2woh(hs'


DEBUG = False
ALLOWED_HOSTS = ["ishtaki.azurewebsites.net", '127.0.0.1']

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'report',
    'django_recaptcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DATABASES = {
#     'default': {
        
#         'ENGINE': 'mssql',
#         'NAME': 'db-ishtaki',
#         'USER': 'maf68',
#         'PASSWORD': 'Mhfaub2003',
#         'HOST':  'ishtaki-server.database.windows.net',  # Change to your server name
#         'PORT': '1433',  # Change to '5432' for PostgreSQL
#          'OPTIONS': {
#             'driver': 'ODBC Driver 18 for SQL Server',
#             'extra_params': 'TrustServerCertificate=yes',
#         },
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'Db',  
    #     # change name to database name on your laptop
    #     'USER': 'moham',  
    #     # change user to ur database user name on your laptop
    #     'PASSWORD': '123',  
    #     # password of your user
    #     'HOST': 'localhost',
    #     'PORT': '5432',  
    # }
}

ROOT_URLCONF = 'Capstone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Capstone.wsgi.application'

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# reCAPTCHA settings
RECAPTCHA_PUBLIC_KEY = '6Lf67qkpAAAAAH7rWvxRc8EW9T_YKDdwmUI_HCnN6Lf67qkpAAAAAH7rWvxRc8EW9T_YKDdwmUI_HCnN'
RECAPTCHA_PRIVATE_KEY = '6Lf67qkpAAAAAC-hYor-GdOGPmwjo3-i24q5FfGK6Lf67qkpAAAAAC-hYor-GdOGPmwjo3-i24q5FfGK'
