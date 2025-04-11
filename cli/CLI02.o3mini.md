# Tutorial: Usando o GIT na Linha de Comando

Agora que você já sabe usar a linha de comando e executar programas em Python, vamos aprender a usar o GIT. O GIT é uma ferramenta que os programadores usam para guardar versões do código e colaborar em projetos. Aqui, vamos ver alguns comandos básicos do GIT.

---

## 1. Inicializando um Repositório

Um "repositório" é onde o GIT guarda o seu código e o histórico de alterações. Para criar um repositório em uma pasta:

1. Entre na pasta do seu projeto:
   ```bash
   cd caminho/para/seu_projeto
   ```
2. Inicialize o repositório com o comando:
   ```bash
   git init
   ```
   Esse comando vai criar uma pasta escondida chamada ".git" que guarda todas as informações do projeto.

---

## 2. Configurando o Usuário (Local)

Para identificar quem está fazendo as alterações, o GIT grava um nome e um e-mail em cada commit. Aqui vamos configurar esses dados de forma local, ou seja, somente para este repositório:

1. Configure o nome:
   ```bash
   git config --local user.name "Seu Nome"
   ```
2. Configure o e-mail:
   ```bash
   git config --local user.email "seuemail@exemplo.com"
   ```
   
Verifique a configuração usando:
   ```bash
   git config user.name
   git config user.email
   ```

---

## 3. Fazendo um Commit

Um "commit" é como salvar uma versão do seu código. Para fazer um commit, siga estes passos:

1. Adicione os arquivos que você modificou à "área de preparação" (staging area). Por exemplo, para adicionar todos os arquivos:
   ```bash
   git add .
   ```
2. Faça o commit com uma mensagem que explique a alteração:
   ```bash
   git commit -m "Mensagem explicando a alteração"
   ```
   Exemplo:
   ```bash
   git commit -m "Adiciona o programa Python que imprime Olá, mundo!"
   ```

---

## 4. Consultando o Status do Repositório

Para saber quais arquivos foram modificados ou estão prontos para commit, use:
   ```bash
   git status
   ```
Esse comando mostra quais mudanças estão sendo rastreadas e quais ainda não foram adicionadas ao commit.

---

## 5. Enviando (Push) para um Repositório Remoto

Geralmente, os programadores guardam o código em um repositório online (por exemplo, no GitHub ou GitLab) para trabalhar com outras pessoas. Para enviar os seus commits para esse repositório remoto, siga estes passos:

1. Se ainda não adicionou o repositório remoto, faça isso com:
   ```bash
   git remote add origin https://seu-repositorio-url.git
   ```
2. Envie (push) as suas alterações para o repositório remoto:
   ```bash
   git push origin main
   ```
   Dica: Se sua ramificação (branch) principal tiver um nome diferente, use o nome dela (por exemplo, "master" ou outro).

---

## 6. Baixando (Pull) Alterações do Repositório Remoto

Caso outra pessoa tenha feito alterações e você precise atualizar o seu projeto com as novas mudanças, use:
   ```bash
   git pull origin main
   ```
   Esse comando baixa as alterações do repositório remoto e atualiza o seu projeto local.

---

## 7. Resumo dos Comandos

Aqui está uma lista rápida dos comandos que aprendemos:

- Inicializar repositório:
  ```bash
  git init
  ```
- Configurar o usuário (local):
  ```bash
  git config --local user.name "Seu Nome"
  git config --local user.email "seuemail@exemplo.com"
  ```
- Adicionar arquivos para commit:
  ```bash
  git add .
  ```
- Fazer o commit:
  ```bash
  git commit -m "Sua mensagem de commit"
  ```
- Consultar status:
  ```bash
  git status
  ```
- Adicionar repositório remoto:
  ```bash
  git remote add origin https://seu-repositorio-url.git
  ```
- Enviar alterações para o remoto:
  ```bash
  git push origin main
  ```
- Baixar alterações do remoto:
  ```bash
  git pull origin main
  ```

---

## 8. Dicas Finais

- Sempre escreva mensagens claras no commit para lembrar do que se tratavam as alterações.
- Use o comando `git status` frequentemente para saber o que está acontecendo com seu repositório.
- Se tiver dúvidas ou problemas, peça ajuda a um colega ou professor.

Parabéns por concluir o tutorial! Agora você já aprendeu o básico para usar o GIT pela linha de comando e pode guardar e compartilhar seus códigos. Continue praticando e explorando mais sobre essas ferramentas. Bom trabalho e bons estudos!