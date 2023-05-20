import sqlite3

conexao = sqlite3.connect('escola.db')



#inserir dados
def inserir_dados(i):
    with conexao:
        cursor = conexao.cursor()
        funcao = 'INSERT INTO Alunos (Nome, Educacao_especial, Turma, Notas, Professor, Anotacoes) VALUES (?, ?, ?, ?, ?, ?)'
        cursor.execute(funcao, i)



#ver dados da tabela
def ver_dados():
    lista = []
    with conexao:
        cursor = conexao.cursor()
        funcao = 'SELECT * FROM Alunos'
        cursor.execute(funcao)
        dados = cursor.fetchall()

        for i in dados:
            lista.append(i)
        return lista



'''lista = []
#atualizar dados
with conexao:
    cursor = conexao.cursor()
    funcao = 'UPDATE Alunos SET Nome=? WHERE id_aluno=?'
    cursor.execute(funcao, lista)



lista = []
#deletar dados
with conexao:
    cursor = conexao.cursor()
    funcao = 'DELETE FROM Alunos WHERE id_aluno=?'
    cursor.execute(funcao, lista)'''