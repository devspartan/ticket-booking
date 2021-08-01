import graphene
from graphene_django import DjangoObjectType, fields
from .models import *
from graphene import relay


class TicketsType(DjangoObjectType):
    class Meta:
        model = Ticket

class ScreenType(DjangoObjectType):

    class Meta: 
        model = Screen
        fields = ('__all__')
        interfaces = (relay.Node,)

class SeatType(DjangoObjectType):
    class Meta:
        model = Seat
        fields = ('__all__')
        interfaces = (relay.Node,)