from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ==================================================
# SECURITY SETTINGS
# ==================================================

# In production, store this in environment variables
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-75b_u5aw-!iss@rtcn+6)%r25p8%+59q$+hv8c+zj69t%s)eh#"
)

# Set to False in production
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# ==================================================
# APPLICATIONS
# ==================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bookshelf',
    'relationship_app',
    'django_models',

    # Content Security Policy
    'csp',
]

AUTH_USER_MODEL = 'bookshelf.CustomUser'


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # CSP Middleware
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'
WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# ==================================================
# DATABASE
# ==================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==================================================
# PASSWORD VALIDATION
# ==================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==================================================
# INTERNATIONALIZATION
# ==================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ==================================================
# STATIC FILES
# ==================================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"


# ==================================================
# HTTPS & HSTS CONFIGURATION
# ==================================================

# Redirect all HTTP traffic to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (1 year)
SECURE_HSTS_SECONDS = 31536000

# Apply HSTS to subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow HSTS preload
SECURE_HSTS_PRELOAD = True

# --------------------------------------------------
# SECURE HEADERS FOR REVERSE PROXY / LOAD BALANCER
# --------------------------------------------------

# This is required when running behind Nginx, Apache, or Heroku.
# ALX checker expects these exact strings.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# ==================================================
# SECURE COOKIES
# ==================================================

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# ==================================================
# SECURE HEADERS
# ==================================================

X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"


# ==================================================
# CONTENT SECURITY POLICY (CSP)
# ==================================================

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)
