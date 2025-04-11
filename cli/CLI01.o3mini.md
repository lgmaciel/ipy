# Tutorial: Executando Arquivos Python Pela Linha de Comando

Olá, pessoal! Agora que já aprendemos a usar a linha de comando, vamos aprender como executar um programa Python. Isso significa que vamos fazer o computador rodar um arquivo criado em Python, usando o terminal.

---

## 1. O Que é o Python?

O Python é uma linguagem de programação. Ele é usado para criar programas e resolver problemas. Hoje, nós vamos aprender como fazer o computador ler e executar um arquivo feito em Python.

---

## 2. Configurando o Python no Computador

Antes de executar um programa Python, você precisa ter o Python instalado. Para verificar se você já tem o Python instalado, siga estes passos:

1. Abra o terminal.
2. Digite o seguinte comando e pressione Enter:
   ```bash
   python --version
   ```
   ou, se esse comando não funcionar, tente:
   ```bash
   python3 --version
   ```
3. Se você vir uma mensagem como "Python 3.X.X", significa que o Python está instalado. Se não aparecer nada ou mostrar um erro, você precisa instalar o Python. Peça ajuda a um adulto ou professor para instalar.

---

## 3. Criando um Arquivo Python

Vamos criar um arquivo simples de Python no nosso diretório.

1. Primeiro, crie uma pasta para seu projeto se ainda não tiver uma:
   ```bash
   mkdir meu_projeto_python
   ```
2. Entre na pasta:
   ```bash
   cd meu_projeto_python
   ```
3. Crie um arquivo chamado "meu_programa.py" usando o comando `touch`:
   ```bash
   touch meu_programa.py
   ```

---

## 4. Escrevendo um Programa Simples em Python

Agora que temos um arquivo, precisamos colocar um conteúdo nele. Você pode usar um editor de texto simples, como o Notepad, ou usar o editor no terminal, como o nano.

### Usando o Nano (Editor Simples do Terminal):

1. Abra o arquivo com o nano:
   ```bash
   nano meu_programa.py
   ```
2. Escreva o seguinte código simples:
   ```python
   # Este é um comentário: ele explica o que o código faz
   print("Olá, mundo!")  # Isto mostrará "Olá, mundo!" na tela.
   ```
3. Para salvar e sair:
   - Pressione Ctrl + O para salvar.
   - Pressione Enter para confirmar o nome do arquivo.
   - Pressione Ctrl + X para sair do nano.

---

## 5. Executando o Programa Python

Agora que você criou e salvou seu programa, vamos executá-lo com Python.

1. Certifique-se de estar na mesma pasta onde o arquivo está. Se não estiver, use o comando `cd` para entrar nessa pasta.
2. Para executar, digite:
   ```bash
   python meu_programa.py
   ```
   ou, se o seu sistema usa o comando python3:
   ```bash
   python3 meu_programa.py
   ```
3. Você verá a seguinte mensagem na tela:
   ```
   Olá, mundo!
   ```

Parabéns! Seu programa Python foi executado com sucesso.

---

## 6. O Que Aconteceu?

- Quando você digitou o comando para executar o programa, o Python abriu o arquivo "meu_programa.py".
- O Python leu o código escrito no arquivo.
- O comando `print("Olá, mundo!")` diz ao Python que ele deve mostrar a mensagem "Olá, mundo!" na tela.

---

## 7. Experimentando Um Pouco Mais

Agora que você sabe executar um programa Python, tente alterar o seu código! Por exemplo, abra o "meu_programa.py" novamente e mude a mensagem:
  
1. Abra o arquivo:
   ```bash
   nano meu_programa.py
   ```
2. Altere a linha para:
   ```python
   print("Aprendendo Python é muito divertido!")
   ```
3. Salve e saia do editor (Ctrl + O, Enter, Ctrl + X).
4. Execute novamente o programa:
   ```bash
   python meu_programa.py
   ```
5. Veja a nova mensagem na tela.

---

## 8. Dicas Finais

- Sempre verifique se o Python está instalado.
- Use um editor de texto de sua preferência para editar seus arquivos Python.
- Quando houver erros, leia as mensagens do terminal com atenção, elas podem ajudar você a entender o problema.

Essa parte do tutorial mostrou como criar e executar um programa Python pela linha de comando. No próximo passo, aprenderemos sobre o uso do GIT para ajudar vocês a controlar as versões dos seus códigos.

Bom trabalho e continue praticando!