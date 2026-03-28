# app/services/entity_service.py

import re
from sqlalchemy.orm import Session
from app.models.item import Item


def clean_text(text: str):
    return re.sub(r'[^a-zA-Z0-9 ]', '', text).lower()


def extract_quantity(message: str):
    numbers = re.findall(r'\d+', message)
    if numbers:
        return int(numbers[0])
    return None


def extract_products(message: str, db: Session):
    """
    Multi-product extraction:
    - Matches numeric codes (2001, 2005, etc.)
    - Returns multiple matched products
    """

    cleaned_message = clean_text(message)
    numbers = re.findall(r'\d+', cleaned_message)

    items = db.query(Item).all()

    matched_products = []

    for item in items:
        item_name_clean = clean_text(item.name)

        for num in numbers:
            if num in item_name_clean:
                matched_products.append(item.name)
                break

    return list(set(matched_products))


def extract_entities(message: str, db: Session):
    return {
        "products": extract_products(message, db),
        "quantity": extract_quantity(message)
    }