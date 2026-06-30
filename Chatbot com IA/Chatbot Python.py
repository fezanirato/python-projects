# Passo a passo:
# Título
# Input do Chat
# A cada mensagem enviada:
    # Mostrar a mensagem que usuario enviou no chat
    # Enviar para a IA responder
    # Exibir resposta da IA no chat
# Fazer site usando streamlit (Frontend e Backend)

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="Chave secreta API")

st.write("### Chatbot com IA")

# Criar memoria usando session state

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# Exibir o histórico de mensagens

for mensagem in st.session_state["lista_mensagens"]:

    role = mensagem["role"]
    conteudo = mensagem["content"]

    st.chat_message(role).write(conteudo)

# Input do usuário
mensagem_usuario = st.chat_input("Escreva uma mensagem...")

if mensagem_usuario:

    # Salva mensagem do usuário
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)
    
    # Mostra na tela
    st.chat_message("user").write(mensagem_usuario)

    # Resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages = st.session_state["lista_mensagens"],
        model = "gpt-4o"
    )
    print(resposta_modelo)
    resposta_ia = resposta_modelo.choices[0].message.content

    # Mostra resposta
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

    print(st.session_state["lista_mensagens"])