### Exercício 1: Interpretação de Código - Verificação de Faixa Etária

**Código:**
```python
idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de entrada e saída.
3. Modifique o código para incluir uma nova faixa etária "Jovem Adulto" para idades entre 18 e 25 anos.

### Exercício 2: Interpretação de Código - Verificação de Nota com Mensagem Personalizada

**Código:**
```python
nota = float(input("Digite a nota do aluno: "))

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Insuficiente")
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de entrada e saída.
3. Modifique o código para incluir uma nova categoria "Muito Bom" para notas entre 8 e 9.

### Exercício 3: Interpretação de Código - Verificação de Categoria de Produto

**Código:**
```python
categoria = input("Digite a categoria do produto (A, B ou C): ")

if categoria == "A":
    print("Produto de alta qualidade")
elif categoria == "B":
    print("Produto de qualidade média")
elif categoria == "C":
    print("Produto de baixa qualidade")
else:
    print("Categoria inválida")
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de entrada e saída.
3. Modifique o código para incluir uma nova categoria "D" para produtos de qualidade premium.

### Exercício 4: Interpretação de Código - Verificação de Temperatura

**Código:**
```python
temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura < 0:
    print("Congelante")
elif temperatura < 15:
    print("Frio")
elif temperatura < 25:
    print("Agradável")
elif temperatura < 35:
    print("Quente")
else:
    print("Muito quente")
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de entrada e saída.
3. Modifique o código para incluir uma nova categoria "Extremamente quente" para temperaturas acima de 40 graus.

### Exercício 5: Interpretação de Código - Verificação de Login

**Código:**
```python
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido")
else:
    print("Usuário ou senha incorretos")
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de entrada e saída.
3. Modifique o código para incluir uma mensagem específica para quando o nome de usuário estiver correto, mas a senha estiver errada.