from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    contact_no= models.CharField(max_length=15)
