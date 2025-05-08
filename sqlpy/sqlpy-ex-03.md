# Lista de Tarefas: Consultar Múltiplos Valores no SQLite com Python

## Objetivo
Consultar múltiplos registros da tabela `usuarios` usando uma lista de emails como chave.

### Passo 1: Conectar ao banco de dados
1. Importe o módulo `sqlite3` no seu script Python.
2. Use a função `sqlite3.connect()` para abrir o arquivo de banco de dados existente (`meu_banco.db`).

### Passo 2: Criar um cursor
1. Crie um cursor usando o método `.cursor()` do objeto de conexão.

### Passo 3: Escrever e executar a consulta
1. Escreva um comando SQL para selecionar todos os campos de registros da tabela `usuarios` onde o `email` esteja em uma lista de valores.
   **Exemplo de comando SQL:**
   ```sql
   SELECT * FROM usuarios WHERE email IN (?, ?, ?)
   ```
2. Use o método `.execute()` do cursor para executar o comando SQL, passando a lista de emails como parâmetros.

### Passo 4: Obter e exibir os resultados
1. Use o método `.fetchall()` do cursor para obter todos os registros correspondentes.
2. Verifique se a lista de resultados não está vazia antes de exibi-los.
3. Exiba os registros no console.

### Passo 5: Fechar a conexão
1. Após concluir a consulta, feche o cursor e a conexão com o banco de dados usando os métodos `.close()`.

### Exemplo de Código
```python
import sqlite3

# Passo 1: Conectar ao banco de dados
conexao = sqlite3.connect('meu_banco.db')

# Passo 2: Criar um cursor
cursor = conexao.cursor()

# Passo 3: Escrever e executar a consulta
emails = ['alice@example.com', 'bob@example.com', 'carol@example.com']
placeholders = ', '.join(['?'] * len(emails))  # Gera "?, ?, ?"
query = f'SELECT * FROM usuarios WHERE email IN ({placeholders})'
cursor.execute(query, emails)

# Passo 4: Obter e exibir os resultados
registros = cursor.fetchall()
if registros:
    print('Registros encontrados:')
    for registro in registros:
        print(registro)
else:
    print('Nenhum registro encontrado para os emails fornecidos.')

# Passo 5: Fechar a conexão
cursor.close()
conexao.close()
```
