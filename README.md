# 🏥 **Sistema de Gerenciamento de Pacientes e Consultas**
## 📌 **Descrição**:

Este projeto é uma API REST desenvolvida com Flask para gerenciar pacientes, profissionais de saúde e consultas médicas. Ele permite operações CRUD (Create, Read, Update, Delete) para cada entidade e usa Flask-SQLAlchemy para persistência de dados com SQLite.

## ✅ **Principais funcionalidades:**

- Cadastro, listagem, atualização e remoção de pacientes.  
- Cadastro, listagem, atualização e remoção de profissionais de saúde.  
- Agendamento, atualização de status e cancelamento de consultas médicas.  
- API RESTful com suporte a CORS.

## **🚀 Como Rodar o Projeto**

### **1️⃣ Clonar o repositório em uma pasta desejada**

git clone https://github.com/AndrePereira03/backend.git  
cd backend

### **2️⃣ Criar e ativar o ambiente virtual**

python -m venv venv  
venv/Scripts/activate

### **3️⃣ Instalar as dependências**

pip install -r requirements.txt

### **4️⃣ Rodar a API**

python main.py

Se tudo estiver certo, a saída será algo como:

- Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
- A API estará disponível no endereço http://127.0.0.1:5000/.

A página inicial deverá exibir a mensagem:
"API está rodando! Acesse /paciente, /profissional ou /consulta"

### **5️⃣ Rodar os testes automatizados:**

pytest -v testes.py


## **🛠 Tecnologias Utilizadas**
- Python 3.8+
- Flask 3.1.0
- Flask-SQLAlchemy
- Flask-CORS
- SQLite
- Pytest para testes automatizados


## **📜 Licença**
Este projeto é de código aberto e está sob a licença MIT.


