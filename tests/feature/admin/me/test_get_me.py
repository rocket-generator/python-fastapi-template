from fastapi.testclient import TestClient

from app.bootstrap.create_app import create_app

app = create_app(environment="test")

client = TestClient(app)


def test_get_me():
    response = client.post("/admin/auth/signin",
                           json={
                               "email": "test@example.com",
                               "password": "test",
                           })
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data

    access_token = response_data["access_token"]
    response = client.get("/admin/me",
                          headers={"Authorization": f"bearer {access_token}"})
    print("------")
    print(response.text)
    print("------")
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
