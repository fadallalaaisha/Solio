from django.db import models
from django.db.models.fields import CharField
from django.db.models.enums import Choices

#from django.http import request

class Customer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    image=models.ImageField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=13)
    id_number=models.PositiveSmallIntegerField()
    # nationlities=((u'K',u'Kneya'),
    # (u'S',u'Sudan'),
    # (u'Sm',u'Somali'),)

    # nationality=models.CharField(max_length=1,choices=nationlities)
    genders=((u'F',u'Female'),
    (u'M',u'Male'),
    (u'O',u'Others'),
    )
    gender=models.CharField(max_length=1,choices=genders)
    age=models.PositiveSmallIntegerField()
    location=models.CharField(max_length=12)

