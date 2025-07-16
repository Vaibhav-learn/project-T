from pydantic import BaseModel, EmailStr

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

# For registering a user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# For login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# For returning user profile
class UserPublic(BaseModel):
    username: str
    email: EmailStr
