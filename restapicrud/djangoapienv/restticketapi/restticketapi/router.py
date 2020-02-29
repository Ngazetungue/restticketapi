
from ticketapi.viewsets import TicketViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ticket', TicketViewset)


