### Exercício 1: Substituição de Variáveis

Analise o código abaixo e determine o valor das variáveis `a`, `b` e `c` após a execução do código.

```python
a = 10
b = 5
c = a + b
a = 20
b = a - b
c = c + a
```

1. Qual é o valor de `a` após a execução do código?
2. Qual é o valor de `b` após a execução do código?
3. Qual é o valor de `c` após a execução do código?

### Exercício 2: Interpolação de Valores em Strings

Analise o código abaixo e determine a saída impressa no console.

```python
nome = "Alice"
idade = 30
peso = 65.5

saudacao = "Olá, " + nome + "! Você tem " + str(idade) + " anos e pesa " + str(peso) + " kg."
print(saudacao)

saudacao_fstring = f"Olá, {nome}! Você tem {idade} anos e pesa {peso} kg."
print(saudacao_fstring)
```

1. Qual é a saída impressa pela primeira instrução `print(saudacao)`?
2. Qual é a saída impressa pela segunda instrução `print(saudacao_fstring)`?

### Exercício 3: Uso de Expressões Aritméticas em fStrings

Analise o código abaixo e determine a saída impressa no console.

```python
x = 10
y = 3

resultado = f"A soma de {x} e {y} é {x + y}."
print(resultado)

resultado2 = f"A diferença entre {x} e {y} é {x - y}."
print(resultado2)

resultado3 = f"O produto de {x} e {y} é {x * y}."
print(resultado3)

resultado4 = f"A divisão de {x} por {y} é {x / y}."
print(resultado4)
```

1. Qual é a saída impressa pela primeira instrução `print(resultado)`?
2. Qual é a saída impressa pela segunda instrução `print(resultado2)`?
3. Qual é a saída impressa pela terceira instrução `print(resultado3)`?
4. Qual é a saída impressa pela quarta instrução `print(resultado4)`?