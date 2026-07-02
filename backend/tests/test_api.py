import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_health(client):
    resp = await client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


@pytest.mark.asyncio
async def test_listar_defeitos(client):
    resp = await client.get("/api/defeitos/")
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_dashboard(client):
    resp = await client.get("/api/indicadores/dashboard")
    assert resp.status_code == 200
    data = resp.json()
    assert "total_defeitos" in data
    assert "total_lotes" in data
