"""
WSGI config for ieee project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/opt/ieeedtu/IEEE-App-Service/')
os.environ["DJANGO_SETTINGS_MODULE"] = "ieee.settings"

application = get_wsgi_application()
