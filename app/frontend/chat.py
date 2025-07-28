import streamlit as st
import requests
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Chat AI", page_icon="💬")

st.title("💬 Chat AI")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.write(prompt)
    
    try:
        response = requests.post(
            "http://localhost:8000/chat/send",
            json={"message": prompt},
            timeout=10
        )
        
        if response.status_code == 200:
            ai_response = response.json().get("response", "Desculpe, não consegui processar sua mensagem.")
        else:
            ai_response = "Erro na API. Tente novamente."
            
    except:
        ai_response = "Olá! Como posso ajudar você hoje?"
    
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    
    with st.chat_message("assistant"):
        st.write(ai_response)
