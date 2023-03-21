from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context
from django.template.loader import get_template
from backend.settings import EMAIL_HOST_USER
from api.models import Events,Alumni
from django.contrib.auth.models import User
from django.template.loader import render_to_string

@receiver(post_save, sender = Events)
def send_event_mail(sender,instance,**kwargs):
    htmly = "email.html"
    recipientlist = list(User.objects.all().values_list("email", flat=True))
    html_content = render_to_string(htmly,{'heading':instance.eventname,
                                           'body':instance.text_body,
                                           'date':instance.date,
                                           'Location':instance.location,
                                           'image.url':instance.eventimage.url})
    mail = EmailMultiAlternatives(
         subject=instance.eventname,
         body = html_content,
         from_email=EMAIL_HOST_USER,
         bcc = recipientlist,
         reply_to=[EMAIL_HOST_USER],
      )

    mail.content_subtype = "html"
    mail.send()
          
        
        