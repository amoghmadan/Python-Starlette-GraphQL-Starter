import graphene


class Hello(graphene.Mutation):
    """."""

    class Arguments:
        """."""

        name = graphene.String()

    name = graphene.String()

    @staticmethod
    async def mutate(root, info, **kwargs):
        """."""

        name = kwargs.get('name')

        return Hello(name=name)
