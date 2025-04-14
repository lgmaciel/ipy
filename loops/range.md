## A Função `range()` em Loops

A função `range()` é muito útil em Python para gerar sequências de números. Ela é frequentemente usada em loops para controlar o número de iterações. Vamos explorar como utilizá-la em loops `for` e `while` com exemplos práticos.

### Usando `range()` em Loops `for`

#### Exemplo 1: Iterando sobre uma sequência de números

O loop `for` pode usar a função `range()` para iterar sobre uma sequência de números. Por exemplo:

```python
for i in range(5):
    print(f"Número: {i}")
```

Neste exemplo, o loop `for` itera de 0 a 4 (5 não é incluído). A cada iteração, o valor de `i` é impresso.

#### Exemplo 2: Iterando com um passo personalizado

A função `range()` também permite especificar um passo diferente de 1:

```python
for i in range(0, 10, 2):
    print(f"Número par: {i}")
```

Aqui, o loop `for` itera de 0 a 8, incrementando de 2 em 2. Apenas números pares são impressos.

### Usando `range()` em Loops `while`

Embora a função `range()` seja mais comumente usada com loops `for`, também podemos utilizá-la em loops `while` para controlar as iterações.

#### Exemplo 1: Iterando com um índice

Podemos usar `range()` para criar uma sequência e iterar sobre ela com um loop `while`:

```python
numeros = list(range(5))
indice = 0

while indice < len(numeros):
    print(f"Número: {numeros[indice]}")
    indice += 1
```

Neste exemplo, criamos uma lista de números usando `range()` e iteramos sobre ela com um loop `while`.

#### Exemplo 2: Iterando com um passo personalizado

Também podemos usar `range()` para criar uma sequência com um passo personalizado e iterar sobre ela:

```python
numeros = list(range(0, 10, 3))
indice = 0

while indice < len(numeros):
    print(f"Número múltiplo de 3: {numeros[indice]}")
    indice += 1
```

Aqui, criamos uma lista de números múltiplos de 3 usando `range()` e iteramos sobre ela com um loop `while`.
