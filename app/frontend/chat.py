import streamlit as st
import requests

st.set_page_config(page_title="Chat AI", page_icon="💬")

st.title("💬 Chat AI")

if 'messages' not in st.session_state:
    st.session_state.messages = []

user_id = st.number_input("ID do Usuário", min_value=1, step=1, value=st.session_state.get('user_id', 99))
st.session_state.user_id = user_id

for message in st.session_state.messages:
    role = "assistant" if message["type_message"].lower() == "ai" else "user"
    with st.chat_message(role):
        st.write(message["content"])
if prompt := st.chat_input("Digite sua mensagem..."):
    try:
        response = requests.post(
            "http://localhost:8000/chat/ongoing",
            json={
                "input_user": prompt,
                "user_id": int(st.session_state.user_id)
            },
            timeout=30
        )
        if response.status_code == 201:
            data = response.json()
            st.session_state.messages.append({
                "type_message": "user",
                "content": prompt
            })
            if "messages" in data and data["messages"]:
                last_message = data["messages"]
            
                for message in st.session_state.messages:
                    role = "assistant" if message["type_message"].lower() == "ai" else "user"
                    with st.chat_message(role):
                            st.write(message["content"])
        else:
            st.error("Erro na API. Tente novamente.")
    except Exception as e:
        st.error(f"Erro de conexão: {str(e)}")

if st.button("Finalizar Conversa"):
    st.session_state.messages = []
    st.success("Conversa finalizada com sucesso!")
    st.rerun()
