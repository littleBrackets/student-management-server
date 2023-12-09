from django.db import models

# Create your models here.

class SignUP(models.Model):
    idx = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    def _str_(self):
        return self.title
    
class School(models.Model):
    idx = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    contact = models.CharField(max_length=120)    
    def _str_(self):
        return self.title