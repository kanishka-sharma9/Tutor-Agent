import streamlit as st
import os
import json
import uuid
import time
import requests

st.set_page_config(
    page_title="Tutor Agent",
    page_icon="🪧",
    layout="centered"
)

BASE_URL="http://127.0.0.1:8000/"
APP_NAME="tutor"


st.session_state['user_id']="user-1"
st.session_state['session_id'] = f"session-1"
st.session_state.messages=[]


def create_session():
    response = requests.post(
        f"{BASE_URL}/apps/{APP_NAME}/users/{st.session_state['user_id']}/sessions/{st.session_state['session_id']}",
        headers={"Content-Type": "application/json"},
        data=json.dumps({})
    )
    st.session_state.messages = []
    return True
    
def send_message(message):
    if not st.session_state['session_id']:
        st.error("No active session. Please create a session first.")
        return False
    
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": message})
    
    # Send message to API
    response = requests.post(
        f"{BASE_URL}/run",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "app_name": APP_NAME,
            "user_id": st.session_state['user_id'],
            "session_id": st.session_state['session_id'],
            "new_message": {
                "role": "user",
                "parts": [{"text": message}]
            }
        })
    )
    
    if response.status_code != 200:
        st.error(f"Error: {response.text} {response.json()}")
        return False
    st.session_state.messages.append({"role": "Assistant", "response": response.json()})
    # st.write(st.session_state.messages)
    return True


st.title("🧑‍🏫 Tutor Agent")

# Sidebar for session management
with st.sidebar:
    st.header("Session Management")
    
    if 'session_id' in st.session_state:
        st.success(f"Active session: {st.session_state['session_id']}")
        if st.button("➕ New Session"):
            create_session()
    else:
        st.warning("No active session")
        if st.button("➕ Create Session"):
            create_session()
    
    st.divider()
    st.caption("This app interacts with the Speaker Agent via the ADK API Server.")
    st.caption("Make sure the ADK API Server is running on port 8000.")

# Chat interface
st.subheader("Conversation")

# Display messages
# for msg in st.session_state.messages:
#     if msg["role"] == "user":
#         st.chat_message("user").write(msg["content"])
#     else:
#         with st.chat_message("assistant"):
#             st.write(msg["content"])

# Input for new messages
if st.session_state.session_id:  # Only show input if session exists
    user_input = st.chat_input("Type your message...")
    if user_input:
        send_message(user_input)
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.chat_message("user").write(msg["content"])
            else:
                with st.chat_message("assistant"):
                    st.write(msg['response'][0])
else:
    st.info("👈 Create a session to start chatting")