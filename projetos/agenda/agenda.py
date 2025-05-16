
"""
Model da Agenda
autor: gustavo razzera
data: 16/05/2025
"""

minha_agenda = {}

def cadastrar(agenda, email, nome, idade, endereco, favorito=False):
    status = False
    if not email in agenda.keys():
        agenda[email] = [nome, idade, endereco, favorito]
        status = True

    return (status, email)

def atualizar(agenda, email, nome, idade, endereco, favorito=False):    
    status = True
    try:
        agenda[email] = [nome, idade, endereco, favorito]        
    except KeyError:
        status = False
    return (status, email)

def favoritar(agenda, email):
    status = True
    try:
        agenda[email][3] = True        
    except KeyError:
        status = False
    return (status, email)

def apagar(agenda, email):
    status = True
    try:
        del agenda[email]
    except KeyError:
        status = False

    return (status, email)

"""
def consultar(agenda, email):
    if email in agenda.keys():
        return agenda[email]
    else:
        return None
"""
"""
def consultar(agenda, email):
    try:
        return agenda[email]
    except KeyError:
        return None
"""

def consultar(agenda, email):
    status = True
    dados = []
    try:
         dados = agenda[email]
    except KeyError:
        status = False

    return(status, dados)

def listagem(agenda):
    return agenda.items()

def agenda_init():
    cadastrar(minha_agenda, 'srx@email.com', 'Sr. X', 30, 'Rua x')
    cadastrar(minha_agenda, 'sry@email.com', 'Sr. Y', 31, 'Rua y', True)

"""
    View da agenda
"""
def imprimir(registros):
    for email, dados in registros:        
        print(f'''e-mail: {email}
    Nome: {dados[0]}        
    Endereço: {dados[2]}
    Idade: {dados[1]}
    Favorito: {dados[3]}        
    ''')

def imprimir_um(registro):
     email, dados = registro
     print(f'''e-mail: {email}
    Nome: {dados[0]}        
    Endereço: {dados[2]}
    Idade: {dados[1]}
    Favorito: {dados[3]}        
    ''')
"""
Controlador da Agenda

"""
agenda_init()
print("Agenda 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS")

# inicia testes de uso do sistema

def test_ctrl_cadastrar():
    # CADASTRAR: recebe dados da view
    email = 'srz@email.com'
    nome = 'Sr. Z'
    idade = 32
    endereco = 'Rua z'

    # pedir que a model cadastre o novo registro
    ok, email = cadastrar(minha_agenda, email, nome, idade, endereco)

    # pede à View que informe o usuário sobre o resultado da operação
    if ok:
        print(f'{email} cadastrado com sucesso')
    else:
        print(f'Não cadastrado: {email} já existe na agenda')

def test_ctrl_consultar():
    # recebe dados da view
    email = "srz@email.com" # deveria ser um input() ou algo assim...
    # consultar model
    ok, registros = consultar(minha_agenda, email)
    if ok:
        # repassar para a camada de View os dados obtidos da Model
        imprimir_um((email, registros))
    else:
        print("Registro não encontrado")

def test_ctrl_apagar():
    sucesso = apagar(minha_agenda,'sry@email.com')
    if sucesso:
        print("Registro excluído")
    else:
        print("Registro inexistente")

def test_ctrl_atualizar():
    # ATUALIZAR
    email = 'srz@email.com'
    nome = 'Senhor Ze'
    idade = 31
    endereco = 'Rua do sr. Z'

    # pedir que a model atualize o novo registro
    ok, email = atualizar(minha_agenda, email, nome, idade, endereco)

    # pede à View que informe o usuário sobre o resultado da operação
    if ok:
        print(f'{email} atualizado com sucesso')
        status, dados = consultar(minha_agenda, email)
        imprimir_um((email, dados))
    else:
        print(f'{email} não existe na agenda')

def test_ctrl_favoritar():
    test_ctrl_cadastrar() # cadastra srz@email.com
    test_ctrl_consultar() # consulta srz@email.com para confirmar
    
    print(f'*** Favoritando...')
    
    ok, email = favoritar(minha_agenda, "srz@email.com")
    if ok:
        test_ctrl_consultar() # consulta e lista srz@email.com
        print(f'{email} favoritado!')
    else:
        print(f"{email} inexistente")

"""
Rodando TESTES
"""

test_ctrl_favoritar()