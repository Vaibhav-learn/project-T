from fastapi import APIRouter
from models.user_model import User, UserLogin
from controllers.auth_controller import signup, login

router = APIRouter()

@router.post("/signup")
def user_signup(user: User):
    return signup(user)

@router.post("/login")
def user_login(user: UserLogin):
    return login(user)
