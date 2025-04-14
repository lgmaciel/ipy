### Exercício 1: Interpretação de Código - Loop `for` com `range`

**Código:**
```python
for i in range(3):
    print(f"Iteração {i}")
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de saída.
3. Modifique o código para que ele imprima "Iteração 1", "Iteração 2", "Iteração 3" (começando de 1).

---

### Exercício 2: Interpretação de Código - Loop `while` com Condição

**Código:**
```python
contador = 0

while contador < 3:
    print(f"Contador: {contador}")
    contador += 1
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de saída.
3. Modifique o código para que ele pare quando o contador atingir 5.

---

### Exercício 3: Interpretação de Código - Loop `for` com Lista

**Código:**
```python
nomes = ["Ana", "Bruno", "Carlos"]

for nome in nomes:
    print(f"Olá, {nome}!")
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de saída.
3. Modifique o código para que ele imprima "Bem-vindo, {nome}!" em vez de "Olá, {nome}!".

---

### Exercício 4: Interpretação de Código - Loop `while` com Entrada do Usuário

**Código:**
```python
senha = "1234"
entrada = ""

while entrada != senha:
    entrada = input("Digite a senha: ")
    if entrada == senha:
        print("Acesso permitido.")
    else:
        print("Senha incorreta. Tente novamente.")
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de entrada e saída.
3. Modifique o código para que ele permita apenas 3 tentativas antes de bloquear o acesso.

---

### Exercício 5: Interpretação de Código - Loop `for` com Condicional

**Código:**
```python
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} é par.")
    else:
        print(f"{i} é ímpar.")
```

**Instruções:**
1. Explique o que o código faz.
2. Dê exemplos de saída.
3. Modifique o código para que ele imprima apenas os números pares.