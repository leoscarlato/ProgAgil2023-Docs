from flask import Flask
from flask import request
import sqlite3

DATABASE = "alunos.db"

app = Flask(__name__)

# Criando aluno

@app.route("/aluno", methods=["POST"])
def criar_aluno():
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    nome = request.json["nome"]
    idade = request.json["idade"]

    cursor.execute(""" INSERT INTO alunos (nome, idade) VALUES (?, ?) """, (nome, idade))
    
    conn.commit()
    
    return {"messagem": "Aluno criado com sucesso!"}, 201

# Listando alunos

@app.route("/aluno", methods=["GET"])
def listar_alunos():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(""" SELECT * FROM alunos """)

    alunos = cursor.fetchall()

    return {"alunos": alunos}, 200

# Buscando aluno por id

@app.route("/aluno/<int:id>", methods=["GET"])
def buscar_aluno(id):
         
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(""" SELECT * FROM alunos WHERE id = ? """, (id,))

    aluno = cursor.fetchone()

    return {"aluno": aluno}, 200
    
# Atualizando aluno

@app.route("/aluno/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    data = request.json

    for key, value in data.items():
        if key != "nome" and key != "idade":
            return {"mensagem": f"Chave {key} inválida"}, 400
        
        cursor.execute(f""" UPDATE alunos SET {key} = ? WHERE id = ? """, (value, id))

    conn.commit()

    return {"mensagem": "Aluno atualizado com sucesso!"}, 200

# Deletando aluno

@app.route("/aluno/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
        
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(""" DELETE FROM alunos WHERE id = ? """, (id,))
    
    conn.commit()
    
    return {"mensagem": "Aluno deletado com sucesso!"}, 200


if __name__ == "__main__":
    app.run(debug=True)
