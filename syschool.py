from tkinter import *
from tkinter import ttk
from funcoes import *

#cores
cor = '#f0f3f5'  #preto
cor1 = '#feffff'  #branco
cor2 = '#df9091' #vermelho
cor3 = '#a9cc90' #verde
cor4 = '#9ea5b6' #azul
cor5 = '#eff0f2' #cinzinha
cor6 = '#dddee8' #cinzinha mais escuro

#janela do sistema
janela = Tk()
janela.title('Syschool')
janela.geometry('1100x460')
janela.resizable(False,False)



#divisoes da janela
faixa1 = Frame(janela, width=310, height=50, relief='flat', bg=cor6)
faixa1.grid(row=0, column=0)

faixa2 = Frame(janela, width=310, height=400, bg=cor5, relief='flat')
faixa2.grid(row=1, column=0, sticky=NSEW, pady=1)

faixa3 = Frame(janela, width=900, height=400, bg=cor1, relief='flat')
faixa3.grid(row=0, column=1, sticky=NSEW, padx=1, rowspan=2)



#faixa1 titulo
titulo = Label(faixa1, text='Cadastro de alunos', relief='flat', font=('verdana', 15, 'bold'), bg=cor6)
titulo.place(x=10,y=10)



def inserir():
    Nome = entrada_nome.get()
    Professor = entrada_prof.get()
    Educacao_especial = entrada_ed.get()
    Turma = entrada_turma.get()
    Notas = entrada_nota.get()
    Anotacoes = entrada_anot.get()
    
    lista = [Nome, Educacao_especial, Turma, Notas, Professor, Anotacoes]
    inserir_dados(lista)

    entrada_nome.delete(0, 'end')
    entrada_prof.delete(0, 'end')
    entrada_ed.delete(0, 'end')
    entrada_turma.delete(0, 'end')
    entrada_nota.delete(0, 'end')
    entrada_anot.delete(0, 'end')

    for widget in faixa3.winfo_children():
        widget.destroy()
    
    ver()


#faixa 2 campos
campo_nome = Label(faixa2, text='Nome: ', relief='flat', font=('arial', 10))
campo_nome.place(x=10,y=10)
entrada_nome = Entry(faixa2, width=45, relief='solid', justify='left')
entrada_nome.place(x=10,y=38)

campo_prof = Label(faixa2, text='Professor(a): ', relief='flat', font=('arial', 10))
campo_prof.place(x=10,y=70)
entrada_prof = Entry(faixa2, width=45, relief='solid', justify='left')
entrada_prof.place(x=10,y=98)

campo_ed = Label(faixa2, text='Educação Especial: ', relief='flat', font=('arial', 10))
campo_ed.place(x=10,y=130)
entrada_ed = Entry(faixa2, width=45, relief='solid', justify='left')
entrada_ed.place(x=10,y=158)

campo_turma = Label(faixa2, text='Turma: ', relief='flat', font=('arial', 10))
campo_turma.place(x=10,y=190)
entrada_turma = Entry(faixa2, width=15, relief='solid', justify='left')
entrada_turma.place(x=10,y=218)

campo_nota = Label(faixa2, text='Nota bimestral: ', relief='flat', font=('arial', 10))
campo_nota.place(x=160,y=190)
entrada_nota = Entry(faixa2, width=20, relief='solid', justify='left')
entrada_nota.place(x=160,y=218)

campo_anot = Label(faixa2, text='Anotações: ', relief='flat', font=('arial', 10))
campo_anot.place(x=10,y=250)
entrada_anot = Entry(faixa2, width=45, relief='solid', justify='left')
entrada_anot.place(x=10,y=278)



#botões
b_inserir = Button(faixa2, text='Inserir', command= inserir, relief='raised', font=('verdana', 8, 'bold'), bg=cor3, fg=cor1, overrelief='ridge')
b_inserir.place(x=10,y=330)

b_atualizar = Button(faixa2, text='Alterar', relief='raised', font=('verdana', 8, 'bold'), bg=cor4, fg=cor1, overrelief='ridge')
b_atualizar.place(x=80,y=330)

b_del = Button(faixa2, text='Deletar', relief='raised', font=('verdana', 8, 'bold'), bg=cor2, fg=cor1, overrelief='ridge')
b_del.place(x=163,y=330)







def ver():

    lista = ver_dados()

    #campo de visualização dos dados na lista
    itens_lista = ['ID','Nome', 'Educação especial','Turma', 'Nota do Bimestre', 'Professor(a)','Anotações']
    tree = ttk.Treeview(faixa3, selectmode = 'extended', columns = itens_lista, show= 'headings')
    tree.grid(column=0, row=0, sticky='nsew')
    faixa3.grid_rowconfigure(0, weight=12)

    #formatação dos campos
    centro = ['center', 'center', 'center', 'center', 'center', 'center','w']
    comprim = [30, 170, 120, 70, 120, 100, 160]
    n = 0

    for i in itens_lista:
        tree.heading(i, text = i.title(), anchor=CENTER)
        tree.column(i, width = comprim[n], anchor = centro[n])
        n += 1

    for dados in lista:
        tree.insert('', 'end', values = dados)

#funções
ver()

#abrir janela
janela.mainloop()
