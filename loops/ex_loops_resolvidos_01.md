# Exercícios de Programação com Loops `for` em Python

Estes são 10 exercícios de programação utilizando loops `for` em Python. Os exercícios são apresentados em ordem de dificuldade crescente e incluem explicações introdutórias para novos conceitos.

---

## Exercício 1: Contagem Simples
Escreva um programa que imprima os números de 1 a 10. Este exercício introduz o conceito básico de um loop `for` para contagem.

```python
for i in range(1, 11):
    print(i)
```

---

## Exercício 2: Contagem com Passo Maior que 1
Modifique o programa anterior para imprimir apenas os números ímpares de 1 a 10. Aqui, você aprenderá a usar o parâmetro de passo no `range`.

```python
for i in range(1, 11, 2):
    print(i)
```

---

## Exercício 3: Iteração sobre uma Lista
Crie uma lista com os nomes de cinco frutas e use um loop `for` para imprimir cada nome. Este exercício introduz a iteração sobre listas.

```python
frutas = ["maçã", "banana", "laranja", "uva", "manga"]
for fruta in frutas:
    print(fruta)
```

---

## Exercício 4: Soma de Números
Escreva um programa que calcule a soma dos números de 1 a 100. Aqui, você aprenderá a usar uma variável acumuladora.

```python
soma = 0
for i in range(1, 101):
    soma += i
print("A soma é:", soma)
```

---

## Exercício 5: Contagem Regressiva
Implemente um programa que imprima uma contagem regressiva de 10 a 1. Este exercício reforça o uso do `range` com valores decrescentes.

```python
for i in range(10, 0, -1):
    print(i)
```

---

## Exercício 6: Multiplicação de Elementos de uma Lista
Dada uma lista de números `[2, 4, 6, 8]`, escreva um programa que imprima o dobro de cada número. Este exercício combina iteração sobre listas e operações matemáticas.

```python
numeros = [2, 4, 6, 8]
for numero in numeros:
    print(numero * 2)
```

---

## Exercício 7: Contagem de Caracteres em Strings
Peça ao usuário para digitar uma palavra e use um loop `for` para contar quantas letras "a" existem na palavra. Este exercício introduz a iteração sobre strings.

```python
palavra = input("Digite uma palavra: ")
contador = 0
for letra in palavra:
    if letra == "a":
        contador += 1
print("A palavra contém", contador, "letras 'a'.")
```

---

## Exercício 8: Tabuada
Escreva um programa que imprima a tabuada de multiplicação do número 5 (de 1 a 10). Este exercício reforça o uso de loops para cálculos repetitivos.

```python
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
```

---

## Exercício 9: Soma de Elementos de uma Lista
Dada uma lista de números `[1, 2, 3, 4, 5]`, escreva um programa que calcule a soma de todos os elementos. Este exercício reforça o uso de variáveis acumuladoras.

```python
numeros = [1, 2, 3, 4, 5]
soma = 0
for numero in numeros:
    soma += numero
print("A soma dos números é:", soma)
```

---