import os
from pathlib import Path
from dotenv import load_dotenv

"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# load environment variables from .env file located in the 
# BASE_DIR (where manage.py is located)
load_dotenv() 

# this .env file define what '.env' file to pick from the 'environments' folder
SELECTED_ENV = os.getenv("SELECTED_ENV")

print(f">>> Selected Environment for Deployment:  '{SELECTED_ENV}'")

# you might need one or all the different environments below. This allows to
# change the Project deployment without touching the code for it 
# (with or without Docker). Just set the environment variables in the files
# in folder "environments" accordingly.

if SELECTED_ENV == "prod":
    env_filename = ".env.prod"                  # production environment
elif SELECTED_ENV == "dev":
    env_filename = ".env.dev"                   # development environment
elif SELECTED_ENV == "local":
    env_filename = ".env.local"                 # local (with container)
elif SELECTED_ENV == "local":
    env_filename = ".env.local_wo_container"    # local (without container)
else: env_filename = ".env.local"

load_dotenv(dotenv_path = f"environments/{env_filename}")
print(">>> SELECTION: ", os.getenv("SELECTION"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print (">>>> PROJECT_DIR", PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG",False)
print(f">>> DEBUG = {DEBUG}")

# gets a list of allowed hosts
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",['localhost','0.0.0.0','127.0.0.1']).split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',    # library for doing beautiful html forms
    'crispy_bootstrap5',
    # if your app is not added here, your html templates won't be found!
    'app',
]

# By default, the "bootstrap4" template pack is commonly used, but you can 
# choose from "bootstrap3", "bootstrap4", or "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5' # For advanced customization

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

# note: added the DIRS templates for the authentication & permissions
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database Selection ----------------------------------------------------------
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if SELECTED_ENV in ['prod', 'dev', 'local']:
    # Use this if you want to use a PostgreSQL DB
    # check this for more help: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("POSTGRES_DB","fake_db"),
            'USER': os.getenv("POSTGRES_USER","fake_user"),
            'PASSWORD': os.getenv("POSTGRES_PASSWORD","fake_password"),
            
            # SUPER IMPORTANT!! the host should match the name of the 
            # docker database service ('app-db' in this case) or it won't work!
            'HOST': 'app-db', # or the ip address of your db server
            'PORT': os.getenv("POSTGRES_PORT","5432")
        }
    }

else: # selected environment is 'local_wo_container' (local without container)

    # this is the SQLite3 default development database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# If you have additional directories, configure them here
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'app', 'static'),
]

# Directory where static files will be collected to for deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirects to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# For testing only
# This will show the password reset information in the console
# In Prod this should be replaced by an email for the users
# More info here https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
