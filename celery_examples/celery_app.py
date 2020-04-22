import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_examples.settings")

app = Celery("celery_example")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_mail_every_10_sec': {
        'task': 'test_app.tasks.send_mail_task',
        'schedule': 10,
        'kwargs': {
            'message': "Hello from beat",
            'recipients': ['lapki@yahoo.com'],
            'subject': 'Scheduled message for you!'
        }
    }
}
