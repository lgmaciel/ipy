usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido")
elif usuario == "admin" and not senha == "1234":
    print("Usuário correto. Senha errada.")
else:
    print("Usuário ou senha incorretos")