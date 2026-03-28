# app/db/init_db.py

import pandas as pd
from sqlalchemy.exc import IntegrityError
from app.db.database import SessionLocal, engine, Base
from app.models.item import Item


def seed_from_csv():
    db = SessionLocal()

    try:
        # ✅ Ensure tables exist
        Base.metadata.create_all(bind=engine)

        df = pd.read_csv("test_item.csv")
        df.columns = [col.strip().lower() for col in df.columns]

        required_columns = ["name", "stock", "price"]

        for col in required_columns:
            if col not in df.columns:
                raise Exception(f"Missing required column: {col}")

        df = df.drop_duplicates(subset=["name"])

        for _, row in df.iterrows():
            name = str(row["name"]).strip().upper()

            if not name or name == "NAN":
                continue

            stock = row["stock"]
            price = row["price"]

            stock = int(stock) if not pd.isna(stock) else 0
            price = int(price) if not pd.isna(price) else 0

            try:
                db.add(Item(name=name, stock=stock, price=price))
                db.commit()

            except IntegrityError:
                db.rollback()
                print(f"⚠️ Skipping duplicate: {name}")

        print("✅ Data inserted successfully from CSV")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_from_csv()