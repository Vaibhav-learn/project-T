from models.user_model import User, UserLogin
from utils.security import hash_password, verify_password

# Fake database
fake_users_db = {}

def signup(user: User):
    if user.email in fake_users_db:
        return {"error": "User already exists"}
    user.password = hash_password(user.password)
    fake_users_db[user.email] = user.dict()
    return {"message": "User created successfully"}

def login(user: UserLogin):
    db_user = fake_users_db.get(user.email)
    if not db_user:
        return {"error": "Invalid credentials"}
    if not verify_password(user.password, db_user["password"]):
        return {"error": "Invalid credentials"}
    return {"message": "Login successful"}
