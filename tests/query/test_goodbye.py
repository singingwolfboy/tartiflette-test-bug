import pytest
from aiohttp.test_utils import TestClient


@pytest.mark.asyncio
async def test_goodbye(client: TestClient):
    query = """
        query {
            goodbye(name: "Bob")
        }
    """

    async with client.post("/graphql", json={"query": query}) as response:
        result = await response.json()
    assert "errors" not in result
    assert result["data"]["goodbye"] == "Goodbye Bob"
