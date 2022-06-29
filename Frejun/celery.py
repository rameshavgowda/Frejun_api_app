from __future__ import absolute_import,unicode_literals
import os
from urllib.request import Request
from celery import Celery
from django.conf import settings
from pytz import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Frejun.settings')

app = Celery('Frejun')
app.conf.enable_utc = False

app.conf.update(timezone= 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

#celery beat settings

app.autodiscover_tasks()
def debug_task(self):
    print(f'Request:{self.request!r}')