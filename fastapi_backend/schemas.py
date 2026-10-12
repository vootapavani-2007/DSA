from pydantic import BaseModel, EmailStr, Field, ConfigDict


class RegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)
    role: str = Field(
        default="viewer",
        pattern="^(admin|analyst|viewer)$"
    )


class UserResponse(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    username: str
    password: str