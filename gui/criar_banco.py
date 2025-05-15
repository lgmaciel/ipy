# Importando a biblioteca Tkinter
import sqlite3
import tkinter as tk
from tkinter import messagebox

def criar_banco_de_dados():
    nome_banco = tx_nome.get() #pegando conteúdo da caixa de texto (Entry)
    conexao = sqlite3.connect(f'{nome_banco}.db')    
    conexao.close()    
    messagebox.showinfo("Info", "Banco de dados criado.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Criar banco de dados")
janela.geometry("320x200+500+300")

# Adicionando um rótulo
rotulo = tk.Label(janela, text="Nome do banco de dados:")
rotulo.pack()

# Adicionando uma entrada de texto
tx_nome = tk.Entry(janela)
tx_nome.pack()

# Adicionando um botão
botao = tk.Button(janela, text="Criar", command=criar_banco_de_dados)
botao.pack()

# Iniciando o loop principal da aplicação
janela.mainloop()