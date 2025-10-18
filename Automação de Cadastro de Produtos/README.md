# 🤖 Automação de Cadastro de Produtos

Este projeto tem como objetivo **automatizar o processo de cadastro de produtos em um sistema web**, lendo informações de um arquivo CSV e simulando o comportamento humano ao preencher formulários online.

---

## 🧩 Contexto do Projeto

Imagine que você tenha uma base de produtos contendo centenas de registros — como **códigos, marcas, tipos, categorias, preços e observações** — e precise cadastrar tudo isso manualmente em um sistema.  
Esse processo seria **lento, cansativo e sujeito a erros humanos**.

Neste projeto, utilizei **Python** para automatizar completamente essa tarefa.  
O programa acessa o sistema, faz login e cadastra todos os produtos de forma automática, como se você mesmo estivesse usando o computador.

---

## ⚙️ Funcionalidades

Ao executar o script, o programa:

1. Abre o navegador automaticamente  
2. Acessa o site do sistema  
3. Faz login com usuário e senha  
4. Lê a base de dados (`produtos.csv`)  
5. Insere cada informação nos campos correspondentes  
6. Envia o cadastro  
7. Repete o processo até todos os produtos serem cadastrados

---

## 🧠 Tecnologias Utilizadas

- **Python 3**
- **PyAutoGUI** – para automação de mouse e teclado  
- **Pandas** – para leitura e manipulação da base de dados  
- **Time** – para controle de pausas e sincronização  

---

## 🎯 Resultado Esperado

Ao final da execução, todos os produtos da base estarão cadastrados automaticamente no sistema, sem nenhuma intervenção manual.

---

## 👨‍💻 Desenvolvido por

Felipe Zanirato
🔗 GitHub
📧 felipe.zanirato@outlook.com
