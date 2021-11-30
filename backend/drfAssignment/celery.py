from __future__ import absolute_import

import os
from celery import Celery
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfAssignment.settings')

app = Celery('sku_aggregator')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "trigger-crawl-glamorous": {
        "task": "run.spider",
        "schedule": crontab(minute="0", hour="12", day_of_week="1"),
        "args": ("glamorous-uk-crawl",) 
    },
    "trigger-crawl-europe361": {
        "task": "run.spider",
        "schedule": crontab(minute="0", hour="13", day_of_week="1"),
        "args": ("europe361_crawl",)
    }
}
