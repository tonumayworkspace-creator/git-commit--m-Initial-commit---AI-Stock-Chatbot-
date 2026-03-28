# 🤖 AI Stock Chatbot — Production-Ready NLP Inventory Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Architecture](https://img.shields.io/badge/Architecture-Modular-blueviolet)
![Status](https://img.shields.io/badge/Status-Production--Ready-success)

---

## 🚀 Overview

AI Stock Chatbot is a **production-ready backend system** that processes real-world inventory queries using a hybrid NLP pipeline.

Unlike traditional chatbots, this system handles **noisy, incomplete, and multi-entity queries**, making it suitable for real business workflows.

---

## 🎯 Problem Solved

Businesses often receive unstructured queries like:

- `2001 50 pcs`
- `vivo stock available?`
- `2005 realme aur 2002 vivo dono check karo`

These are difficult to process using standard systems.

👉 This project converts such inputs into **structured, actionable responses**.

---

## 🧠 Core Capabilities

### ✅ Intelligent NLP Pipeline
- Rule-based intent detection
- Entity extraction using:
  - Numeric mapping (2001 → product)
  - Keyword matching (brand names)
- Handles noisy & real-world queries

---

### 🔥 Multi-Product Query Handling
- Extracts multiple products from a single query
- Returns aggregated results

---

### 📦 Inventory Intelligence
- Stock validation
- Shortage calculation
- Remaining stock computation
- Low stock alerts

---

### 🗄️ Data Layer
- SQL-based inventory system (SQLite)
- ORM using SQLAlchemy
- Clean schema design

---

### 🔄 Data Ingestion Pipeline
- CSV / Excel → Database
- Handles:
  - Missing values
  - Duplicates
  - Data normalization

---

### 💬 Chat Interface
- Streamlit-based ChatGPT-style UI
- Card-based responses
- Color-coded stock status

---

### 📊 Batch Processing
- Reads queries from Excel
- Sends to API
- Evaluates responses

---

## 🏗️ System Architecture

```
User Query
   ↓
FastAPI Backend
   ↓
NLP Layer (Intent + Entity Extraction)
   ↓
Database (SQLite via SQLAlchemy)
   ↓
Business Logic (Stock Service)
   ↓
Response (JSON)
   ↓
Streamlit UI
```

---

## 📂 Project Structure

```
ai-stock-chatbot/
│
├── app/
│   ├── main.py
│   ├── routes/chat.py
│   ├── services/
│   │   ├── intent_service.py
│   │   ├── entity_service.py
│   │   └── stock_service.py
│   ├── db/
│   ├── models/
│   ├── ui.py
│   └── run_queries.py
│
├── test_item.csv
├── Test Message.xlsx
├── stock.db
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 2️⃣ Start Backend
```
uvicorn app.main:app --reload
```

### 3️⃣ Launch UI
```
streamlit run app/ui.py
```

### 4️⃣ Run Batch Queries
```
python -m app.run_queries
```

---

## 🧪 Example Queries

- `2001 50 pcs`
- `vivo stock confirm`
- `price of 2003`
- `2005 realme aur 2002 vivo check karo`

---

## 📈 Engineering Highlights

- Designed **hybrid NLP system** without dependency on LLM
- Implemented **scoring-based entity resolution**
- Built **multi-entity extraction pipeline**
- Created **modular, scalable backend architecture**
- Ensured **robust handling of real-world noisy inputs**

---

## 🚀 Future Enhancements

- LLM integration for semantic understanding
- Vector database (RAG)
- Deployment (Render / AWS)
- Role-based access system

---

## 👨‍💻 Author

**Tanumay Bhattacharya**

---

## ⭐ Impact

This project demonstrates:
- Real-world problem solving
- Backend engineering skills
- NLP system design
- Production-level thinking

---

👉 If you found this useful, consider giving it a ⭐
