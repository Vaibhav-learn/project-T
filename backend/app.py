from flask import Flask
from flask_cors import CORS
from database import db
from routes.cart_routes import cart_bp
from routes.wishlist_routes import wishlist_bp
from routes.product_routes import product_bp

app = Flask(__name__)
CORS(app)

app.config.from_pyfile('config.py')

db.init_app(app)

app.register_blueprint(cart_bp)
app.register_blueprint(wishlist_bp)
app.register_blueprint(product_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)