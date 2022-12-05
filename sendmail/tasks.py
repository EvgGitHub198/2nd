from config.celery import app
from django.core.mail import send_mail
from .models import Mail
from .service import send


@app.task
def send_spam_email(user_email):
    send(user_email)

@app.task
def send_beat_email():
    for mail in Mail.objects.all():
        send_mail(
            'Hello',
            'Thanks for subscribing!',
            'mishagon02@gmail.com',
            [mail.email],
            fail_silently=False,
        )
