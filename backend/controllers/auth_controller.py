from flask import jsonify, request
from models.user_model import User, UserCreate, UserLogin
from utils.security import hash_password, verify_password, create_access_token, decode_access_token

# In-memory user storage
users = []

def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if any(user.email == email for user in users):
        return jsonify({"error": "User with this email already exists"}), 409

    hashed_pw = hash_password(password)
    user = User(username=username, email=email, password=hashed_pw)
    users.append(user)

    return jsonify({"message": "User created successfully"}), 201


def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = next((u for u in users if u.email == email), None)
    if not user or not verify_password(password, user.password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token({"sub": user.email})
    return jsonify({
        "access_token": access_token,
        "token_type": "bearer"
    }), 200


def get_current_user():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid token"}), 401

    token = auth_header.split(" ")[1]
    payload = decode_access_token(token)
    if not payload:
        return jsonify({"error": "Invalid or expired token"}), 401

    user_email = payload.get("sub")
    user = next((u for u in users if u.email == user_email), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "username": user.username,
        "email": user.email
    }), 200


def update_user():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid token"}), 401

    token = auth_header.split(" ")[1]
    payload = decode_access_token(token)
    if not payload:
        return jsonify({"error": "Invalid or expired token"}), 401

    user_email = payload.get("sub")
    user = next((u for u in users if u.email == user_email), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    new_username = data.get("username")
    new_password = data.get("password")

    if new_username:
        user.username = new_username
    if new_password:
        user.password = hash_password(new_password)

    return jsonify({
        "message": "User updated successfully",
        "username": user.username,
        "email": user.email
    }), 200


def delete_user():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid token"}), 401

    token = auth_header.split(" ")[1]
    payload = decode_access_token(token)
    if not payload:
        return jsonify({"error": "Invalid or expired token"}), 401

    user_email = payload.get("sub")
    user = next((u for u in users if u.email == user_email), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    users.remove(user)

    return jsonify({"message": "User deleted successfully"}), 200