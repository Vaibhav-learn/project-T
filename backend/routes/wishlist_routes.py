from flask import Blueprint, request, jsonify # type: ignore
from models.wishlist_model import Wishlist # type: ignore
from database import db

wishlist_bp = Blueprint('wishlist', __name__)

@wishlist_bp.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    data = request.json
    exists = Wishlist.query.filter_by(user_id=data['user_id'], product_id=data['product_id']).first()
    if exists:
        return jsonify({'message': 'Item already in wishlist'}), 200
    item = Wishlist(user_id=data['user_id'], product_id=data['product_id'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item added to wishlist'}), 201

@wishlist_bp.route('/wishlist/<int:user_id>', methods=['GET'])
def get_wishlist(user_id):
    items = Wishlist.query.filter_by(user_id=user_id).all()
    return jsonify([{'product_id': i.product_id} for i in items])

@wishlist_bp.route('/wishlist/<int:user_id>/<int:product_id>', methods=['DELETE'])
def remove_from_wishlist(user_id, product_id):
    item = Wishlist.query.filter_by(user_id=user_id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item removed from wishlist'})
    return jsonify({'error': 'Item not found'}), 404
