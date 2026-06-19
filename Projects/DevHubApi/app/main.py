from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .auth import create_access_token, hash_password, verify_password, get_current_user
from .schemas import UserCreate, UserRead, LoginRequest, UserResponse, UserUpdate
from .database import engine, SessionLocal, get_db
from .models import Base, User

app = FastAPI(
    title="Developer Hub API"
)

Base.metadata.create_all(bind=engine)

@app.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        (User.email == user.email) | (User.username == user.username)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username or email already registered"
        )

    hashed = hash_password(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed
    )

    db.add(db_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Unable to register user"
        )
    db.refresh(db_user)
    return db_user

@app.post("/login")
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == login_data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        login_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.get("/users", response_model=List[UserRead])
def get_users(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(User).all()

@app.get("/")
def root():
    return {"message": "Developer Hub API"}

@app.get("/users/{id}")
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    user = db.query(User).filter(
        User.id == id
    ).first()

    return user


@app.post("/users")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@app.put("/users/{id}")
def update_user(
    id: int,
    update: UserUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    user = db.query(User).filter(
        User.id == id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.username = update.name

    db.commit()

    return user

@app.delete("/users/{id}")
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    user = db.query(User).filter(
        User.id == id
    ).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}

