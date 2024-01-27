from django.db import models
from django import forms



class register(models.Model):
    Name=models.CharField(max_length=30)
    Email_address=models.EmailField()
    Mobile_Number=models.IntegerField()
    address=models.TextField()
    city=models.TextField()
    state=models.TextField()
    zip=models.IntegerField()

    