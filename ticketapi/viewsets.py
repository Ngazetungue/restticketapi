
from rest_framework import viewsets
from . import models
from . import serializers

class TicketViewset(viewsets.ModelViewSet):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer


     
