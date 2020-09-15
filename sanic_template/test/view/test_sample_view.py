import pytest


@pytest.mark.asyncio
async def test_index(test_client):
    resp = await test_client.get('/')
    assert resp.status == 200
