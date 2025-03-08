
from pathlib import Path
import os
import django_heroku
from environ import Env

from datetime import timedelta
env = Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

Env.read_env(os.path.join(BASE_DIR, '.env'))
ENVIRONMENT = env('ENVIRONMENT', default='production')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

if ENVIRONMENT == "development":
    PAYSTACK_SECRET_KEY = env('PAYSTACK_SECRET_KEY_TEST')
else:
    PAYSTACK_SECRET_KEY = env('PAYSTACK_SECRET_KEY_PROD')


# SECURITY WARNING: don't run with debug turned on in production!

CORS_ALLOWED_ORIGINS  = [
    'https://hlsnigeria-e0c4b5df87f5.herokuapp.com',  # Your Heroku deployment
    'http://127.0.0.1:8000',  # Localhost for testing on local development server
    'https://hls.com.ng',  # Production or main domain if hosted here
    'https://www.hls.com.ng',
    'https://hlsnew.netlify.app',
    'http://localhost:5173',
    'https://hls-vr1z.onrender.com'  # Render deployment domain
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'headers',  # Add this line to allow the 'headers' field
]
# Application definition
CSRF_ALLOWED_ORIGINS = [
    "https://hls.com.ng",           # Your main domain
    "https://www.hls.com.ng",
    "https://hlsnew.netlify.app",
    "https://hls-vr1z.onrender.com"  
    "http://localhost:5173"
]

CORS_ORIGINS_WHITELIST = [
    "https://hls.com.ng",           # Your main domain
    "https://www.hls.com.ng",
    "https://hlsnew.netlify.app",
    "https://hls-vr1z.onrender.com",
    "http://localhost:5173"
]

CSRF_TRUSTED_ORIGINS = [
    "https://hls.com.ng",           # Your main domain
    "https://www.hls.com.ng",
    "https://hls-vr1z.onrender.com"  # Render deployment domain
    "http://localhost:5173"
]

CSRF_COOKIE_SECURE = True  # Ensures cookie is only sent over HTTPS
CSRF_COOKIE_SAMESITE = 'None'  # Allows cross-site cookies; required for CORS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'storages',
    'corsheaders',
    'home',
    'user',
    'dashboard',
    'blog',
    'api',
    'podcasts',
    'NT_gallery',
    'crispy_forms',
    'crispy_bootstrap4',
    'widget_tweaks',
]
# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HLSBACK.urls'

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

WSGI_APPLICATION = 'HLSBACK.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


if ENVIRONMENT == "development":
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR/'db.sqlite3',
        }
    }
else: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            # 'NAME': 'dbuap6sb6d2e99',
            # 'USER': 'udrt2vnk83cb27',
            # 'PASSWORD': 'p695d0b8f20d05a6899f36c244b7262ec9fc22d8417d98e5fa61a31a70ac1f80b',
            # 'HOST': 'c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com',
            # 'PORT': '5432',
            # 'OPTIONS': {
            #     'autocommit': True,
            #     'sslmode': 'require',
            # }
        }
    }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dbuap6sb6d2e99',
#         'User': 'udrt2vnk83cb27',
#         'PASSWORD': 'p695d0b8f20d05a6899f36c244b7262ec9fc22d8417d98e5fa61a31a70ac1f80b',
#         'HOST': 'c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com',
#         'PORT': '5432'
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
    # {
    #     'NAME': 'HLSBACK.validators.CustomPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR , 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AWS S3 Storage settings
AWS_ACCESS_KEY_ID = 'AKIATFBMO53EKIXSNNUY'  # Replace with your AWS access key ID
AWS_SECRET_ACCESS_KEY = 'vf+xxthS0G7T4l37rtvmYdzhiR4yEZQS3yXHIfsz'  # Replace with your AWS secret access key
AWS_STORAGE_BUCKET_NAME = 'hlsnigeriabucket'  # Replace with your S3 bucket name

# Use AWS S3 for storing media files
AWS_S3_REGION_NAME = 'eu-north-1'  
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"

# Django-Storages settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# URL to use for media files (pointing to S3)
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"

# Optional settings for caching and other S3 optimizations
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # Cache the file for a day
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'home:home'

LOGIN_URL = 'user:login'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server for Gmail
EMAIL_PORT = 587  # Port for TLS
EMAIL_USE_TLS = True  # Use TLS encryption for security
EMAIL_HOST_USER = 'folajimiopeyemisax13@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'zzitfwiibuujeltz'  # Your Gmail app password (not the regular Gmail password)
DEFAULT_FROM_EMAIL = 'folajimiopeyemisax13@gmail.com'  # Same email as EMAIL_HOST_USER

# dont forget admin honeypot
# ACCOUNT_USERNAME_BLACKLIST = ['admin', 'sakamanje']

django_heroku.settings(locals())
