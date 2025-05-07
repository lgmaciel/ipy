# Lista de Tarefas: Operações Básicas com SQLite e Python

## Objetivo
Criar um banco de dados SQLite, uma tabela com os campos `id`, `nome`, `email` e inserir 10 registros na tabela.

### Passo 1: Criar um banco de dados SQLite
1. Importe o módulo `sqlite3` no seu script Python.
2. Use a função `sqlite3.connect()` para criar ou abrir um arquivo de banco de dados chamado `meu_banco.db`.

### Passo 2: Criar uma tabela no banco de dados
1. Crie um cursor usando o método `.cursor()` do objeto de conexão.
2. Escreva um comando SQL para criar uma tabela chamada `usuarios` com os seguintes campos:
   - `id` (inteiro, chave primária, autoincremento),
   - `nome` (texto, não nulo),
   - `email` (texto, único).
   
   **Exemplo de comando SQL com autoincremento:**
   ```sql
    [...]
       id INTEGER PRIMARY KEY AUTOINCREMENT,
    [...]
   
   ```

3. Execute o comando SQL usando o método `.execute()` do cursor.
4. Salve as alterações no banco de dados com o método `.commit()`.

### Passo 3: Inserir 10 registros na tabela
1. Crie uma lista de 10 tuplas, cada uma contendo valores para os campos `nome` e `email`.
2. Use o comando SQL `INSERT INTO` para inserir os valores na tabela.
3. Utilize o método `.executemany()` do cursor para inserir todos os registros de uma vez.
4. Salve as alterações no banco de dados com o método `.commit()`.

### Passo 4: Fechar a conexão
1. Após concluir as operações, feche o cursor e a conexão com o banco de dados usando os métodos `.close()`.

### Exemplo de Código
```python
import sqlite3

# Passo 1: Criar o banco de dados
conexao = sqlite3.connect('meu_banco.db')

# Passo 2: Criar a tabela
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')
conexao.commit()

# Passo 3: Inserir registros
dados = [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Carol', 'carol@example.com'),
    ('David', 'david@example.com'),
    ('Eve', 'eve@example.com'),
    ('Frank', 'frank@example.com'),
    ('Grace', 'grace@example.com'),
    ('Hank', 'hank@example.com'),
    ('Ivy', 'ivy@example.com'),
    ('Jack', 'jack@example.com')
]
cursor.executemany('INSERT INTO usuarios (nome, email) VALUES (?, ?)', dados)
conexao.commit()

# Passo 4: Fechar a conexão
cursor.close()
conexao.close()
```
