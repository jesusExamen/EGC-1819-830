ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
]
STATIC_URL = '/static/'

APIS = {
    'authentication': 'http://127.0.0.1:8000',
    'base': 'http://127.0.0.1:8000',
    'booth': 'http://127.0.0.1:8000',
    'census': 'http://127.0.0.1:8000',
    'mixnet': 'http://127.0.0.1:8000',
    'postproc': 'http://127.0.0.1:8000',
    'store': 'http://127.0.0.1:8000',
    'visualizer': 'http://127.0.0.1:8000',
    'voting': 'http://127.0.0.1:8000',
}

BASEURL = 'http://127.0.0.1:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'USER': 'decide',
        'HOST': 'localhost',
        'PORT': '5432',
        'PASSWORD': 'decide'

    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256

STATIC_URL = '/static/'