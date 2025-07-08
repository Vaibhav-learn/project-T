from models.product_model import Product
from database import db

def add_product(data):
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        category=data.get('category', ''),
        image_url=data.get('image_url', '')
    )
    db.session.add(new_product)
    db.session.commit()
    return new_product

def get_products(category=None):
    if category:
        return Product.query.filter_by(category=category).all()
    return Product.query.all()

def update_product(product_id, data):
    product = Product.query.get(product_id)
    if not product:
        return None
    for key in data:
        if hasattr(product, key):
            setattr(product, key, data[key])
    db.session.commit()
    return product

def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return False
    db.session.delete(product)
    db.session.commit()
    return True
