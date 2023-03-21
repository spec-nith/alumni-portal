import uuid
from django.db import models


class Alumni(models.Model):
    name = models.CharField(max_length=75,blank=False)
    email = models.EmailField(blank=False,unique=True)


    def __str__(self):
        return self.name
    


    
class Events(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    eventname = models.CharField(max_length=50,blank=False)
    eventimage = models.ImageField(upload_to='events',blank=True,null = True)
    date = models.DateField(blank=False)
    text_body = models.TextField(max_length=255,blank=False)
    location = models.TextField(max_length=100,blank=False)

    
    def __str__(self):
        return self.eventname