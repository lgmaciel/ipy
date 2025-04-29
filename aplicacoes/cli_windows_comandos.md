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
    ```

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

- **`attrib`**  
    Exibe ou altera atributos de arquivos.  
    **Exemplo:**  
    ```cmd
    attrib +r arquivo1.txt
    attrib +h arquivo2.txt
    attrib -r arquivo1.txt
    ```
    Os dois primeiros exemplos acima definem os atributo de:
    - "somente leitura" para o arquivo `arquivo1.txt`. Agora esse arquivo não pode ser modificado (inclusive, não pode ser apagado).
    - "escondido" para o arquivo `arquivo2.txt`. Agora esse arquivo não aparecerá na listagem de diretório.
    
    O terceiro exemplo *remove* o atributo `r` do arquivo `arquivo1.txt`. Agora o arquivo volta a poder ser modificado (inclusive, apagado).



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

