"""
Exemplo de programa com interface em linha de comando (CLI)

"""
import sys
import datetime
"""
Modelo: dados e funções que acessam e manipulam esses dados
"""

# dados

hora =  datetime.datetime.now()
titulo = "exemplo de programa com interface em linha de comando"
frase = "Time is Money!"
 
"""
Visão: funções que recebem dados do usuário e mostram dados ao usuário
Note que nenhuma destas funções acessa dados do Modelo diretamente.
"""
def view_mostrar_hora(uma_hora):
    print(f'horas: {uma_hora}')

def view_mostrar_titulo(um_titulo):
    print(f'título: {um_titulo}')

def view_mostrar_frase(uma_frase):
    print(f'frase: {uma_frase}')

"""
Controlador: funções responsáveis por:
- receber dados da camada de Visão;
- consultar a camada de Modelo; 
- chamar funções da camada de Visão para mostrar
  respostas recebidas da camada de Modelo ao usuário

  V -> C -> M  (usuário dá um comando)
  V <- C <- M (usuário recebe resposta)
"""

def ctrl_horas():
    view_mostrar_hora(hora)

def ctrl_titulo():
    view_mostrar_titulo(titulo)

def ctrl_frase():
    view_mostrar_frase(frase)
    

"""
TESTES:


"""

# chamando funções do Controlador
ctrl_horas()
ctrl_titulo()
ctrl_frase()


