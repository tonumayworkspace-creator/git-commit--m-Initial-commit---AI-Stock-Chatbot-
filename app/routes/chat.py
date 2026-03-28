# app/routes/chat.py

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.intent_service import detect_intent
from app.services.entity_service import extract_entities
from app.services.stock_service import get_stock_info

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    message: str


@router.post("/")
def chat(request: ChatRequest, db: Session = Depends(get_db)):

    message = request.message

    intent = detect_intent(message)
    entities = extract_entities(message, db)

    products = entities.get("products", [])
    quantity = entities.get("quantity")

    if not products:
        return {
            "intent": intent,
            "error": "Product not identified in message"
        }

    results = []

    for product in products:
        result = get_stock_info(db, product, quantity)
        results.append(result)

    return {
        "intent": intent,
        "products": products,
        "data": results
    }