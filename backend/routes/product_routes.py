from flask import Blueprint, request, jsonify
from controllers.product_controller import add_product, get_products, update_product, delete_product

product_bp = Blueprint('products', __name__, url_prefix='/')

# ✅ Add a new product
@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Missing required fields: name and price"}), 400
    
    product = add_product(data)
    return jsonify({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "category": product.category,
        "image_url": product.image_url
    }), 201

# ✅ Get all products or filter by category
@product_bp.route('/products', methods=['GET'])
def list_products():
    category = request.args.get('category')
    products = get_products(category)
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": p.price,
        "category": p.category,
        "image_url": p.image_url
    } for p in products])

# ✅ Update a product by ID
@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.json
    updated = update_product(product_id, data)
    if updated:
        return jsonify({
            "id": updated.id,
            "name": updated.name,
            "description": updated.description,
            "price": updated.price,
            "category": updated.category,
            "image_url": updated.image_url
        })
    return jsonify({"error": "Product not found"}), 404

# ✅ Delete a product by ID
@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    success = delete_product(product_id)
    if success:
        return jsonify({"message": "Product deleted successfully"})
    return jsonify({"error": "Product not found"}), 404
