## Operadores lógicos

Agora que você já entende como usar desvios condicionais com `if` e `else` em Python, vamos aprender sobre operadores lógicos. 

Operadores lógicos nos ajudam a combinar várias condições em uma única expressão lógica. Isso é útil quando queremos verificar se mais de uma coisa é verdadeira ao mesmo tempo.

Os principais operadores lógicos em Python são:

1. **E lógico (`and`)**: Usado para verificar se duas condições são verdadeiras ao mesmo tempo.
2. **OU lógico (`or`)**: Usado para verificar se pelo menos uma das condições é verdadeira.
3. **NÃO lógico (`not`)**: Usado para inverter a verdade de uma condição.

Vamos ver alguns exemplos:

### Exemplo 1: Usando `and`

```python
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")
```

Neste exemplo, o programa verifica se a idade é maior ou igual a 18 **e** (`and`) se a pessoa tem carteira de motorista. Ambos precisam ser verdadeiros para que a mensagem "Você pode dirigir." seja impressa.

### Exemplo 2: Usando `or`

```python
dia = "domingo"
tempo = "chuvoso"

if dia == "sábado" or dia == "domingo":
    print("É fim de semana!")
else:
    print("É dia de semana.")
```

Neste exemplo, o programa verifica se o dia é "sábado" **ou** (`or`)"domingo". Se pelo menos uma dessas condições for verdadeira, a mensagem "É fim de semana!" será impressa.

### Exemplo 3: Usando `not`

```python
esta_chovendo = False

if not esta_chovendo:
    print("Vamos à praia!")
else:
    print("Vamos ao cinema.")
```

Neste exemplo, o programa verifica se **não** (`not`) está chovendo. Se a condição `esta_chovendo` for falsa, a mensagem "Vamos à praia!" será impressa.

### Comparando Strings

Operadores lógicos também podem ser usados para comparar strings. Vamos ver alguns exemplos:

```python
fruta = "maçã"

if fruta == "maçã" or fruta == "laranja":
    print("Você escolheu uma fruta cítrica.")
else:
    print("Você escolheu outra fruta.")
```

Neste exemplo, o programa verifica se a variável `fruta` é igual a "maçã" **ou** "laranja". Se pelo menos uma dessas condições for verdadeira, a mensagem "Você escolheu uma fruta cítrica." será impressa.

### Exemplo com `and` e Strings

```python
nome = "Ana"
sobrenome = "Silva"

if nome == "Ana" and sobrenome == "Silva":
    print("Olá, Ana Silva!")
else:
    print("Olá, visitante!")
```

Neste exemplo, o programa verifica se o `nome` é "Ana" **e** o `sobrenome` é "Silva". Ambos precisam ser verdadeiros para que a mensagem "Olá, Ana Silva!" seja impressa.
