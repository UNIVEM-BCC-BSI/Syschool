from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlite3

# Acima ocorre a importação das ferramentas do toolkit Kivy e banco Sqlite3

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # Construtor grid layout
        super(MyGridLayout, self).__init__(**kwargs)
        # Colunas
        self.cols = 2
        # Linhas
        self.rows = 8

        # Widgets de label e input
        self.add_widget(Label(text="Cadastro de Alunos", font_size=25))
        self.add_widget(Label(text=""))

        self.add_widget(Label(text="Nome do Aluno: "))
        self.aluno = TextInput()
        self.add_widget(self.aluno)

        self.add_widget(Label(text="Professor: "))
        self.professor = TextInput()
        self.add_widget(self.professor)

        self.add_widget(Label(text="Educação Especial: "))
        self.educacao = TextInput()
        self.add_widget(self.educacao)

        self.add_widget(Label(text="Nota bimestral: "))
        self.nota = TextInput()
        self.add_widget(self.nota)

        self.add_widget(Label(text="Anotações: "))
        self.anotacoes = TextInput()
        self.add_widget(self.anotacoes)

        # Botões
        self.incluir = Button(text="Incluir")
        # Definindo a função que será chamada ao apertar o botão
        self.incluir.bind(on_press=self.incluir_dados)
        self.add_widget(self.incluir)

        self.deletar = Button(text="Deletar")
        # Definindo a função que será chamada ao apertar o botão
        self.deletar.bind(on_press=self.deletar_dados)
        self.add_widget(self.deletar)

        self.alterar = Button(text="Alterar")
        # Definindo a função que será chamada ao apertar o botão
        self.alterar.bind(on_press=self.alterar_dados)
        self.add_widget(self.alterar)

    # Definindo as funções
    def incluir_dados(self, instance):
        # Obtendo os valores dos inputs
        aluno = self.aluno.text
        professor = self.professor.text
        educacao = self.educacao.text
        nota = self.nota.text
        anotacoes = self.anotacoes.text

        # Banco de dados
        conexao = sqlite3.connect("meu_banco.db")
        # Cursor para interagir com o banco
        cursor = conexao.cursor()
        # Criando a tabela
        cursor.execute("CREATE TABLE minha_tabela (aluno TEXT, professor TEXT, educacao REAL, nota TEXT, anotacoes TEXT)")

        # Inserindo dados
        cursor.execute("INSERT INTO minha_tabela (aluno, professor, educacao, nota, anotacoes) VALUES (?, ?, ?, ?, ?)",
                       (aluno, professor, educacao, nota, anotacoes))
        # Salvando
        conexao.commit()
        # Fechando a conexão
        cursor.close()
        conexao.close()

        # limpando os inputs
        self.aluno.text = ""
        self.professor.text = ""
        self.educacao.text = ""
        self.nota.text = ""
        self.anotacoes.text = ""

    def deletar_dados(self, instance):
        # Obtendo os valores dos inputs
        aluno = self.aluno.text
        professor = self.professor.text
        educacao = self.educacao.text
        nota = self.nota.text
        anotacoes = self.anotacoes.text

        # Deletando dados
        cursor.execute("DELETE FROM minha_tabela (aluno, professor, educacao, nota, anotacoes) WHERE (?, ?, ?, ?, ?)",
                       (aluno, professor, educacao, nota, anotacoes))
        # Salvando
        conexao.commit()
        # Fechando a conexão
        cursor.close()
        conexao.close()

        # limpando os inputs
        self.aluno.text = ""
        self.professor.text = ""
        self.educacao.text = ""
        self.nota.text = ""
        self.anotacoes.text = ""
    def alterar_dados(self, instance):
        # Obtendo os valores dos inputs
        aluno = self.aluno.text
        professor = self.professor.text
        educacao = self.educacao.text
        nota = self.nota.text
        anotacoes = self.anotacoes.text

        # Alterando dados
        cursor.execute("UPDATE minha_tabela SET (aluno, professor, educacao, nota, anotacoes) WHERE (?, ?, ?, ?, ?)",
                       (aluno, professor, educacao, nota, anotacoes))
        # Salvando
        conexao.commit()
        # Fechando a conexão
        cursor.close()
        conexao.close()

        # limpando os inputs
        self.aluno.text = ""
        self.professor.text = ""
        self.educacao.text = ""
        self.nota.text = ""
        self.anotacoes.text = ""

# Classe de exibição de tela
class MyApp(App):
    def build(self):
        self.title = "Syschool"
        #label = Label(text="Cadastro de Alunos")
        #return label
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()
