from flask import request, jsonify
from db import create_app, db
from models import Paciente, ProfissionalSaude, Consulta

app = create_app()

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return "API está rodando! Acesse /paciente, /profissional ou /consulta"

# CRUD paciente
@app.route("/paciente", methods=["GET"])
@app.route("/paciente/<int:paciente_id>", methods=["GET"])
def get_paciente(paciente_id=None):
    if paciente_id:
        paciente = Paciente.query.get(paciente_id)
        if paciente:
            return jsonify({"id": paciente.id, "nome": paciente.nome, "email": paciente.email, "cpf": paciente.cpf})
        return {"message": "Paciente não encontrado"}, 404
    pacientes = Paciente.query.all()
    return jsonify([{"id": p.id, "nome": p.nome, "email": p.email, "cpf": p.cpf} for p in pacientes])

@app.route("/paciente", methods=["POST"])
def create_paciente():
    data = request.json
    novo_paciente = Paciente(nome=data["nome"], email=data["email"], cpf=data["cpf"], telefone=data.get("telefone"))
    db.session.add(novo_paciente)
    db.session.commit()
    return {"message": "Paciente criado com sucesso", "id": novo_paciente.id}, 201

@app.route("/paciente/<int:paciente_id>", methods=["PUT"])
def update_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return {"message": "Paciente não encontrado"}, 404
    data = request.json
    paciente.nome = data.get("nome", paciente.nome)
    paciente.email = data.get("email", paciente.email)
    paciente.telefone = data.get("telefone", paciente.telefone)
    db.session.commit()
    return {"message": "Paciente atualizado com sucesso"}

@app.route("/paciente/<int:paciente_id>", methods=["DELETE"])
def delete_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return {"message": "Paciente não encontrado"}, 404
    db.session.delete(paciente)
    db.session.commit()
    return {"message": "Paciente excluído com sucesso"}

# CRUD prof. saude
@app.route("/profissional", methods=["POST"])
def create_profissional():
    data = request.json
    novo_profissional = ProfissionalSaude(nome=data["nome"], especialidade=data["especialidade"], credencial=data["credencial"])
    db.session.add(novo_profissional)
    db.session.commit()
    return {"message": "Profissional criado com sucesso", "id": novo_profissional.id}, 201

@app.route("/profissional/<int:profissional_id>", methods=["GET"])
def get_profissional(profissional_id):
    profissional = ProfissionalSaude.query.get(profissional_id)
    if profissional:
        return jsonify({"id": profissional.id, "nome": profissional.nome, "especialidade": profissional.especialidade})
    return {"message": "Profissional não encontrado"}, 404

# CRUD consulta
@app.route("/consulta", methods=["POST"])
def create_consulta():
    data = request.json
    nova_consulta = Consulta(paciente_id=data["paciente_id"], profissional_id=data["profissional_id"], data_hora=data["data_hora"], status="agendada")
    db.session.add(nova_consulta)
    db.session.commit()
    return {"message": "Consulta agendada com sucesso", "id": nova_consulta.id}, 201

@app.route("/consulta/<int:consulta_id>", methods=["GET"])
def get_consulta(consulta_id):
    consulta = Consulta.query.get(consulta_id)
    if consulta:
        return jsonify({"id": consulta.id, "paciente_id": consulta.paciente_id, "profissional_id": consulta.profissional_id, "data_hora": consulta.data_hora, "status": consulta.status})
    return {"message": "Consulta não encontrada"}, 404

@app.route("/consulta/<int:consulta_id>", methods=["DELETE"])
def delete_consulta(consulta_id):
    consulta = Consulta.query.get(consulta_id)
    if not consulta:
        return {"message": "Consulta não encontrada"}, 404
    db.session.delete(consulta)
    db.session.commit()
    return {"message": "Consulta excluída com sucesso"}


if __name__ == "__main__":
    app.run(debug=True)
