## Arquivos BATCH no Windows

Arquivos BATCH são scripts de texto simples usados no Windows para automatizar tarefas repetitivas. Eles contêm uma sequência de comandos que são executados em ordem pelo Prompt de Comando (CMD). Esses arquivos têm a extensão `.bat` ou `.cmd` e são amplamente utilizados para tarefas como manipulação de arquivos, configuração de ambiente e execução de programas.

### Exemplos de Arquivos BATCH

1. **Criar uma árvore de diretórios para um projeto simples em Python:**

```batch
@echo off
cd C:\
mkdir MeuProjeto
cd MeuProjeto
mkdir src
mkdir tests
echo print("Hello, World!") > src\main.py
echo Projeto criado com sucesso!
```

2. **Escrever uma frase no terminal usando parâmetros recebidos em linha de comando:**

```batch
@echo off
echo Olá, %1! Bem-vindo ao mundo dos arquivos BATCH.
```

*Como executar:*  
Salve o arquivo como `exemplo2.bat` e execute no CMD:  
```
exemplo2.bat João
```

3. **Criar uma árvore de diretórios cuja raiz é fornecida por linha de comando:**

```batch
@echo off
if "%1"=="" (
    echo Por favor, forneça o nome do diretório raiz.
    exit /b
)
mkdir %1
cd %1
mkdir src
mkdir docs
mkdir bin
echo Estrutura de diretórios criada em %1.
```

*Como executar:*  
Salve o arquivo como `exemplo3.bat` e execute no CMD:  
```
exemplo3.bat MeuProjeto
```