from pydantic import BaseModel, validator

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    @validator("email")
    def simple_email_check(cls, v):
        if "@" not in v or v.strip() == "":
            raise ValueError("invalid email")
        return v
    
class LoginRequest(BaseModel):
    email: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    name: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True