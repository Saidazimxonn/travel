"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from decouple import config
from pathlib import Path  

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w1p8=hty)%s*f#8icdf9ys^749thcrsqcdhp-%2@p%)x&wv@2+'
DEBUG = True
# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = ['*']
GOOGLE_RECAPTCHA_SECRET_KEY = '6Lf9AQUiAAAAAKBF5OwZONldS_obn8Nnvu77-R-C'
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'active_link',
    #Create APP
    'frontend',
    'management',
    'django_ckeditor_5',
     'admin_reorder',
     'snowpenguin.django.recaptcha3',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]
# ADMIN_REORDER = (
#     # Keep original label and models
#     'sdddddddf',

  

#     # Reorder app models
#     {'app': 'management',  'label': 'group1', 'models': ('Managment', 'Sections','RegionalCenters')},

  
# )

ROOT_URLCONF = 'config.urls'
# from management.models import DocFile
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
                'django.template.context_processors.i18n', 
                #add context processors
                'management.context_processor.extras'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'samcity2',
#         'USER': 'said_azim',
#         'PASSWORD':'59764172',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True



gettext = lambda s: s
LANGUAGES = (
    ('uz',  gettext('Uzbek')),
    ('ru',  gettext('Russian')),
    ('en',  gettext('English')),
    
)
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

#STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CKEDITOR

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
# CKEDITOR_CONFIGS = {
#     # 'default' :{
#     #     'extraPlugins':'codesnippet',
#     #     'toolbar':'full'
#     # },
#     #     'default': {
#     #     'toolbar': 'Full',
#     #     'height': 300,
#     #     'width': '100%',
#     #     'removePlugins': 'stylesheetparser',
#     #     'extraAllowedContent': 'iframe[*]',
#     # },

    
# }

# CKEDITOR_CONFIGS = {
#     'default': {
#         'skin': 'moono',
#         # 'skin': 'office2013',
#         'toolbar_Basic': [
#             ['Source', '-', 'Bold', 'Italic']
#         ],
#         # 'toolbar_YourCustomToolbarConfig': [
#         #     {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#         #     {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#         #     {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
#         #     {'name': 'forms',
#         #      'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#         #                'HiddenField']},
#         #     '/',
#         #     {'name': 'basicstyles',
#         #      'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#         #     {'name': 'paragraph',
#         #      'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#         #                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#         #                'Language']},
#         #     {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#         #     {'name': 'insert',
#         #      'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#         #     '/',
#         #     {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
#         #     {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#         #     {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#         #     {'name': 'about', 'items': ['About']},
#         #     '/',  # put this to force next toolbar on new line
#         #     {'name': 'yourcustomtools', 'items': [
#         #         # put the name of your editor.ui.addButton here
#         #         'Preview',
#         #         'Maximize',
#         #         'Youtube',
               

#         #     ]},
#         # ],
#         # 'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
#         # # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
#         # # 'height': 291,
#         # # 'width': '100%',
#         # # 'filebrowserWindowHeight': 725,
#         # # 'filebrowserWindowWidth': 940,
#         # # 'toolbarCanCollapse': True,
#         # # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#         # 'tabSpaces': 4,
#         # 'extraPlugins': ','.join([
#         #     'uploadimage', # the upload image feature
#         #     # your extra plugins here
#         #     'div',
#         #     'autolink',
#         #     'autoembed',
#         #     'embedsemantic',
#         #     'autogrow',
#         #     # 'devtools',
#         #     'widget',
#         #     'lineutils',
#         #     'clipboard',
#         #     'dialog',
#         #     'dialogui',
#         #     'elementspath',
#         #     'youtube'
#         #  ]),
#     }
# }   
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

TEXT_ADDITIONAL_TAGS = ('iframe',)
TEXT_ADDITIONAL_ATTRIBUTES = ('scrolling', 'allowfullscreen', 'frameborder', 'src', 'height', 'width')
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': '100%',
        'removePlugins': 'stylesheetparser',
        'extraAllowedContent': 'iframe[*]',
    },
   
}
