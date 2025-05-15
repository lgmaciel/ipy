# mapa com dados da agenda (o "banco de dados")
agenda = {} # começa com um mapa vazio

# definição das funções do sistama

def adicionar(email, dados): # dados é uma list    
    global agenda
    agenda[email] = dados

def consultar(email):
    global agenda
    return agenda[email]

def excluir(email):
    global agenda
    try:
        del agenda[email]
    except KeyError:
        return False
    
    return True

def atualizar(email, dados): # dados é uma list com os novos valores do registro
    global agenda
    agenda[email] = dados