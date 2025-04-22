## Funções - Estudo de caso: Baby Shark

Considere o programa abaixo, que imprime na tela a letra da música do Baby Shark.

```python
bebeTubarao = """
Bebê tubarão, tchu tchu ru ru
Bebê tubarão, tchu tchu ru ru
Bebê tubarão, tchu tchu ru ru
Bebê tubarão!

Mamãe tubarão, tchu tchu ru ru
Mamãe tubarão, tchu tchu ru ru
Mamãe tubarão, tchu tchu ru ru
Mamãe tubarão!

Papai tubarão, tchu tchu ru ru
Papai tubarão, tchu tchu ru ru
Papai tubarão, tchu tchu ru ru
Papai tubarão!

Vovó tubarão, tchu tchu ru ru
Vovó tubarão, tchu tchu ru ru
Vovó tubarão, tchu tchu ru ru
Vovó tubarão!

Vovô tubarão, tchu tchu ru ru
Vovô tubarão, tchu tchu ru ru
Vovô tubarão, tchu tchu ru ru
Vovô tubarão!

Vou caçar, tchu tchu ru ru
Vou caçar, tchu tchu ru ru
Vou caçar, tchu tchu ru ru
Vou caçar!

Foge, foge, tchu tchu ru ru
Foge, foge, tchu tchu ru ru
Foge, foge, tchu tchu ru ru
Foge, foge!

São e salvos, tchu tchu ru ru
São e salvos, tchu tchu ru ru
São e salvos, tchu tchu ru ru
São e salvos!

É o fim, tchu tchu ru ru
É o fim, tchu tchu ru ru
É o fim, tchu tchu ru ru
É o fim!
"""

print(bebe_tubarao)
```

Podemos notar que há uma regra para formar cada estrofe.

1. dizemos qual é a frase que inicia cada sentença
2. acrescentamos `', tchu tchu ru ru'` ao final da frase e cantamos o resultado (a sentença) 3 vezes
3. a sentença final é a frase inicial acrescida de `'!'`

Esse é um `algoritmo` para formar uma estrofe do `Baby Shark`.

Vamos reescrever o programa usando esse algoritmo.

```python
# Função para criar uma estrofe do Baby Shark
def bebe_tubarao(frase):
    return (
        (frase + ', tchu tchu ru ru\n') * 3
        + frase + '!\n\n'
    )

# Criação das estrofes
estrofe1 = bebe_tubarao('Bebê tubarão')
estrofe2 = bebe_tubarao('Mamãe tubarão')
estrofe3 = bebe_tubarao('Papai tubarão')
estrofe4 = bebe_tubarao('Vovó tubarão')
estrofe5 = bebe_tubarao('Vovô tubarão')
estrofe6 = bebe_tubarao('Vou caçar')
estrofe7 = bebe_tubarao('Foge, foge')
estrofe8 = bebe_tubarao('Sãos e salvos')
estrofe9 = bebe_tubarao('É o fim')

# Exibindo todas as estrofes
print(estrofe1 + estrofe2 + estrofe3 + estrofe4 + estrofe5 + estrofe6 + estrofe7 + estrofe8)

```

## O que aconteceu aqui!?
Nesse programa usamos uma `Função` para **abstrair a operação** de criar uma estrofe do 'Baby Shark'.

```python
def bebe_tubarao(frase):
    return (
        (frase + ', tchu tchu ru ru\n') * 3
        + frase + '!\n\n'
    )
```

No código acima:

- Definimos a função usando a palavra `def` seguida do nome da função e parênteses
- entre os parênteses `()` declaramos uma variável que receberá o argumento da função (que será informado por quem chamar a função)
- Após os dois pontos'`:`' escrevemos o `corpo da função`, que é o código que será executado quando alguém `chamar a função`.
- `return` indica qual é o resultado da função, ou seja, o que ela retorna para quem a chamou

Depois, nós usamos a função.

Para usar uma função usamos seu nome seguido de parênteses e passamos os parâmetros necessários, caso existam.

No exemplo, chamamos a função 9 vezes. 

```python
estrofe1 = bebe_tubarao('Bebê tubarão')
estrofe2 = bebe_tubarao('Mamãe tubarão')
estrofe3 = bebe_tubarao('Papai tubarão')
# ...
```

A cada chamada de função:

- passamos como parâmetro uma frase inicial diferente, que caracteriza a estrofe
- a função pegou essa frase e usou ela para gerar a estrofe, segundo o padrão
- ao final dessa operação, a função retornou para nós a string com a estrofe "customizada"
- pegamos o retorno da função demos a ele um nome de variável(estrofe1, estrofe2...) e utilizamos essa variável no final do programa para imprimir na tela a estrofe (usando `print()`)

```python
print(estrofe1 + estrofe2 + estrofe3 + estrofe4 + estrofe5 + estrofe6 + estrofe7 + estrofe8)
```


## Composição de funções

Podemos reescrever o programa para simplificá-lo mais.

Note que só estamos usando as variáveis `estrofe1`, `estrofe2`... para passar o resultado da função `bebe_tubarao()` para a função `print()`.

Podemos fazer isso diretamente, sem usar as variáveis.

Aqui passamos o resultado de `bebe_tubarao()` diretamente para `print`. 

```python   
print(bebe_tubarao('Bebê tubarão'))
print(bebe_tubarao('Mamãe tubarão'))
print(bebe_tubarao('Papai tubarão'))
print(bebe_tubarao('Vovô tubarão'))
print(bebe_tubarao('Vovó tubarão'))
print(bebe_tubarao('Vou caçar'))
print(bebe_tubarao('Foge, foge'))
print(bebe_tubarao('Sãos e salvos'))
print(bebe_tubarao('É o fim'))
```

## Refatoração

Refatorar é `reorganizar os fatores de um programa`, ou seja, as partes que compõe o programa.

Refatorações acontecem quando mudamos de ideia sobre o modo como abstraímos alguma operação ou sobre como estamos chamando uma variável, função...

Durante uma refatoração escrevemos e reescrevemos código para adequar o programa à nova ideia.

Vamos pensar melhor no que a função `bebe_tubarao()` está fazendo. Na verdade, ela gera apenas uma estrofe da música `bebê tubarão` e não a letra inteira. Então, um melhor nome para ela seria `estrofe()` e não `bebe_tubarao()`.

Uma função `bebe_tubarao()` deveria gerar a letra inteira da música e não só uma das estrofes. Então vamos reescrever o programa para:

- mudar o nome da função `bebe_tubarao()` para `estrofe()`
- criar uma nova função `bebe_tubarao()` que gera a letra inteira da música

Refatorando o código ele poderia ficar assim:

```python
def bebe_tubarao(frase):
    return (
        (frase + ', tchu tchu ru ru\n') * 3
        + frase + '!\n\n'
    )
    
def bebe_tubarao():
    return (
    estrofe('Bebê tubarão')
    + estrofe('Mamãe tubarão')    
    + estrofe('Papai tubarão')
    + estrofe('Vovô tubarão')
    + estrofe('Vovó tubarão')
    + estrofe('Vou caçar')
    + estrofe('Foge, foge')
    + estrofe('Sãos e salvos')
    + estrofe('É o fim')
    )

letra_da_musica = bebe_tubarao()

print(letra_da_musica)

```

Nessa nova versão o código do programa representa melhor a forma abstrata como estamos concebendo a formação da letra do 'Bebê Tubarão'. 

Agora o programa está dizendo mais claramente que 'Bebê Tubarão' retorna a `letra_da_musica` e que ela é composta pela `estrofe('Bebê Tubarão')` + a `estrofe('Papai Tubarão')` + a `estrofe(...)...`
