from rest_framework import serializers
from . import models

class Menuserializer(serializers.ModelSerializer):
    class Meta:
        model=models.Menu
        fields=['title','price','inventory']