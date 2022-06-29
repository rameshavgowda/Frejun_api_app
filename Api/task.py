from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from Frejun import settings

@shared_task(bind=True)
def mail_fun(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = 'project assigned'
        message = 'hi please check the company workspace you have a project to work'
        to_mail = user.email
        send_mail (
            subject=mail_subject,
            message=message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_mail],
            fail_silently= True,
        )
    return 'Done'