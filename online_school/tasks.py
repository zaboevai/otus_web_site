from celery import shared_task
from django.core.mail import send_mail

from otus_web_site.settings import DEFAULT_FROM_EMAIL


@shared_task
def send_subscribe_email(email: str):
    return send_mail(subject='Подписка на BrainStorm',
                     message='Поздравляем вы успешно подписаны на рассылку новостей',
                     from_email=DEFAULT_FROM_EMAIL,
                     recipient_list=[email],
                     )
