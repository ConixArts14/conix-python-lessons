from fastapi.testclient import TestClient

def get_auth_headers(client: TestClient, email: str, password: str = "testpass123") -> dict:
    """Helper to register a user, log in, and return the Bearer authorization header."""
    client.post("/auth/register", json={"email": email, "password": password})
    login_res = client.post(
        "/auth/token",
        data={"username": email, "password": password}
    )
    token = login_res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_read_users_me_authenticated(client: TestClient):
    """Test that /auth/me returns the logged-in user's profile."""
    headers = get_auth_headers(client, "me@example.com")
    response = client.get("/auth/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "me@example.com"
    assert "id" in data

def test_protected_routes_require_token(client: TestClient):
    """Test that /auth/me and /items/ reject requests without a Bearer token."""
    me_res = client.get("/auth/me")
    assert me_res.status_code == 401

    items_res = client.get("/items/")
    assert items_res.status_code == 401

