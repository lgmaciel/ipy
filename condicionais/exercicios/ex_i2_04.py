temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura < 0:
    print("Congelante")
elif temperatura < 15:
    print("Frio")
elif temperatura < 25:
    print("Agradável")
elif temperatura < 35:
    print("Quente")
elif temperatura < 40:
    print("Muito quente")
elif temperatura >= 40:
    print("Extremamente quente")
