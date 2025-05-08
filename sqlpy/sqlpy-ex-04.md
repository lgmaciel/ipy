# Atualizando Dados em uma Tabela com Python e SQLite3

Este roteiro ensina como atualizar dados em uma tabela de um banco de dados SQLite usando Python.

## Passos

1. **Importe o módulo sqlite3**  
   O módulo `sqlite3` é usado para interagir com bancos de dados SQLite.

2. **Conecte-se ao banco de dados**  
   Use `sqlite3.connect()` para criar ou abrir um banco de dados existente.

3. **Crie um cursor**  
   O cursor permite executar comandos SQL.

4. **Escreva a consulta de atualização**  
   Use o comando SQL `UPDATE` para modificar os dados.

5. **Execute a consulta**  
   Utilize o método `execute()` do cursor para executar a consulta.

6. **Confirme as alterações**  
   Use `commit()` para salvar as alterações no banco de dados.

7. **Feche a conexão**  
   Sempre feche a conexão com o banco de dados após terminar.

## Exemplo de Código

```python
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Criando um cursor
cursor = conn.cursor()

# Consulta SQL para atualizar dados
sql_update_query = """
UPDATE tabela_exemplo
SET coluna1 = ?
WHERE coluna2 = ?;
"""

# Dados para atualização
dados = ('novo_valor', 'condicao')

# Executando a consulta
cursor.execute(sql_update_query, dados)

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()
```

## Explicação do Código

- **`UPDATE tabela_exemplo`**: Especifica a tabela onde os dados serão atualizados.
- **`SET coluna1 = ?`**: Define a nova informação para a coluna.
- **`WHERE coluna2 = ?`**: Condição para selecionar as linhas a serem atualizadas.
- **`cursor.execute(sql_update_query, dados)`**: Substitui os `?` pelos valores em `dados`.

## Dicas

- Sempre use placeholders (`?`) para evitar ataques de SQL Injection.
- Teste a consulta SQL diretamente no banco de dados antes de implementá-la no código.
- Certifique-se de que a condição no `WHERE` é específica para evitar atualizar várias linhas acidentalmente.
