# flake8: noqa
import os

from rdrf.settings import *
import rotes


FALLBACK_REGISTRY_CODE = "rotes"
LOCALE_PATHS = env.getlist("locale_paths", ['/data/translations/locale'])

# Adding this project's app first, so that its templates overrides base templates
INSTALLED_APPS = [
    FALLBACK_REGISTRY_CODE,
] + INSTALLED_APPS

ROOT_URLCONF = '%s.urls' % FALLBACK_REGISTRY_CODE

SEND_ACTIVATION_EMAIL = False

PROJECT_TITLE = env.get("project_title", "Prince Charles Ortho Registry")
PROJECT_TITLE_LINK = "login_router"

# Registration customisation (if any) goes here
# REGISTRATION_CLASS = "rotes.custom_registration.CustomRegistration"

VERSION = env.get('app_version', '%s (rotes)' % rotes.VERSION)
