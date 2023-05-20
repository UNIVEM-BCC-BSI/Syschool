import sqlite3

#conexao
try:
    conexao = sqlite3.connect('escola.db')
    print('Banco de dados conectado com sucesso.')
except sqlite3.Error as i:
    print(f'Erro ao conectar ao banco de dados: {i}')

#tabela alunos
try:
    with conexao:
        cursor = conexao.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Alunos (
            id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT,
            Educacao_especial TEXT,
            Turma TEXT,
            Notas REAL,
            Professor TEXT,
            Anotacoes TEXT
        )""")
        print('Tabela Alunos criada com sucesso.')
except sqlite3.Error as i:
    print(f'Erro ao criar a tabela de alunos: {i}')
