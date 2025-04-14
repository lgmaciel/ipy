## A Instrução `break` em Loops

A instrução `break` é usada em Python para interromper a execução de um loop antes que ele complete todas as iterações. Ela pode ser usada tanto em loops `for` quanto em loops `while`. Vamos explorar como utilizá-la com exemplos práticos.

### Usando `break` em Loops `for`

#### Exemplo 1: Interrompendo um loop ao encontrar um valor específico

```python
for numero in range(10):
    if numero == 5:
        print("Número 5 encontrado, interrompendo o loop.")
        break
    print(f"Número: {numero}")
```

Neste exemplo, o loop `for` é interrompido quando o número 5 é encontrado.

#### Exemplo 2: Interrompendo um loop ao encontrar uma condição

```python
nomes = ["Ana", "Bruno", "Carlos", "Diana"]
for nome in nomes:
    if nome == "Carlos":
        print("Carlos encontrado, interrompendo o loop.")
        break
    print(f"Nome: {nome}")
```

Aqui, o loop `for` é interrompido ao encontrar o nome "Carlos".

### Usando `break` em Loops `while`

#### Exemplo 1: Interrompendo um loop com base em uma condição

```python
contador = 0
while contador < 10:
    if contador == 7:
        print("Contador chegou a 7, interrompendo o loop.")
        break
    print(f"Contador: {contador}")
    contador += 1
```

Neste exemplo, o loop `while` é interrompido quando o contador atinge o valor 7.

#### Exemplo 2: Interrompendo um loop com entrada do usuário

```python
while True:
    comando = input("Digite 'sair' para interromper o loop: ")
    if comando == "sair":
        print("Comando 'sair' recebido, interrompendo o loop.")
        break
    print(f"Você digitou: {comando}")
```

Aqui, o loop `while` é interrompido quando o usuário digita "sair".
