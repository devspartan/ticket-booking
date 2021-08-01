import graphene
from graphene import relay
from graphql_relay import from_global_id
from graphql import GraphQLError
from .graphqlTypes import *
from .models import *



class UpdateSeatMutation(relay.ClientIDMutation):
    seat = graphene.Field(SeatType, required=False)

    class Input:
        id = graphene.ID()
        seat_id = graphene.String(required=False)
    
    @staticmethod
    def mutate_and_get_payload(root, info, id=None, seat_id=None):
        obj = None
        try:
            obj = Seat.objects.get(id=from_global_id(id)[1])
        except:
            raise GraphQLError("Object not found")
        
        obj.seat_id = seat_id
        obj.save()

        return UpdateSeatMutation(seat=obj)


class CreateSeatMutation(relay.ClientIDMutation):
    msg = graphene.String()
    class Input:
        st_alpha = graphene.String(required=True)
        st_num = graphene.Int(required=True)
        screen = graphene.ID(required=True)
    
    @staticmethod
    def mutate_and_get_payload(root, info, st_alpha, st_num, screen):

        alpha = ['A', 'B', 'C', 'D',]
        
        st = alpha.index(st_alpha)

        for st in range(st, len(alpha)):
            for i in range(1, 5):
                seat_id = alpha[st] + str(i)                
                seat = Seat.objects.create(seat_id=seat_id, screen=Screen.objects.get(id=from_global_id(screen)[1]))
                
        return CreateSeatMutation(msg="Success")
    
class BookTicketMutation(relay.ClientIDMutation):
    # ticket = graphene.Field(TicketsType)
    msg = graphene.String()

    class Input: 
        username = graphene.String(required=True)
        seat = graphene.ID(required=True)
        show = graphene.ID(required=True)
        
    @classmethod
    def validateInputs(username, seat, show):
        if username is None:
            raise GraphQLError("username is not provided")
        
        if seat is None:
            raise GraphQLError("Seat is not provided")
        elif not Seat.objects.filter(id=from_global_id(seat)[1]).exists:
            raise GraphQLError("Invalid seat id!")
        
        if show is None:
            raise GraphQLError("Show is not provided")
        elif not Show.objects.filter(id=from_global_id(show)[1]).exists:
            raise GraphQLError('Show does not exist')

    @classmethod
    def mutate_and_get_payload(root, info, username=None, seat=None, show=None):

        root.validateInputs(username, seat, show)

        ticket_id = username + Seat.objects.get(id=from_global_id(seat)[1])
        print(ticket_id, "ticket id")
        # tckt = Ticket.objects.create(username=username, )

        return BookTicketMutation(msg="Hello")