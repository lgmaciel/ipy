## CMD - Windows

O CMD do Windows pode ser uma ferramenta poderosa para programadores, permitindo automação, gerenciamento de arquivos e execução de scripts. Alguns dos principais usos são:

1. **Automação com Scripts Batch**  
    - Criação e execução de scripts `.bat` para automatizar tarefas repetitivas.  
    - Exemplo:  
      ```cmd
      @echo off
      echo Automação em andamento...
      mkdir Projeto
      cd Projeto
      echo Arquivo criado > arquivo.txt
      ```

2. **Controle de Versionamento**  
    - Uso de ferramentas como o Git diretamente no CMD para controle de versão.  
    - Exemplo:  
      ```cmd
      git clone https://github.com/usuario/repositorio.git
      git status
      git commit -m "Mensagem de commit"
      ```

3. **Execução de Compiladores e Interpretadores**  
    - Compilação de código ou execução de scripts em linguagens como C, Python, Java, etc.  
    - Exemplo:  
      ```cmd
      python script.py
      javac Programa.java
      java Programa
      ```

4. **Gerenciamento de Pacotes**  
    - Uso de gerenciadores de pacotes como Chocolatey ou Winget para instalar ferramentas e dependências.  
    - Exemplo:  
      ```cmd
      choco install nodejs
      winget install Microsoft.VisualStudioCode
      ```

5. **Configuração de Variáveis de Ambiente**  
    - Configuração de variáveis de ambiente para projetos e ferramentas.  
    - Exemplo:  
      ```cmd
      set PATH=%PATH%;C:\Ferramentas
      ```

6. **Testes de Rede e Depuração**  
    - Uso de comandos como `ping`, `tracert` e `netstat` para verificar conectividade e depurar problemas de rede.  
    - Exemplo:  
      ```cmd
      ping localhost
      netstat -an
      ```

7. **Gerenciamento de Processos**  
    - Listar, iniciar ou finalizar processos diretamente pelo CMD.  
    - Exemplo:  
      ```cmd
      tasklist
      taskkill /IM notepad.exe /F
      ```

8. **Acesso a Ferramentas de Desenvolvimento**  
    - Execução de ferramentas como Node.js, npm, Angular CLI, etc.  
    - Exemplo:  
      ```cmd
      node -v
      npm install
      ng serve
      ```

9. **Criação e Gerenciamento de Arquivos e Diretórios**  
    - Manipulação de arquivos e diretórios para organização de projetos.  
    - Exemplo:  
      ```cmd
      mkdir Projeto
      cd Projeto
      echo Código > main.py
      ```

10. **Execução de Testes Automatizados**  
     - Rodar testes automatizados para projetos diretamente no terminal.  
     - Exemplo:  
        ```cmd
        pytest
        npm test
        ```

Esses usos tornam o CMD uma ferramenta essencial para programadores que trabalham no ambiente Windows.

### Árvore de Diretórios

Todos os arquivos de um computador estão armazenados em um banco de dados estruturado em árvore.

Uma **árvore de diretórios** é uma estrutura hierárquica usada para organizar e armazenar arquivos e pastas em um sistema de arquivos. Essa estrutura é chamada de "árvore" porque se assemelha a uma árvore invertida, onde:

- O **"tronco"** ou raiz é o diretório principal, chamado de **diretório raiz** (geralmente representado como `/` em sistemas Unix/Linux ou como uma unidade, como `C:\`, no Windows).
- Os **"galhos"** são os subdiretórios (pastas) que podem conter outros subdiretórios ou arquivos.
- As **"folhas"** são cada um dos arquivos que não possuem subdiretórios abaixo deles.


### Exemplo de uma árvore de diretórios:
```
/
├── home
│   ├── joao
│   │   ├── documentos
│   │   │   └── arquivo.txt
│   │   └── imagens
│   └── maria
├── var
└── etc
```

### Características principais:

1. **Hierarquia**: Cada diretório pode conter outros diretórios (subdiretórios) ou arquivos, formando uma relação de "pai e filho".
2. **Caminho Absoluto**: Cada arquivo ou pasta pode ser identificado por um caminho completo que começa na raiz e segue pelos subdiretórios até o destino.
   - Exemplo no Windows: `C:\Users\Joao\Documentos\arquivo.txt`
   - Exemplo no Linux: `/home/joao/documentos/arquivo.txt`
3. **Organização**: Essa estrutura facilita a organização lógica dos dados, permitindo que arquivos relacionados sejam agrupados em pastas específicas.

Essa estrutura é amplamente usada porque é intuitiva e escalável, permitindo que sistemas operacionais e usuários gerenciem grandes volumes de dados de forma eficiente.


### Como Abrir o CMD no Windows

1. Pressione as teclas `Win + R` para abrir a janela "Executar".
2. Digite `cmd` e pressione `Enter`.
3. O Prompt de Comando será aberto.


### Comandos Mais Usados no CMD

- **`dir`**  
    Lista os arquivos e diretórios no diretório atual.  
    **Exemplo:**  
    ```cmd
    dir
    ```

- **`cls`**  
    Limpa a tela do terminal.  
    **Exemplo:**  
    ```cmd
    cls
    ``

- **`cd`**  
    Navega entre diretórios. Use `cd ..` para voltar ao diretório anterior.  
    **Exemplo:**  
    ```cmd
    cd C:\Users
    ```

- **`mkdir`**  
    Cria um novo diretório.  
    **Exemplo:**  
    ```cmd
    mkdir NovoDiretorio
    ```

- **`rmdir`**  
    Remove um diretório vazio.  
    **Exemplo:**  
    ```cmd
    rmdir NovoDiretorio
    ```

- **`del`**  
    Exclui arquivos.  
    **Exemplo:**  
    ```cmd
    del arquivo.txt
    ```

- **`copy`**  
    Copia arquivos de um local para outro.  
    **Exemplo:**  
    ```cmd
    copy arquivo.txt C:\Backup
    ```

- **`move`**  
    Move arquivos de um local para outro.  
    **Exemplo:**  
    ```cmd
    move arquivo.txt C:\Documentos
    ```

- **`ipconfig`**  
    Exibe informações de configuração de rede.  
    **Exemplo:**  
    ```cmd
    ipconfig
    ```

- **`ping`**  
    Verifica a conectividade com outro dispositivo na rede.  
    **Exemplo:**  
    ```cmd
    ping google.com
    ```

- **`exit`**  
    Fecha o Prompt de Comando.  
    **Exemplo:**  
    ```cmd
    exit
    ```

