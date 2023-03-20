import uuid
from django.db import models


class Alumnimanager(models.Manager):
    def create_manager(self,name:str,email) -> 'Alumni':
        if not name:
            raise ValueError('Alumni must have a name!')
        if not email:
            raise ValueError('Alumni must have an email')
        
        alumni = self.model()
        alumni.name = name
        alumni.email = email
        alumni.save()

        return alumni
    
class Alumni(models.Model):
    name = models.CharField(max_length=75,blank=False)
    email = models.EmailField(blank=False,unique=True)
    objects = Alumnimanager()

    def __str__(self):
        return self.name
    
class Eventsmanager(models.Manager):
    def create_event(self,eventname:str,date_:str,*args) -> 'Events':
        if not eventname:
            raise ValueError('Event must have a name!')
        if not date_:
            raise ValueError('Event must have a date!')
        
        event = self.model(args)
        event.eventname = eventname
        event.date_ = date_
        event.save()
        return event
        

    
class Events(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    eventname = models.CharField(max_length=50,blank=False)
    eventimage = models.ImageField(upload_to='events',blank=True,null = True)
    date = models.DateField(blank=False)
    text_body = models.TextField(max_length=255,blank=True,null=True)
    location = models.TextField(max_length=100,blank=True,null=True)
    objects = Eventsmanager
    
    def __str__(self):
        return self.eventname