"""
WSGI config for hindi_land project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hindi_land.settings')

application = get_wsgi_application()
