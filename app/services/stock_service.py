# app/services/stock_service.py

from sqlalchemy.orm import Session
from app.models.item import Item


def get_stock_info(db: Session, product_name: str, quantity_requested: int = None):

    item = db.query(Item).filter(Item.name == product_name).first()

    if not item:
        return {"error": "Product not found"}

    response = {
        "product": item.name,
        "available_stock": item.stock,
        "price": item.price
    }

    if quantity_requested is not None:

        if quantity_requested <= 0:
            response["status"] = "invalid quantity"
            return response

        if quantity_requested <= item.stock:
            response["status"] = "available"
            response["remaining_stock"] = item.stock - quantity_requested
        else:
            response["status"] = "insufficient stock"
            response["shortage"] = quantity_requested - item.stock

    else:
        response["status"] = "in stock" if item.stock > 0 else "out of stock"

    if item.stock < 50 and item.stock > 0:
        response["warning"] = "low stock"

    return response