from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from starlette.routing import Route

import settings
from schema import schema

routes = [
    Route('/', endpoint=GraphQLApp(schema=schema, executor_class=AsyncioExecutor, graphiql=settings.GRAPHIQL)),
]
