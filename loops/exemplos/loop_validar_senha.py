senha_valida = False

while not senha_valida:
    senha = input("senha: ")    
    senha_valida = senha == "abcde"
    if not senha_valida:
        print("senha inválida")

print("senha válida") 
