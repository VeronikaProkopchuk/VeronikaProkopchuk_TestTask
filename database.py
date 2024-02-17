from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#database url
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

#database engine
engine = create_engine(
SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#creating session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Using Base as a base class for all database models
class Base(DeclarativeBase):
    pass

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
