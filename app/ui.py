# app/ui.py

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat/"

st.set_page_config(page_title="AI Stock Chatbot", layout="centered")

# CSS
st.markdown("""
<style>
.card {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
}
.status-green { color: #22c55e; font-weight: bold; }
.status-red { color: #ef4444; font-weight: bold; }
.status-yellow { color: #facc15; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Stock Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

user_input = st.chat_input("Ask about stock...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = requests.post(API_URL, json={"message": user_input})
        data = response.json()

        # MULTI PRODUCT RESPONSE
        if isinstance(data.get("data"), list):

            bot_reply = ""

            for result in data["data"]:

                status = result.get("status", "N/A")

                if "available" in status or "in stock" in status:
                    status_class = "status-green"
                elif "insufficient" in status:
                    status_class = "status-red"
                else:
                    status_class = "status-yellow"

                bot_reply += f"""
<div class="card">
<b>📦 Product:</b> {result.get("product")}<br>
<b>📊 Stock:</b> {result.get("available_stock")}<br>
<b>💰 Price:</b> ₹{result.get("price")}<br>
<b>Status:</b> <span class="{status_class}">{status}</span><br>
</div><br>
"""

        elif "error" in data:
            bot_reply = f"<span class='status-red'>❌ {data['error']}</span>"
        else:
            bot_reply = "No response"

    except Exception:
        bot_reply = "<span class='status-red'>❌ Backend connection error</span>"

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply, unsafe_allow_html=True)