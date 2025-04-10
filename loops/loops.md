## Loops


Um loop repete um bloco de código várias vezes.

Existem dois tipos principais de loops em Python: `for` e `while`. Vamos começar com o loop `for`.

### Loop `for`

O loop `for` é usado quando você sabe exatamente quantas vezes quer repetir algo. Ele é como uma lista de tarefas que você precisa fazer uma após a outra.

Vamos ver um exemplo simples:

```python
for i in range(5):
    print("Olá, mundo!")
```

Neste exemplo, o loop `for` repete o bloco de código 5 vezes. A variável `i` assume os valores 0, 1, 2, 3 e 4, e a mensagem "Olá, mundo!" é impressa em cada iteração.

### Loop `while`

O loop `while` é usado quando você quer repetir algo até que uma condição seja falsa. Ele é como uma tarefa que você continua fazendo enquanto uma certa condição for verdadeira.

Vamos ver um exemplo:

```python
contador = 0

while contador < 5:
    print("Olá, mundo!")
    contador += 1
```

Neste exemplo, o loop `while` repete o bloco de código enquanto a variável `contador` for menor que 5. A cada iteração, a mensagem "Olá, mundo!" é impressa e o valor de `contador` é incrementado em 1. Quando `contador` chega a 5, a condição se torna falsa e o loop para.

### Exemplo Prático: Contando de 1 a 10

Vamos ver como podemos usar um loop `for` para contar de 1 a 10:

```python
for i in range(1, 11):
    print(i)
```

Neste exemplo, o loop `for` começa em 1 e vai até 10. A variável `i` assume os valores 1, 2, 3, ..., 10, e cada valor é impresso.

### Exemplo Prático: Pedindo Senha

Vamos ver como podemos usar um loop `while` para pedir uma senha até que a senha correta seja digitada:

```python
senha_correta = "1234"
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso permitido.")
    else:
        print("Senha incorreta. Tente novamente.")
```

Neste exemplo, o loop `while` continua pedindo a senha até que a senha correta seja digitada. Se a senha digitada for correta, a mensagem "Senha correta! Acesso permitido." é impressa e o loop para. Se a senha for incorreta, a mensagem "Senha incorreta. Tente novamente." é impressa e o loop continua.

