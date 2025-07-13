from flask import Blueprint
from controllers import auth_controller

auth_bp = Blueprint("auth", __name__)

auth_bp.route("/signup", methods=["POST"])(auth_controller.signup)
auth_bp.route("/login", methods=["POST"])(auth_controller.login)
auth_bp.route("/me", methods=["GET"])(auth_controller.get_current_user)
auth_bp.route("/update", methods=["PUT"])(auth_controller.update_user)
auth_bp.route("/delete", methods=["DELETE"])(auth_controller.delete_user)