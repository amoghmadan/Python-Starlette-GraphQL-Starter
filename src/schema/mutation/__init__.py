import graphene
from .hello import Hello


class Mutation(graphene.ObjectType):
    """."""

    hello = Hello.Field()
