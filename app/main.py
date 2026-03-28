# app/main.py

from fastapi import FastAPI
from app.routes import chat
from app.db.database import engine, Base
from app.models import item

app = FastAPI(
    title="AI Stock Chatbot API",
    description="Backend system for stock queries using NLP",
    version="1.0.0"
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(chat.router)


@app.get("/")
def root():
    return {"message": "AI Stock Chatbot API is running 🚀"}