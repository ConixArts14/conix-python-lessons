from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./runner_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    posts = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")

from database import SessionLocal
from Day_156_Python_Developer_Mastery import User, Post

# Create a database session
db = SessionLocal()

# 1. Create a new user
new_user = User(username="conix_dev", email="conix@runner.com", hashed_password="securepassword123")
db.add(new_user)
db.commit()
db.refresh(new_user)
print(f"Created User: {new_user.username} with ID: {new_user.id}")

# 2. Create a post associated with that user using their ID
new_post = Post(title="My First FastAPI Post", content="Learning foreign keys and relationships with Alembic!", user_id=new_user.id)
db.add(new_post)
db.commit()
db.refresh(new_post)
print(f"Created Post: '{new_post.title}' owned by user_id: {new_post.user_id}")

# 3. Test the relationship lookup!
user_posts = db.query(User).filter(User.username == "conix_dev").first()
print(f"\n--- Checking Relationships ---")
print(f"User: {user_posts.username}")
print(f"Their Posts:")
for post in user_posts.posts:
    print(f"  - [{post.id}] {post.title}: {post.content}")

db.close()