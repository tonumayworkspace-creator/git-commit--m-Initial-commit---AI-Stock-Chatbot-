# app/test_db.py

from app.db.database import SessionLocal
from app.models.item import Item

db = SessionLocal()

items = db.query(Item).all()

print(f"\nTotal items in DB: {len(items)}\n")

for item in items[:10]:
    print(item.id, item.name, item.stock, item.price)

db.close()