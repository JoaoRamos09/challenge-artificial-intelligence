import streamlit as st
import requests
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Chat AI", page_icon="💬")

st.title("💬 Chat AI")

if 'conversation_id' not in st.session_state:
    st.session_state.conversation_id = None

# Campo para inserir o ID do usuário
user_id = st.number_input("ID do Usuário", min_value=1, step=1, value=st.session_state.get('user_id', 99))
st.session_state.user_id = user_id

# NÃO EXIBE MENSAGENS ANTIGAS, pois não guardamos mais nada

if prompt := st.chat_input("Digite sua mensagem..."):
    try:
        if st.session_state.conversation_id is None:
            # Primeira mensagem: inicia a conversa
            response = requests.post(
                "http://localhost:8000/chat/start",
                json={
                    "input_user": prompt,
                    "user_id": int(st.session_state.user_id)
                },
                timeout=30
            )
            if response.status_code == 201:
                data = response.json()
                st.session_state.conversation_id = data["conversation_id"]
                # Exibe as mensagens do histórico retornado, sem guardar nada
                for message in data["messages"]:
                    role = "assistant" if message["type_message"] == "ai" else "user"
                    with st.chat_message(role):
                        if message["type_message"] == "ai":
                            st.write( message["content"])
                        else:
                            st.write(message["content"])
            else:
                st.error("Erro ao iniciar conversa. Tente novamente.")
        else:
            # Conversa já iniciada: envia para o endpoint ongoing
            response = requests.post(
                "http://localhost:8000/chat/ongoing",
                json={
                    "input_user": prompt,
                    "conversation_id": st.session_state.conversation_id
                },
                timeout=30
            )
            if response.status_code == 201:
                data = response.json()
                # Exclui totalmente as mensagens antigas (não guardamos nada)
                # Exibe as mensagens do histórico atualizado, sem guardar nada
                for message in data["messages"]:
                    role = "assistant" if message["type_message"] == "AI" else "user"
                    with st.chat_message(role):
                        if message["type_message"] == "AI":
                            st.write("🤖 " + message["content"])
                        else:
                            st.write(message["content"])
            else:
                st.error("Erro na API. Tente novamente.")
    except Exception as e:
        st.error(f"Erro de conexão: {str(e)}")

if st.button("Finalizar Conversa") and st.session_state.conversation_id:
    try:
        response = requests.post(
            "http://localhost:8000/chat/finished",
            params={"conversation_id": st.session_state.conversation_id},
            timeout=10
        )
        if response.status_code == 204:
            st.success("Conversa finalizada com sucesso!")
            st.session_state.messages = []
            st.session_state.conversation_id = None
            st.rerun()
        else:
            st.error("Erro ao finalizar conversa.")
    except Exception as e:
        st.error(f"Erro ao finalizar conversa: {str(e)}")
