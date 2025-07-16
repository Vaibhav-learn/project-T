from flask import Blueprint, request, jsonify
from controllers.order_controller import (
    place_order, get_order, get_all_orders, update_order_status
)

order_bp = Blueprint("orders", __name__)

@order_bp.route("/", methods=["POST"])
def create_order():
    data = request.json
    order = place_order(data)
    return jsonify({
        "message": "Order placed",
        "order_id": order.id
    }), 201

@order_bp.route("/", methods=["GET"])
def list_orders():
    orders = get_all_orders()
    return jsonify([{
        "id": o.id,
        "item": o.item_name,
        "quantity": o.quantity,
        "status": o.status,
        "created_at": o.created_at
    } for o in orders])

@order_bp.route("/<int:order_id>", methods=["GET"])
def get_single_order(order_id):
    order = get_order(order_id)
    if order:
        return jsonify({
            "id": order.id,
            "item": order.item_name,
            "quantity": order.quantity,
            "status": order.status,
            "created_at": order.created_at
        })
    return jsonify({"error": "Order not found"}), 404

@order_bp.route("/<int:order_id>", methods=["PATCH"])
def update_status(order_id):
    data = request.json
    new_status = data.get("status")
    order = update_order_status(order_id, new_status)
    if order:
        return jsonify({"message": "Status updated"})
    return jsonify({"error": "Order not found"}), 404