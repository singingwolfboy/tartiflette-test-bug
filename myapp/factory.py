from pathlib import Path

from aiohttp import web
from tartiflette import Engine
from tartiflette_aiohttp import register_graphql_handlers


def make_app() -> web.Application:
    app = register_graphql_handlers(
        web.Application(),
        engine=Engine(),
        engine_sdl=str(Path(__file__).parent / "graphql" / "sdl"),
        engine_modules=[
            "myapp.graphql.directives",
            "myapp.graphql.resolvers",
            "myapp.graphql.scalars",
        ],
        graphiql_enabled=True,
    )
    return app
