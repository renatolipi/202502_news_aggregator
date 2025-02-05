import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_aggregator.settings')


app = Celery('news_aggregator')


# namespace='CELERY' means all celery-related config keys should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(['nba'])
