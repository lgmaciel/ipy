
### Receber parâmetros pela linha de comando

Quando você executa um programa pela linha de comando, pode passar **parâmetros** ou **argumentos** para ele. Esses parâmetros são usados para fornecer informações adicionais ao programa, como configurações ou dados de entrada.

#### Exemplo em Python
Aqui está um exemplo simples de como receber parâmetros pela linha de comando em Python usando o módulo `sys`:

```python
import sys

# sys.argv é uma lista que contém os argumentos passados pela linha de comando
# O primeiro elemento (sys.argv[0]) é o nome do script
# Os demais elementos são os argumentos fornecidos

if len(sys.argv) > 1:
    print("Parâmetros recebidos:", sys.argv[1:])
else:
    print("Nenhum parâmetro foi passado.")
```

#### Como executar:
1. Salve o código acima em um arquivo chamado `main.py`.
2. No terminal, execute o script passando parâmetros:
   ```bash
   python main.py argumento1 argumento2
   ```
3. A saída será:
   ```
   Parâmetros recebidos: ['argumento1', 'argumento2']
   ```

#### Exemplo com `argparse`
Para programas mais complexos, o módulo `argparse` é recomendado, pois permite definir argumentos opcionais, tipos de dados e mensagens de ajuda:

```python


import argparse

# Configurando o parser
parser = argparse.ArgumentParser(description="Exemplo de leitura de parâmetros.")
parser.add_argument("nome", help="Seu nome")
parser.add_argument("--idade", type=int, help="Sua idade (opcional)")

# Lendo os argumentos
args = parser.parse_args()

print(f"Olá, {args.nome}!")
if args.idade:
    print(f"Você tem {args.idade} anos.")
```

#### Como executar:
1. Salve o código acima em `main.py`.
2. No terminal, execute:
   ```bash
   python main.py João --idade 25
   ```
3. A saída será:
   ```
   Olá, João!
   Você tem 25 anos.
   ```

Esses exemplos mostram como capturar e usar parâmetros fornecidos pela linha de comando para tornar seus scripts mais dinâmicos e flexíveis.