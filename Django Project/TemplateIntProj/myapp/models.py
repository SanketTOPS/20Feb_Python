from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.BigIntegerField()
    subject=models.CharField(max_length=100)
    msg=models.TextField()