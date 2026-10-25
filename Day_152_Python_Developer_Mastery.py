# Day 152 - Activity 1: Password Hashing & JWT Token Generation
from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext

# 1. Password Hashing Configuration (Using bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Secret key & algorithm to sign JWT tokens
SECRET_KEY = "super_secret_runner_key_152"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
    """Takes a plain-text password and returns a secure bcrypt hash."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain-text password against the stored hash."""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Generates a signed JWT access token valid for a set duration."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --- Quick Test Execution ---
if __name__ == "__main__":
    raw_pass = "RunnerSpeed123!"
    hashed = hash_password(raw_pass)
    print(f"🔒 [HASHED PASSWORD]: {hashed}")
    print(f"✅ [VERIFICATION CHECK]: {verify_password(raw_pass, hashed)}")
    
    # Generate token
    token = create_access_token({"sub": "conix@mastery.com"})
    print(f"🎫 [JWT ACCESS TOKEN]: {token}")

# Day 152 - Activity 1: Password Hashing & JWT Token Generation (Direct Bcrypt)
from datetime import datetime, timedelta, timezone
import bcrypt
import jwt

# Secret key & algorithm to sign JWT tokens
SECRET_KEY = "super_secret_runner_key_152"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
    """Takes a plain-text password and returns a secure bcrypt hash."""
    # Convert string password to bytes, generate salt, and hash
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain-text password against the stored hash."""
    plain_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_bytes, hashed_bytes)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Generates a signed JWT access token valid for a set duration."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --- Quick Test Execution ---
if __name__ == "__main__":
    raw_pass = "RunnerSpeed123!"
    hashed = hash_password(raw_pass)
    print(f"🔒 [HASHED PASSWORD]: {hashed}")
    print(f"✅ [VERIFICATION CHECK]: {verify_password(raw_pass, hashed)}")
    
    # Generate token
    token = create_access_token({"sub": "conix@mastery.com"})
    print(f"🎫 [JWT ACCESS TOKEN]: {token}")

# Day 152 - Activity 3: Automated Testing for JWT Authentication
from fastapi.testclient import TestClient
from main_auth import app

client = TestClient(app)

def test_read_dashboard_unauthorized():
    """Ensure accessing the dashboard without a token fails with 401."""
    response = client.get("/runner/dashboard")
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"

def test_login_success():
    """Ensure valid runner credentials successfully return a JWT access token."""
    response = client.post(
        "/token",
        data={"username": "conix@mastery.com", "password": "RunnerSpeed123!"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_read_dashboard_authorized():
    """Ensure a runner can access the secure dashboard using a valid generated token."""
    # Step 1: Login to get the access token
    login_res = client.post(
        "/token",
        data={"username": "conix@mastery.com", "password": "RunnerSpeed123!"}
    )
    token = login_res.json()["access_token"]

    # Step 2: Access the protected route with the Bearer token in the headers
    response = client.get(
        "/runner/dashboard",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["runner"] == "conix@mastery.com"
    assert "Authenticated" in data["status"]