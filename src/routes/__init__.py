from starlette.routing import Mount

from . import graphql

routes = [
    Mount('/graphql', routes=graphql.routes),
]
