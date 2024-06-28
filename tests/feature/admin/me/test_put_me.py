from fastapi.testclient import TestClient

from app.bootstrap.create_app import create_app
from ...utilities import get_access_token

app = create_app(environment="test")

client = TestClient(app)


def test_put_me():
    access_token = get_access_token(client)

    response = client.put("/admin/me",
                          json={
                              "email": "test2@example.com",
                              "password": "test2",
                          },
                          headers={"Authorization": f"bearer {access_token}"})
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert response_data["email"] == "test2@example.com"

    response = client.post("/admin/auth/signin",
                           json={
                               "email": "test2@example.com",
                               "password": "test2",
                           })
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
