import streamlit as st
import requests

st.set_page_config(page_title="Chat AI", page_icon="💬")
st.title("💬 Chat AI")

if 'messages' not in st.session_state:
    st.session_state.messages = []

user_id = st.number_input("ID do Usuário", min_value=1, value=99)

prompt = st.chat_input("Digite sua mensagem...")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})


    with st.chat_message("user"):
        st.write(prompt)
    
 
    try:
        response = requests.post(
            "http://localhost:8000/chat-ai/ongoing",
            json={"input_user": prompt, "user_id": user_id}
        )
        
        if response.status_code == 201:
            data = response.json()
            
        
            if data.get("answer_ai"):
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": data["answer_ai"]
                })
        
                with st.chat_message("assistant"):
                    st.write(data["answer_ai"])
        else:
            st.error("Erro na API")
            
    except Exception as e:
        st.error(f"Erro: {str(e)}")

if st.button("Limpar Conversa"):
    st.session_state.messages = []
    st.rerun()
