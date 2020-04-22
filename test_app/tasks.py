import time
from typing import List

from django.core.mail import send_mail

from celery_examples.celery_app import app


@app.task
def send_mail_task(subject: str, message: str, recipients: List[str]):
    # Simulate huge delay
    time.sleep(5)

    send_mail(
        subject,
        message,
        'from@example.com',
        recipients,
        fail_silently=False,
    )
