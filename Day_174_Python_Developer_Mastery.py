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

    def test_create_and_read_own_items(client: TestClient):
    """Test creating items and ensuring a user only sees their own items."""
    user_a_headers = get_auth_headers(client, "usera@example.com")
    user_b_headers = get_auth_headers(client, "userb@example.com")

    # User A creates an item
    create_res = client.post(
        "/items/",
        json={"title": "User A Secret Plan", "description": "Top secret"},
        headers=user_a_headers
    )
    assert create_res.status_code == 201
    created_data = create_res.json()
    assert created_data["title"] == "User A Secret Plan"
    assert "owner_id" in created_data

    # User A sees their own item
    user_a_items = client.get("/items/", headers=user_a_headers).json()
    assert len(user_a_items) == 1
    assert user_a_items[0]["title"] == "User A Secret Plan"

    # User B should see an empty list (isolation check)
    user_b_items = client.get("/items/", headers=user_b_headers).json()
    assert len(user_b_items) == 0


def test_cross_user_delete_forbidden(client: TestClient):
    """Test that User B gets 403 Forbidden when trying to delete User A's item, while User A succeeds."""
    owner_headers = get_auth_headers(client, "owner@example.com")
    intruder_headers = get_auth_headers(client, "intruder@example.com")

    # Owner creates an item
    create_res = client.post(
        "/items/",
        json={"title": "Owner Item"},
        headers=owner_headers
    )
    item_id = create_res.json()["id"]

    # Intruder attempts to delete Owner's item -> must fail with 403
    forbidden_res = client.delete(f"/items/{item_id}", headers=intruder_headers)
    assert forbidden_res.status_code == 403

    # Owner deletes their own item -> must succeed with 204
    delete_res = client.delete(f"/items/{item_id}", headers=owner_headers)
    assert delete_res.status_code == 204