from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%dy9s*gx(-h1)s$wm0_3felvl-3kbpv$*)bg-08nyj4v5u#)_p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'rest_framework',
    'drf_yasg',

    # custom apps
    'home',
    'users',
    'events',
    'meetings',
    'interactive_elements',
    'reports',
    'courses',
    'notifications',
    'documents',
    'departments',

    # allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.github',

    # crispy forms apps
    'crispy_forms',
    'crispy_bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'courses.middleware.LessonAccessMiddleware',

]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'yandex': {
        'SCOPE': [
            'login:email',
            'login:info',
            'login:avatar',
        ],
        'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'OAUTH_PKCE_ENABLED': True,
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
        'AUTH_PARAMS': {'allow_signup': 'true'},
        'OAUTH_PKCE_ENABLED': True,
    },
}

OAUTH_PROVIDERS = [
    {
        'provider': 'yandex',
        'name': 'Yandex',
        'client_id': 'c4885d8267a049929068e28f02ddd48d',
        'secret': '36a4c9c8c1e546748c347e1aa634b2e2',
        'key': ''
    },
    {
        'provider': 'github',
        'name': 'GitHub',
        'client_id': 'Iv23liw6mKXJDqe6JV0e',
        'secret': '0ebda726ca58385085da158b7d267453808d5298',
        'key': ''
    }
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nafi',
        'USER': 'postgres',
        'PASSWORD': '0120GiFZ',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

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
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский'),
]

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# daily.co settings
DAILY_CO_API_KEY = '65d12c6c88b7188adc64a5942b4a0962c76695523ac22c97bd0eaaa14afbbd4e'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1

AUTH_USER_MODEL = 'users.CustomUser'

ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSignupForm',
    'login': 'users.forms.CustomLoginForm',
}

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "kinopoisk.y4ndex3@yandex.ru"
EMAIL_HOST_PASSWORD = "hlavcjkvegbuqhge"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = 'Ilimetr. '
DEFAULT_FROM_EMAIL = "kinopoisk.y4ndex3@yandex.ru"

SERVER_EMAIL = "kinopoisk.y4ndex3@yandex.ru"

TINYMCE_JS_URL = os.path.join(STATIC_URL, "https://cdn.tiny.cloud/1/no-origin/tinymce/7.1.2-65/tinymce.min.js")

TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
               "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
               "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
               "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
               "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
               "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "es_ES",  # To force a specific language instead of the Django current language.
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True