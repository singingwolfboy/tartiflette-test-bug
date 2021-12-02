import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient, TestServer
from tartiflette.schema.registry import SchemaRegistry

from myapp import make_app

# https://github.com/pytest-dev/pytest-asyncio/issues/170#issuecomment-706114516
@pytest.fixture
def loop(event_loop):
    return event_loop


@pytest.fixture
def app() -> web.Application:
    # uncomment me to see a different failure!
    # SchemaRegistry.clean()
    return make_app()


@pytest.fixture
async def client(aiohttp_client, app: web.Application) -> TestClient:
    return await aiohttp_client(TestServer(app))
