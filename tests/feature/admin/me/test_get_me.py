from fastapi.testclient import TestClient

from app.bootstrap.create_app import create_app
from ...utilities import get_access_token

app = create_app(environment="test")

client = TestClient(app)


def test_get_me():
    access_token = get_access_token(client)
    response = client.get("/admin/me",
                          headers={"Authorization": f"bearer {access_token}"})
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
