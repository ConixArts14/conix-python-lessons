from fastapi.testclient import TestClient
from Day_164_Python_Developer_Mastery import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint returns a successful welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Day 164 Complete CRUD & Pagination API!"}

def test_register_and_login_user():
    """Test user registration and subsequent token generation via login."""
    # Unique test email to prevent collision on re-runs
    user_data = {
        "username": "runner_tester",
        "email": "tester@runner.com",
        "password": "securepassword123"
    }

    # 1. Register User
    response = client.post("/register/", json=user_data)
    # If already registered from a previous test run, we accept 400, otherwise 200
    assert response.status_code in [200, 400]

    # 2. Login User to get access token
    login_data = {
        "email": "tester@runner.com",
        "password": "securepassword123"
    }
    response = client.post("/login/", json=login_data)
    
    if response.status_code == 200:
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

from fastapi.testclient import TestClient
from Day_164_Python_Developer_Mastery import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint returns a successful welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Day 164 Complete CRUD & Pagination API!"}

def test_register_and_login_user():
    """Test user registration and subsequent token generation via login."""
    user_data = {
        "username": "runner_tester",
        "email": "tester@runner.com",
        "password": "securepassword123"
    }

    # 1. Register User (ignore 400 if already registered)
    client.post("/register/", json=user_data)

    # 2. Login User to get access token
    login_data = {
        "email": "tester@runner.com",
        "password": "securepassword123"
    }
    response = client.post("/login/", json=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_protected_user_profile():
    """Test accessing the protected /users/me/ endpoint with a valid JWT token."""
    login_data = {
        "email": "tester@runner.com",
        "password": "securepassword123"
    }
    # Login to retrieve token
    login_res = client.post("/login/", json=login_data)
    token = login_res.json()["access_token"]

    # Set headers with the Bearer token
    headers = {"Authorization": f"Bearer {token}"}

    # Access protected route
    response = client.get("/users/me/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "tester@runner.com"
    assert "items" in data

def test_create_and_read_item():
    """Test creating an item and reading it back with pagination parameters."""
    login_data = {
        "email": "tester@runner.com",
        "password": "securepassword123"
    }
    login_res = client.post("/login/", json=login_data)
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 1. Create an item
    item_payload = {
        "title": "Morning LSD Run",
        "description": "Completed 15km slow distance training."
    }
    create_res = client.post("/items/", json=item_payload, headers=headers)
    assert create_res.status_code == 200
    item_data = create_res.json()
    assert item_data["title"] == "Morning LSD Run"

    # 2. Read items with pagination (skip=0, limit=5)
    get_res = client.get("/items/?skip=0&limit=5", headers=headers)
    assert get_res.status_code == 200
    items_list = get_res.json()
    assert isinstance(items_list, list)
    assert len(items_list) > 0