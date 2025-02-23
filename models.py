from db import db

class Paciente(db.Model):
    __tablename__ = "pacientes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(15))
    consultas = db.relationship("Consulta", back_populates="paciente", cascade="all, delete")

class ProfissionalSaude(db.Model):
    __tablename__ = "profissionais_saude"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    credencial = db.Column(db.String(50), unique=True, nullable=False)
    consultas = db.relationship("Consulta", back_populates="profissional", cascade="all, delete")

class Consulta(db.Model):
    __tablename__ = "consultas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey("pacientes.id"), nullable=False)
    profissional_id = db.Column(db.Integer, db.ForeignKey("profissionais_saude.id"), nullable=False)
    data_hora = db.Column(db.String(50), nullable=False) 
    status = db.Column(db.String(50), default="agendada")

    paciente = db.relationship("Paciente", back_populates="consultas")
    profissional = db.relationship("ProfissionalSaude", back_populates="consultas")