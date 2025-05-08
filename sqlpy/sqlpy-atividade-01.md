# Roteiro de Atividades: Lista de Presenças em um Evento


## Atividade 1: Configuração Inicial
1. Crie um banco de dados SQLite para armazenar os dados.
2. Configure as tabelas necessárias:
   - **Eventos**: Armazena informações sobre os eventos.
   - **Convidados**: Armazena informações sobre os convidados.
   - **Presenças**: Relaciona convidados e eventos, registrando presença ou ausência.

## Atividade 2: CRUD para Eventos
1. Implemente a funcionalidade para criar novos eventos.
2. Liste todos os eventos cadastrados.
3. Atualize informações de um evento existente.
4. Exclua eventos do banco de dados.

## Atividade 3: CRUD para Convidados
1. Implemente a funcionalidade para adicionar novos convidados.
2. Liste todos os convidados cadastrados.
3. Atualize informações de um convidado existente.
4. Exclua convidados do banco de dados.

## Atividade 4: Registro de Presenças
1. Crie uma funcionalidade para associar convidados a eventos.
2. Registre a presença ou ausência de um convidado em um evento.
3. Liste os convidados de um evento com suas respectivas presenças/ausências.

## Atividade 5: Relatórios
1. Gere um relatório de todos os eventos com a lista de convidados e suas presenças/ausências.
2. Gere um relatório de um convidado específico, mostrando os eventos que ele participou e seu status de presença.

## Atividade 6: Testes e Validação
1. Teste todas as funcionalidades implementadas.
2. Valide os dados inseridos, como evitar duplicação de convidados ou eventos.
3. Garanta que as relações entre eventos, convidados e presenças estejam consistentes.

## Dicas Gerais
- Use boas práticas de modelagem de banco de dados, como normalização.
- Certifique-se de que as tabelas possuem chaves primárias e estrangeiras adequadas.
- Utilize transações para garantir a integridade dos dados ao realizar operações complexas.
