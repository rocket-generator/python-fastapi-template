from fastapi.testclient import TestClient


def get_access_token(client: TestClient) -> str:
    response = client.post("/admin/auth/signin",
                           json={
                               "email": "test@example.com",
                               "password": "test",
                           })
    response_data = response.json()
    return response_data["access_token"]
