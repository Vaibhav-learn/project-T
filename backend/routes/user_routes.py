from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
def get_profile():
    return jsonify({"message": "This would return user profile"})
