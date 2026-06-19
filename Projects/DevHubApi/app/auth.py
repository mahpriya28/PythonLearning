# Hash passwords
from fastapi import Depends
from passlib.context import CryptContext
from jose import jwt
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer

from .database import get_db
from .models import User

SECRET_KEY = "supersecret"

ALGORITHM = "HS256"
security = HTTPBearer()

def create_access_token(data):

    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(
        plain_password,
        hashed_password
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data):
    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def get_current_user(
    credentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    email = payload.get("sub")

    user = db.query(User).filter(
        User.email == email
    ).first()

    return user
    