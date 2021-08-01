from graphene_django.debug import DjangoDebug
import graphene

from tickets import schema
import tickets

class Query(tickets.schema.Query):
    debug = graphene.Field(DjangoDebug, name="_debug")

class Mutation(tickets.schema.Mutation):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation)