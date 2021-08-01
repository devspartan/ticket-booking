import graphene
from graphene_django import DjangoObjectType, fields
from .models import *
from graphene import relay
from .graphqlTypes import *
from .mutations import *


class Query(graphene.ObjectType):
    get_tickets = graphene.List(TicketsType)
    get_screens = graphene.List(ScreenType)
    get_seats = graphene.List(SeatType, booked=graphene.Boolean(), screen = graphene.ID())

    def resolve_get_screens(root, info):
        return Screen.objects.all()
    
    def resolve_get_seats(root, info, booked=None, screen=None):
        return Seat.objects.all()

class Mutation(graphene.ObjectType):
    update_seat = UpdateSeatMutation.Field()
    create_seat = CreateSeatMutation.Field()

    book_ticket = BookTicketMutation.Field()