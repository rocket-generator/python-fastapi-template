from fastapi.testclient import TestClient
from app.bootstrap.create_app import create_app
app = create_app(environment="test")

client = TestClient(app)


def test_read_main():
    response = client.post("/admin/auth/signin", json={
        "email": "test@example.com",
        "password": "test",
    })
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
