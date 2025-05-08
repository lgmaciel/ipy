# Roteiro de Atividades: Consultas em SQLite3 com Python

## Objetivo
Realizar consultas em um banco de dados SQLite3 usando Python e extrair os valores coluna a coluna dos resultados retornados por `fetchone()` e `fetchall()`.

---

## Realizar uma Consulta com `fetchone()`
1. Execute uma consulta SQL para buscar um único registro:
   ```python
   cursor.execute("SELECT * FROM usuarios WHERE id = 1")
   resultado = cursor.fetchone()
   print("Resultado com fetchone():", resultado)
   ```

2. Extraia os valores coluna a coluna:
   ```python
   if resultado:
       id, nome, email = resultado
       print(f"ID: {id}, Nome: {nome}, email: {email}")
   ```

---

## Realizar uma Consulta com `fetchall()`
1. Execute uma consulta SQL para buscar todos os registros:
   ```python
   cursor.execute("SELECT * FROM usuarios")
   resultados = cursor.fetchall()
   print("Resultados com fetchall():", resultados)
   ```

2. Itere pelos resultados e extraia os valores coluna a coluna:
   ```python
   for linha in resultados:
       id, nome, email = linha
       print(f"ID: {id}, Nome: {nome}, email: {email}")
   ```

---

## Passo 5: Fechar a Conexão
1. Sempre feche a conexão ao final do script:
   ```python
   conexao.close()
   ```

---

## Atividade Prática
1. Modifique o código para buscar usuários com um email específico.
2. Adicione novos registros ao banco de dados e teste as consultas.
3. Experimente usar `fetchmany()` para limitar o número de registros retornados.

