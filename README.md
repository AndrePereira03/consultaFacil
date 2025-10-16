# 🏥 **Sistema de Gerenciamento de Pacientes e Consultas**

## **Descrição**:

Este projeto é uma API REST desenvolvida com Flask para gerenciar pacientes, profissionais de saúde e consultas médicas. Ele permite operações CRUD (Create, Read, Update, Delete) para cada entidade e usa Flask-SQLAlchemy para persistência de dados com SQLite.

## **Demonstração do Projeto (clique abaixo para acessar o vídeo)**

[![Demonstração do Projeto Consulta Fácil](https://github.com/AndrePereira03/consultaFacil/blob/AndrePereira03-patch-1/assets/testando-bd.gif?raw=true)](https://www.youtube.com/watch?v=QgzlOASWok8)

## **Principais funcionalidades:**

- Cadastro, listagem, atualização e remoção de pacientes, profissionais e consultas.
- Agendamento, atualização de status e cancelamento de consultas médicas.
- API RESTful com suporte a CORS.

## **Como Rodar o Projeto**

### **1️⃣ Clonar o repositório em uma pasta desejada**

git clone https://github.com/AndrePereira03/consultaFacil.git  
cd consultaFacil

### **2️⃣ Instalar as dependências**

pip install -r requirements.txt

### **3️⃣ Rodar a API**

python main.py

Se tudo estiver certo, a saída será algo como:

- Running on http://127.0.0.1:5000/

### **4️⃣ Rodar os testes automatizados:**

pytest -v testes.py

## **Tecnologias Utilizadas**

- Python 3.8+
- Flask 3.1.0
- Flask-SQLAlchemy
- Flask-CORS
- SQLite
- Pytest para testes automatizados

## **Melhorias Futuras**

- Implementar um handler de exceções para o banco de dados que capture os erros, grave o log completo e retorne ao usuário uma mensagem amigável com um código de referência.

- Implementar API de sincronização com agendas, permitindo que os usuários conectem suas contas e visualizem os eventos do Consulta Facil externamente.
