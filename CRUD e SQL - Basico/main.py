import sqlite3
import os

db_file = 'CRUD e SQL - Basico/alunos.db'

# Verificar se o banco de dados já existe
# Caso exista, ele pula esta etapa do código e vai direto para o CRUD
# Caso não exista, ele cria o banco de dados e a tabela Alunos e depois vai para o CRUD

if not os.path.exists(db_file):

    # Conectando ao banco de dados (será criado se não existir)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Criando a tabela Alunos
    cursor.execute('''
        CREATE TABLE Alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# =========================================================================== CRUD + SQL ===================================================================================

# CREATE

def inserir_aluno(nome, idade):
    conn = sqlite3.connect('CRUD e SQL - Basico/alunos.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Alunos (nome, idade) VALUES (?, ?)
    ''', (nome, idade))

    conn.commit()
    conn.close()

# READ

def listar_alunos():
    conn = sqlite3.connect('CRUD e SQL - Basico/alunos.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Alunos')
    alunos = cursor.fetchall()

    for aluno in alunos:
        print(aluno)

    conn.close()

# UPDATE

def atualizar_nome_aluno(id_aluno, novo_nome):
    conn = sqlite3.connect('CRUD e SQL - Basico/alunos.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE Alunos SET nome = ? WHERE id = ?
    ''', (novo_nome, id_aluno))

    conn.commit()
    conn.close()

# DELETE

def deletar_aluno(id_aluno):
    conn = sqlite3.connect('CRUD e SQL - Basico/alunos.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Alunos WHERE id = ?', (id_aluno,))

    conn.commit()
    conn.close()


# ================================================================================================================================================================

# Inserindo alunos
inserir_aluno('João', 20)
inserir_aluno('Maria', 22)
inserir_aluno('Pedro', 25)
inserir_aluno('Paulo', 30)

# Listando alunos
print('Listando alunos após inserção')
listar_alunos()
print('\n')

# Atualizando nome do aluno
atualizar_nome_aluno(1, 'João da Silva')

# Listando alunos
print('Listando alunos após atualização')
listar_alunos()
print('\n')

# Deletando aluno
deletar_aluno(2)

# Listando alunos
print('Listando alunos após deleção')
listar_alunos()
print('\n')