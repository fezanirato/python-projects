# ChatBot com IA utilizando Python, Streamlit e OpenAI
<img src="Chatbot com IA/Ilustação do Chatbot.jpg" alt="Preview do Chatbot" />
## Sobre o Projeto

Este projeto consiste no desenvolvimento de um **ChatBot com Inteligência Artificial**.

A aplicação permite que o usuário envie mensagens e receba respostas automáticas em tempo real, simulando uma conversa com um assistente virtual, de forma semelhante ao ChatGPT.

Todo o sistema foi desenvolvido utilizando **Python** e **Streamlit**, possibilitando a criação de uma interface moderna sem a necessidade de escrever HTML, CSS ou JavaScript. A comunicação com a inteligência artificial é realizada através da **API da OpenAI**.

---

## Funcionalidades

- Interface de chat moderna e intuitiva.
- Mensagem inicial de boas-vindas.
- Envio de perguntas pelo usuário.
- Respostas geradas por Inteligência Artificial.
- Histórico das mensagens durante a conversa.
- Comunicação em tempo real com a API da OpenAI.
- Desenvolvimento totalmente em Python.

---

## Tecnologias Utilizadas

- Python 3
- Streamlit
- OpenAI API

---

## Configurando a API da OpenAI

Para utilizar o chatbot, é necessário possuir uma chave de API da OpenAI.

Você pode obter uma em:

https://platform.openai.com/

Depois, configure sua chave como variável de ambiente.

### Windows

```bash
set OPENAI_API_KEY=sua_chave_aqui
```

### Linux / macOS

```bash
export OPENAI_API_KEY=sua_chave_aqui
```

Ou utilize um arquivo `.env`, caso o projeto esteja configurado para isso.

---

## Como funciona

1. O usuário acessa o site.
2. Uma mensagem de boas-vindas é exibida.
3. O usuário digita sua pergunta.
4. A mensagem é enviada para a API da OpenAI.
5. A IA processa a solicitação.
6. A resposta é exibida logo abaixo da pergunta, mantendo o histórico da conversa.

---

## Bibliotecas Utilizadas

### Streamlit

Framework utilizado para desenvolver a interface web da aplicação utilizando apenas Python.

Instalação:

```bash
pip install streamlit
```

Documentação:

https://docs.streamlit.io/

---

### OpenAI

Biblioteca oficial para integração com os modelos de Inteligência Artificial da OpenAI.

Instalação:

```bash
pip install openai
```

Documentação:

https://platform.openai.com/docs/overview

---

## Objetivos de Aprendizagem

Durante este projeto são explorados os seguintes conceitos:

- Desenvolvimento de aplicações web com Streamlit.
- Criação de interfaces de chat.
- Armazenamento do histórico das mensagens.
- Integração com APIs.
- Consumo da API da OpenAI.
- Estruturação de aplicações Python.
- Desenvolvimento de aplicações com Inteligência Artificial.

---

## Resultado Esperado

Ao final do projeto, teremos um chatbot funcional com:

- Interface limpa e moderna;
- Campo para envio de mensagens;
- Histórico completo da conversa;
- Respostas geradas por Inteligência Artificial em tempo real.

---

## Desenvolvido por

Felipe Zanirato  
[GitHub](https://github.com/fezanirato)  
[felipe.zanirato@outlook.com](mailto:felipe.zanirato@outlook.com)
