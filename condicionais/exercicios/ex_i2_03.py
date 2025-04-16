categoria = input("Digite a categoria do produto (A, B ou C): ")
categoria = categoria.upper()

if categoria == "A":
    print("Produto de alta qualidade")
elif categoria == "D":
    print("Produto de qualidade premium")
elif categoria == "B":
    print("Produto de qualidade média")
elif categoria == "C":
    print("Produto de baixa qualidade")
else:
    print("Categoria inválida")