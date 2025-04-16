idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade >= 18 and idade <25:
    print("Jovem Adulto")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")