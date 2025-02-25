import pytest
from flask import json
from db import create_app, db
from models import Paciente, ProfissionalSaude, Consulta

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_create_paciente(client):
    response = client.post("/paciente", json={
        "nome": "João", 
        "email": "joao@email.com", 
        "cpf": "12345678900",
        "telefone": "11987654321"
    })
    assert response.status_code == 201
    assert response.json["message"] == "Paciente criado com sucesso"

def test_get_pacientes(client):
    client.post("/paciente", json={
        "nome": "Maria", 
        "email": "maria@email.com", 
        "cpf": "98765432100",
        "telefone": "11976543210"
    })
    response = client.get("/paciente")
    assert response.status_code == 200
    assert len(response.json) == 1

def test_update_paciente(client):
    response = client.post("/paciente", json={
        "nome": "Carlos", 
        "email": "carlos@email.com", 
        "cpf": "11122233344",
        "telefone": "11912345678"
    })
    paciente_id = response.json["id"]
    response = client.put(f"/paciente/{paciente_id}", json={
        "nome": "Carlos Silva",
        "telefone": "11987654321"
    })
    assert response.status_code == 200
    assert response.json["message"] == "Paciente atualizado com sucesso"

def test_delete_paciente(client):
    response = client.post("/paciente", json={
        "nome": "Ana", 
        "email": "ana@email.com", 
        "cpf": "55566677788",
        "telefone": "11955566677"
    })
    paciente_id = response.json["id"]
    response = client.delete(f"/paciente/{paciente_id}")
    assert response.status_code == 200
    assert response.json["message"] == "Paciente excluído com sucesso"

def test_create_profissional(client):
    response = client.post("/profissional", json={
        "nome": "Dr. Pedro", 
        "especialidade": "Cardiologia", 
        "credencial": "CRM123"
    })
    assert response.status_code == 201
    assert response.json["message"] == "Profissional criado com sucesso"

def test_create_consulta(client):
    paciente = client.post("/paciente", json={
        "nome": "Bruno", 
        "email": "bruno@email.com", 
        "cpf": "66677788899",
        "telefone": "11999988877"
    })
    profissional = client.post("/profissional", json={
        "nome": "Dr. Ricardo", 
        "especialidade": "Ortopedia", 
        "credencial": "CRM987"
    })
    
    paciente_id = paciente.json["id"]
    profissional_id = profissional.json["id"]
    
    response = client.post("/consulta", json={
        "paciente_id": paciente_id, 
        "profissional_id": profissional_id, 
        "data_hora": "2025-03-01T10:00:00"
    })
    assert response.status_code == 201
    assert response.json["message"] == "Consulta agendada com sucesso"

def test_update_consulta_status(client):
    paciente = client.post("/paciente", json={
        "nome": "Juliana", 
        "email": "juliana@email.com", 
        "cpf": "99988877766",
        "telefone": "11888877766"
    })
    profissional = client.post("/profissional", json={
        "nome": "Dra. Camila", 
        "especialidade": "Dermatologia", 
        "credencial": "CRM654"
    })
    
    paciente_id = paciente.json["id"]
    profissional_id = profissional.json["id"]
    
    consulta = client.post("/consulta", json={
        "paciente_id": paciente_id, 
        "profissional_id": profissional_id, 
        "data_hora": "2025-03-05T15:00:00"
    })
    consulta_id = consulta.json["id"]
    
    response = client.patch(f"/consulta/{consulta_id}", json={
        "status": "Confirmada"
    })
    assert response.status_code == 200
    assert response.json["message"] == "Status da consulta atualizado com sucesso"
    assert response.json["consulta"]["status"] == "Confirmada"
