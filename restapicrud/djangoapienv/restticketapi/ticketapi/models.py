
from django.db import models

# Create your models here.
class Ticket(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    organization = models.CharField(max_length=50)
    reason = models.CharField(max_length=200)
    
    def __str__(self):
        return self.firstname


