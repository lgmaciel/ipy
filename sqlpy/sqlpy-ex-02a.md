# Lista de Tarefas: Consultar Valores no SQLite com Python

## Objetivo
Consultar um registro específico da tabela `usuarios` usando o campo `email` como chave.

### Passo 1: Conectar ao banco de dados
1. Importe o módulo `sqlite3` no seu script Python.
2. Use a função `sqlite3.connect()` para abrir o arquivo de banco de dados existente (`meu_banco.db`).

### Passo 2: Criar um cursor
1. Crie um cursor usando o método `.cursor()` do objeto de conexão.

### Passo 3: Escrever e executar a consulta
1. Escreva um comando SQL para selecionar todos os campos de um registro da tabela `usuarios` onde o `email` seja igual a um valor específico.
   **Exemplo de comando SQL:**
   ```sql
   SELECT * FROM usuarios WHERE email = ?
   ```
2. Use o método `.execute()` do cursor para executar o comando SQL, passando o valor do email como parâmetro.

### Passo 4: Obter e exibir o resultado
1. Use o método `.fetchone()` do cursor para obter o registro correspondente.
2. Verifique se o resultado não é `None` antes de exibi-lo.
3. Exiba o registro no console.

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
email = 'alice@example.com'
cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))

# Passo 4: Obter e exibir o resultado
registro = cursor.fetchone()
if registro:
    print('Registro encontrado:', registro)
else:
    print('Nenhum registro encontrado com o email:', email)

# Passo 5: Fechar a conexão
cursor.close()
conexao.close()
```
