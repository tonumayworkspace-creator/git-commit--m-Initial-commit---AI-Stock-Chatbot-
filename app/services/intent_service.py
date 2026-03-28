# app/services/intent_service.py

def detect_intent(message: str) -> str:
    msg = message.lower()

    has_stock = any(word in msg for word in ["stock", "available", "hai", "confirm"])
    has_price = any(word in msg for word in ["price", "rate", "kitna"])

    if has_stock and has_price:
        return "check_stock_and_price"
    elif has_stock:
        return "check_stock"
    elif has_price:
        return "check_price"

    if any(word in msg for word in ["urgent", "bhej", "dispatch", "block"]):
        return "action_request"

    return "unknown"