from rest_framework import serializers
from .models import Events


class eventsserializer(serializers.ModelSerializer):

    class Meta:
        fields = ["eventname","eventimage","date","text+"]