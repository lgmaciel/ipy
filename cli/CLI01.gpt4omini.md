# Tutorial de Programação: Executando um Arquivo Python na Linha de Comando

## O que é Python?

Python é uma linguagem de programação muito popular e fácil de aprender. É usada para criar aplicativos, jogos, sites e muito mais. Neste tutorial, vamos aprender como executar um programa Python usando a linha de comando.

## Instalando o Python

Antes de executar um programa Python, você precisa ter o Python instalado no seu computador. Aqui estão as instruções para instalar o Python:

### No Windows

1. Acesse o site oficial do Python: [python.org](https://www.python.org/downloads/).
2. Baixe o instalador para Windows.
3. Execute o instalador e certifique-se de marcar a opção "Add Python to PATH" antes de clicar em "Install Now".

### No macOS

1. Acesse o site oficial do Python: [python.org](https://www.python.org/downloads/).
2. Baixe o instalador para macOS.
3. Execute o instalador e siga as instruções.

### No Linux

A maioria das distribuições Linux já vem com o Python instalado. Para verificar, abra o terminal e digite:

```bash
python3 --version
```

Se não estiver instalado, você pode instalar o Python usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu, você pode usar:

```bash
sudo apt-get install python3
```

## Criando um Arquivo Python

Agora que você tem o Python instalado, vamos criar um arquivo Python simples.

1. Abra a linha de comando.
2. Navegue até a pasta onde você deseja criar o arquivo (por exemplo, "meus_códigos").
3. Crie um novo arquivo chamado "hello.py" usando o comando:

```bash
touch hello.py
```

4. Abra o arquivo "hello.py" em um editor de texto (como Notepad no Windows, TextEdit no macOS ou qualquer editor de sua escolha) e escreva o seguinte código:

```python
print("Olá, mundo!")
```

5. Salve e feche o arquivo.

## Executando o Arquivo Python

Agora que você criou o arquivo Python, vamos executá-lo na linha de comando.

1. Certifique-se de que você está na pasta onde o arquivo "hello.py" está localizado. Use o comando `pwd` para verificar.
2. Para executar o arquivo, digite o seguinte comando:

```bash
python hello.py
```

ou, se você estiver usando Python 3, pode ser necessário usar:

```bash
python3 hello.py
```

3. Pressione `Enter`. Você deve ver a mensagem "Olá, mundo!" exibida na linha de comando.

## Praticando

Agora é sua vez de praticar:

1. Crie um novo arquivo chamado "soma.py".
2. Adicione o seguinte código ao arquivo:

```python
a = 5
b = 3
soma = a + b
print("A soma de", a, "e", b, "é", soma)
```

3. Salve o arquivo e execute-o na linha de comando usando o mesmo método que você usou para "hello.py".

## Conclusão

Você aprendeu como criar e executar um programa Python na linha de comando! Na próxima parte do tutorial, vamos explorar o uso do Git na linha de comando, uma ferramenta essencial para gerenciar projetos de programação. 

Pronto para continuar?