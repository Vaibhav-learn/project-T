from flask import Blueprint, request, jsonify  # type: ignore
from models.cart_model import Cart  # type: ignore
from database import db

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    existing_item = Cart.query.filter_by(user_id=data['user_id'], product_id=data['product_id']).first()
    if existing_item:
        existing_item.quantity += data.get('quantity', 1)
    else:
        new_item = Cart(user_id=data['user_id'], product_id=data['product_id'], quantity=data.get('quantity', 1))
        db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Cart updated'}), 200

@cart_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    items = Cart.query.filter_by(user_id=user_id).all()
    return jsonify([{'product_id': i.product_id, 'quantity': i.quantity} for i in items])

@cart_bp.route('/cart/<int:user_id>/<int:product_id>', methods=['PUT'])
def update_cart(user_id, product_id):
    item = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
    if item:
        item.quantity = request.json.get('quantity', item.quantity)
        db.session.commit()
        return jsonify({'message': 'Cart updated'})
    return jsonify({'error': 'Item not found'}), 404

@cart_bp.route('/cart/<int:user_id>/<int:product_id>', methods=['DELETE'])
def remove_from_cart(user_id, product_id):
    item = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item removed from cart'})
    return jsonify({'error': 'Item not found'}), 404