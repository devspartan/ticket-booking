from graphene_django.debug import DjangoDebug
import graphene

from tickets import schema

class Query(schema.Query):
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query)