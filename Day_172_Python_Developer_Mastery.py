from fastapi.testclient import TestClient

def test_register_user(client: TestClient):
    """Test successful user registration."""
    response = client.post(
        "/auth/register",
        json={"email": "testuser@example.com", "password": "strongpassword123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "testuser@example.com"
    assert "id" in data

def test_register_duplicate_user(client: TestClient):
    """Test that registering the same email twice fails with 400."""
    # First registration
    client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "password123"}
    )
    # Second registration with same email
    response = client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "password123"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_login_success(client: TestClient):
    """Test successful login and JWT token return using OAuth2 form data."""
    # Register user first
    client.post(
        "/auth/register",
        json={"email": "loginuser@example.com", "password": "mypassword"}
    )
    
    # Login via form-urlencoded data (OAuth2PasswordRequestForm requirement)
    response = client.post(
        "/auth/token",
        data={"username": "loginuser@example.com", "password": "mypassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials(client: TestClient):
    """Test login failure with wrong password."""
    client.post(
        "/auth/register",
        json={"email": "wrongpass@example.com", "password": "correctpassword"}
    )
    
    response = client.post(
        "/auth/token",
        data={"username": "wrongpass@example.com", "password": "badpassword"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect email or password"