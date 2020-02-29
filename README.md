# restticketapi
This is a repo for my workshop at PyCon Namibia 2020

Overview
Django REST framework is a powerful and flexible toolkit for building Web APIs.
Requirements
# requirements.txt file included
 """html
 Python (3.7)
 asgiref==3.2.3
 Django==3.0.3
 djangorestframework==3.11.0
 pytz==2019.3
 sqlparse==0.3.0
It is only officially support the latest patch release of each Python and Django series.
"""
Installation
Install using pip...
pip install djangorestframework
Add 'rest_framework' and 'ticketapi' to your INSTALLED_APPS setting.
    INSTALLED_APPS = [
      ...
        'rest_framework',
        'ticketapi',
    ]

OUR TICKET API - EXAMPLE
Let's take a look at a quick example of using REST framework to build a simple ticket API for accessing participants details. Startup up a new project like so...
pip install django
pip install djangorestframework
django-admin startproject restticketapi .
python manage.py startapp ticketapi
./manage.py migrate
./manage.py createsuperuser
Now edit the ticketapi/models.py module in your app folder:
from django.db import models

# Create your models here.
class Ticket(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    organization = models.CharField(max_length=40)
    reason = models.CharField(max_length=200)
    
    def __str__(self):
         return self.firstname

Now create a file called ticketapi/serializers.py module in your app folder:
# Serializers define the API representation.
from rest_framework import serializers
from . models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
     
Now create a file called ticketapi/viewsets.py
# ViewSets define the view behavior.
from rest_framework import viewsets
from . import models
from . import serializers

class TicketViewset(viewsets.ModelViewSet):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer

Create a file called ticketapi/router.py
#Routers provide a way of automatically determining the URL conf.
from ticketapi.viewsets import TicketViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ticket', TicketViewset)

edit the urls file in the main project restticketapi/urls.py
# Wire up our API using automatic URL routing.
from django.contrib import admin
from django.urls import path, include
from . router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]

Now we're done. Let's run our server
./manage.py runserver
