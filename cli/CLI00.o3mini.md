# Tutorial: Introdução à Linha de Comando com Bash

Olá, pessoal! Neste tutorial vamos aprender a usar a linha de comando no sistema operacional. A linha de comando é uma forma de conversar com o computador digitando comandos. Ela é muito usada por programadores para fazer várias tarefas. Vamos começar com o básico!

---

## 1. O que é a Linha de Comando?

A linha de comando, ou terminal, é uma tela onde você digita comandos para o computador, em vez de clicar com o mouse. É como enviar instruções diretas!

---

## 2. Como Abrir o Terminal

Dependendo do seu sistema operacional, você pode abrir o terminal de maneiras diferentes:

- **No Linux:** Procure por “Terminal” no menu de aplicações.
- **No macOS:** Abra o "Terminal" na pasta "Utilitários".
- **No Windows:** Você pode usar o "Git Bash" (se estiver instalado) ou o "Windows Terminal" configurado para usar um ambiente similar ao Bash.

---

## 3. Comandos Básicos do Bash

Aqui estão alguns comandos simples para você começar. Cada comando deve ser digitado e depois pressionar a tecla Enter. Preste atenção no que cada comando faz!

### a) pwd – Mostrar o Diretório Atual

- **O que faz:** Mostra em qual pasta (diretório) você está.
- **Como usar:**  
  ```bash
  pwd
  ```
  
### b) ls – Listar Arquivos e Pastas

- **O que faz:** Mostra os arquivos e pastas que estão na pasta atual.
- **Como usar:**  
  ```bash
  ls
  ```

*Dica:* Às vezes, usar `ls -l` (com o “-l” em minúsculo) mostra mais detalhes, como quem criou o arquivo e quando foi modificado.

### c) cd – Mudar de Diretorio

- **O que faz:** Permite trocar de pasta e navegar pelo sistema.
- **Como usar:**  
  ```bash
  cd nome_da_pasta
  ```
- **Exemplo:**  
  Se você quiser entrar na pasta "Documentos":
  ```bash
  cd Documentos
  ```
- **Para voltar:**  
  ```bash
  cd ..
  ```
  Esse comando volta para a pasta anterior.

### d) mkdir – Criar uma Nova Pasta

- **O que faz:** Cria uma nova pasta.
- **Como usar:**  
  ```bash
  mkdir nova_pasta
  ```
- **Exemplo:**  
  Para criar uma pasta chamada "meu_projeto":
  ```bash
  mkdir meu_projeto
  ```

### e) rmdir – Remover uma Pasta Vazia

- **O que faz:** Remove uma pasta vazia.
- **Como usar:**  
  ```bash
  rmdir nome_da_pasta
  ```
- **Atenção:** Se a pasta não estiver vazia, este comando não funcionará. Em casos assim, pode ser necessário outros comandos (mas vamos aprender isso depois!).

### f) touch – Criar um Novo Arquivo

- **O que faz:** Cria um arquivo vazio.
- **Como usar:**  
  ```bash
  touch arquivo.txt
  ```
- **Exemplo:**  
  Para criar um arquivo chamado "teste.txt":
  ```bash
  touch teste.txt
  ```

### g) cat – Ler o Conteúdo de um Arquivo

- **O que faz:** Mostra o que tem dentro de um arquivo.
- **Como usar:**  
  ```bash
  cat arquivo.txt
  ```
- **Exemplo:**  
  Caso você tenha criado "teste.txt", use:
  ```bash
  cat teste.txt
  ```

### h) cp – Copiar Arquivos ou Pastas

- **O que faz:** Copia um arquivo ou pasta para outro lugar.
- **Como usar (arquivo):**  
  ```bash
  cp arquivo.txt copia_arquivo.txt
  ```
- **Exemplo:**  
  Para copiar "teste.txt" para "teste_copia.txt":
  ```bash
  cp teste.txt teste_copia.txt
  ```

### i) mv – Mover ou Renomear Arquivos/Pastas

- **O que faz:** Move um arquivo ou pasta para outro lugar, ou renomeia.
- **Como usar (renomear arquivo):**  
  ```bash
  mv velho_nome.txt novo_nome.txt
  ```
- **Exemplo:**  
  Para mover "teste.txt" para uma pasta chamada "meu_projeto":
  ```bash
  mv teste.txt meu_projeto/
  ```

### j) rm – Remover Arquivos

- **O que faz:** Remove arquivos (cuidado, porque eles não vão para a lixeira).
- **Como usar:**  
  ```bash
  rm arquivo.txt
  ```
- **Atenção:** Use este comando com cuidado!

---

## 4. Praticando os Comandos

Vamos fazer um exercício simples usando os comandos aprendidos:

1. **Abra o terminal.**

2. **Crie uma pasta para o seu projeto.**
   ```bash
   mkdir meu_projeto
   ```

3. **Entre na pasta criada.**
   ```bash
   cd meu_projeto
   ```

4. **Crie um arquivo chamado "exemplo.txt".**
   ```bash
   touch exemplo.txt
   ```

5. **Verifique se o arquivo foi criado.**
   ```bash
   ls
   ```

6. **Mostre o conteúdo do arquivo (que está vazio).**
   ```bash
   cat exemplo.txt
   ```

7. **Volte para a pasta anterior.**
   ```bash
   cd ..
   ```

---

## 5. Dicas Finais

- Tente usar os comandos várias vezes para se acostumar.
- Se cometer algum erro, não se preocupe! Você pode fechar o terminal e reabrir.
- Sempre leia a mensagem que o terminal mostra; ela pode ajudar a entender o que aconteceu.

Parabéns por concluir a primeira parte do nosso tutorial! Agora você já sabe como usar o terminal para fazer várias tarefas que um programador precisa. Na próxima parte, vamos ver como executar programas Python diretamente da linha de comando.

Bom aprendizado e pratique bastante!