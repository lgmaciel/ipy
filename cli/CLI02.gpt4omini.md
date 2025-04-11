# Tutorial de Programação: Usando Git na Linha de Comando

## O que é Git?

Git é um sistema de controle de versão que permite que você acompanhe as mudanças em seus projetos de programação. Com o Git, você pode salvar diferentes versões do seu código, colaborar com outras pessoas e muito mais. Vamos aprender como usar o Git na linha de comando!

## Instalando o Git

Antes de começar, você precisa ter o Git instalado no seu computador. Aqui estão as instruções para instalar o Git:

### No Windows

1. Acesse o site oficial do Git: [git-scm.com](https://git-scm.com/downloads).
2. Baixe o instalador para Windows.
3. Execute o instalador e siga as instruções. Você pode deixar as opções padrão.

### No macOS

1. Abra o Terminal.
2. Digite o seguinte comando para instalar o Git via Homebrew (se você não tiver o Homebrew, você pode instalá-lo seguindo as instruções em [brew.sh](https://brew.sh/)):

```bash
brew install git
```

### No Linux

A maioria das distribuições Linux já vem com o Git instalado. Para verificar, abra o terminal e digite:

```bash
git --version
```

Se não estiver instalado, você pode instalar o Git usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu, você pode usar:

```bash
sudo apt-get install git
```

## Inicializando um Repositório Git

1. Abra a linha de comando e navegue até a pasta onde você deseja criar seu projeto (por exemplo, "meus_códigos").
2. Crie uma nova pasta para o seu projeto:

```bash
mkdir meu_projeto
cd meu_projeto
```

3. Inicialize um repositório Git:

```bash
git init
```

## Configurando seu Nome e Email

Para que o Git saiba quem está fazendo as alterações, você precisa configurar seu nome e email. Use os seguintes comandos, substituindo "Seu Nome" e "seuemail@example.com" pelas suas informações:

```bash
git config --local user.name "Seu Nome"
git config --local user.email "seuemail@example.com"
```

## Fazendo um Commit

1. Crie um arquivo chamado "README.md" e adicione uma descrição do seu projeto:

```bash
touch README.md
echo "Este é o meu projeto!" > README.md
```

2. Adicione o arquivo ao repositório:

```bash
git add README.md
```

3. Faça um commit para salvar suas alterações:

```bash
git commit -m "Adiciona o arquivo README.md"
```

## Consultando o Status do Repositório

Para ver o status do seu repositório e verificar quais arquivos foram modificados, use:

```bash
git status
```

## Trabalhando com Repositórios Remotos

### Fazendo Push para um Repositório Remoto

Se você tiver um repositório remoto (por exemplo, no GitHub), você pode enviar suas alterações para lá. Primeiro, adicione o repositório remoto:

```bash
git remote add origin https://github.com/seuusuario/meu_projeto.git
```

Em seguida, faça o push das suas alterações:

```bash
git push -u origin master
```

### Fazendo Pull de um Repositório Remoto

Se você quiser obter as últimas alterações de um repositório remoto, use o comando:

```bash
git pull origin master
```

## Praticando

Agora é sua vez de praticar:

1. Crie um novo arquivo chamado "script.py" e adicione algum código Python.
2. Adicione o arquivo ao repositório, faça um commit e, se tiver um repositório remoto, faça o push.

## Conclusão

Parabéns! Você aprendeu a usar a linha de comando, a executar programas Python e a usar o Git para gerenciar seus projetos. Essas habilidades são fundamentais para qualquer programador. Continue praticando e explorando mais sobre programação e controle de versão!

Se você tiver dúvidas ou quiser aprender mais, não hesite em perguntar. Boa sorte na sua jornada de programação!