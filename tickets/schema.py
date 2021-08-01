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


class Query(graphene.ObjectType):
    get_tickets = graphene.List(TicketsType)
    get_screens = graphene.List(ScreenType)

    def resolve_get_screens(root, info):
        return Screen.objects.all()