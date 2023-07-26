from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage


# @shared_task
def send_email_message(message: str, subject: str):
    """
    Метод для отправки сообщения менеджеру на email
    с контактными данными клиента.
    :param message:
    :param subject:
    :return Bool:
    """
    msg = EmailMessage(
        subject, message, to=[settings.EMAIL_MANAGER], from_email=settings.EMAIL_HOST_USER
    )
    msg.content_subtype = 'html'
    try:
        msg.send()  # отправка сообщения на EMAIL_MANAGER
    except Exception as ex:
        print(ex)
        return False
    return True
