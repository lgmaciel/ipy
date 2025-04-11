# Usando o Git na Linha de Comando

Nesta última parte do tutorial, vamos aprender a usar o Git, um sistema de controle de versão, na linha de comando.

## Inicializando um Repositório Git

Primeiro, vamos criar um novo repositório Git para o nosso projeto. Na linha de comando, navegue até a pasta onde você deseja criar o repositório e digite:

```
git init
```

Isso irá criar um novo repositório Git na sua pasta atual.

## Configurando seu Nome e E-mail

O Git precisa saber quem você é. Configure seu nome e e-mail com os seguintes comandos:

```
git config --local user.name "Seu Nome"
git config --local user.email "seu_email@exemplo.com"
```

Observe que usamos a opção `--local` para definir essas configurações apenas para este repositório.

## Adicionando Arquivos ao Repositório

Vamos adicionar o arquivo "meu_programa.py" que criamos anteriormente ao repositório. Digite:

```
git add meu_programa.py
```

Isso adiciona o arquivo à área de "staged" (preparado) para o próximo commit.

## Fazendo um Commit

Agora, vamos criar um commit (uma "versão") do nosso arquivo:

```
git commit -m "Meu primeiro programa Python"
```

O parâmetro `-m` permite que você adicione uma mensagem descritiva para o commit.

## Enviando para um Repositório Remoto

Finalmente, vamos enviar nosso repositório local para um repositório remoto (como o GitHub). Primeiro, crie um novo repositório remoto e obtenha a URL. Em seguida, na linha de comando, digite:

```
git remote add origin https://github.com/seu_usuario/seu_repositorio.git
git push -u origin master
```

Isso adiciona o repositório remoto e envia seu commit inicial para o servidor.

Parabéns! Você acabou de aprender os principais comandos do Git na linha de comando. Agora você pode usar o Git para gerenciar e compartilhar seus projetos de programação Python.

Lembre-se de praticar esses comandos regularmente para se familiarizar com a linha de comando e o Git. Boa sorte em seus estudos de programação!