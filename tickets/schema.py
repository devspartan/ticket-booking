import graphene
from graphene_django import DjangoObjectType, fields
from .models import *

class TicketsType(DjangoObjectType):
    class Meta:
        model = Ticket
        fields = ['ticket_no', 'seat_np']

class Query(graphene.ObjectType):
    get_tickets = graphene.List(TicketsType)
