## Desvios condicionais

Imagine que você está em uma cozinha e quer fazer um bolo. Você precisa seguir uma receita, mas algumas etapas dependem de condições específicas. Por exemplo, se você tiver ovos, você pode fazer um bolo de chocolate. Se não tiver ovos, você pode fazer um bolo de banana. Essas decisões são como desvios condicionais em programação.

Em Python, usamos a palavra-chave `if` (se) para criar essas decisões. Vamos ver um exemplo simples:

```python
idade = 15

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

Neste exemplo, o programa verifica se a variável `idade` é maior ou igual a 18. Se for verdadeiro, ele imprime "Você é maior de idade." Se não for verdadeiro, ele imprime "Você é menor de idade."

Vamos detalhar essas etapas:

1. **`if idade >= 18:`**: Essa é a *condição*. O programa verifica se a idade é maior ou igual a 18.
2. **`print("Você é maior de idade.")`**: Se a condição for verdadeira, o programa executa essa linha de código.
3. **`else:`**: Isso significa "senão". Se a condição não for verdadeira, o programa executa o código abaixo.
4. **`print("Você é menor de idade.")`**: Se a condição não for verdadeira, o programa executa essa linha de código.

Vamos ver outro exemplo:

```python
tempo = "chuvoso"

if tempo == "ensolarado":
    print("Vamos à praia!")
else:
    print("Vamos ao cinema.")
```

Neste exemplo, o programa verifica se a variável `tempo` é igual a "ensolarado". Se for verdadeiro, ele imprime "Vamos à praia!" Se não for verdadeiro, ele imprime "Vamos ao cinema."

Note como desvios condicionais são como caminhos que o programa pode seguir dependendo das condições que você define.