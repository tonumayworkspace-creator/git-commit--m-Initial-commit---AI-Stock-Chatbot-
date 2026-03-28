# app/run_queries.py

import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/chat/"


def run_queries():
    df = pd.read_excel("Test Message (1).xlsx")
    df.columns = [col.strip().lower() for col in df.columns]

    for i, row in df.iterrows():
        message = str(row["message"])

        print(f"\n🔹 Query {i+1}: {message}")

        response = requests.post(API_URL, json={"message": message})
        print(response.json())


if __name__ == "__main__":
    run_queries()