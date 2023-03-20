from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context
from django.template.loader import get_template
from backend.settings import EMAIL_HOST_USER
from api.models import Events,Alumni
from rest_framework import serializers


@receiver(post_save,sender = Events)
def send_event_mail(instance,**kwargs):
    recipientlist = Alumni.objects.all()
    event = instance
    serializing_result = serializers.serialize('json',event)
    event_serialized = serializing_result[1:-1]
    message =get_template("email.html").render(Context({
        'event':event_serialized
    }))
    for r in recipientlist:
        mail = EmailMessage(
            subject="event.eventname",
            body = message,
            from_email=EMAIL_HOST_USER,
            to = [r.email],
            reply_to=[EMAIL_HOST_USER],
        )
        mail.content_subtype = "html"
        mail.send()
        
        