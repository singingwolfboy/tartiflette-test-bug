import pytest
from aiohttp.test_utils import TestClient


@pytest.mark.asyncio
async def test_hello_1(client: TestClient):
    query = """
        query {
            hello(name: "Alice")
        }
    """

    async with client.post("/graphql", json={"query": query}) as response:
        result = await response.json()
    assert "errors" not in result
    assert result["data"]["hello"] == "Hello Alice"


@pytest.mark.asyncio
async def test_hello_2(client: TestClient):
    query = """
        query {
            hello(name: "Bob")
        }
    """

    async with client.post("/graphql", json={"query": query}) as response:
        result = await response.json()
    assert "errors" not in result
    assert result["data"]["hello"] == "Hello Bob"
