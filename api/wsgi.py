import os
import sys

# Put project root on path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Use production settings by default on Vercel
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_website.production_settings")

from django.core.wsgi import get_wsgi_application
from vercel_wsgi import VercelWsgi

application = get_wsgi_application()
app = VercelWsgi(application)

def handler(request, response):
    return app(request, response)
