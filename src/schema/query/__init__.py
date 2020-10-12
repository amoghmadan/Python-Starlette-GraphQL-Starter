import graphene


class Query(graphene.ObjectType):
    """."""

    hello = graphene.String()

    @staticmethod
    async def resolve_hello(root, info):
        """."""

        return 'World'
