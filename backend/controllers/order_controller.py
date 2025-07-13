from models.order_model import db, Order

def place_order(data):
    order = Order(item_name=data['item_name'], quantity=data['quantity'])
    db.session.add(order)
    db.session.commit()
    return order

def get_order(order_id):
    return Order.query.get(order_id)

def get_all_orders():
    return Order.query.all()

def update_order_status(order_id, new_status):
    order = Order.query.get(order_id)
    if order:
        order.status = new_status
        db.session.commit()
    return order
