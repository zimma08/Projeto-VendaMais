# ADR-001 - Escolha da biblioteca de acesso ao banco de dados

## Contexto

Foi desenvolvida uma Prova de Conceito (PoC) em Python utilizando Azure Functions para comparar empiricamente o desempenho das bibliotecas PYODBC e SQLAlchemy no acesso ao banco de dados SQL Server.

O objetivo foi medir o tempo necessário para executar uma consulta SQL e carregar todos os registros retornados para memória.


## Opções Avaliadas

### PYODBC

Biblioteca que realiza acesso direto ao SQL Server através do driver ODBC.

### SQLAlchemy

Biblioteca de acesso a banco de dados que fornece recursos adicionais como abstração de consultas e gerenciamento de conexões.

## Teste Realizado

A comparação foi realizada utilizando:

- Mesmo banco de dados
- Mesma tabela
- Mesmo SELECT
- Duas execuções para cada biblioteca
- Cálculo do tempo médio de execução

Consulta utilizada:

```sql
SELECT * FROM erp.estoque_movimentacao
```

Quantidade de registros retornados:

```text
313 registros
```

## Resultados

| Biblioteca | Execução 1 | Execução 2 | Média |
|------------|------------|------------|--------|
| PYODBC | 0.5403s | 0.4842s | 0.5122s |
| SQLAlchemy | 0.6551s | 0.0428s | 0.3489s |

## Decisão

A biblioteca SQLAlchemy foi escolhida como a melhor alternativa para o cenário analisado.

## Justificativa

Nos testes realizados, o SQLAlchemy apresentou menor tempo médio de execução quando comparado ao PYODBC.

| Biblioteca | Tempo Médio |
|------------|-------------|
| PYODBC | 0.5122s |
| SQLAlchemy | 0.3489s |

Além do desempenho observado, o SQLAlchemy oferece recursos como gerenciamento de conexões e suporte a ORM, facilitando o desenvolvimento e a manutenção do código.

## Conclusão

Com base nos resultados obtidos na PoC, conclui-se que o SQLAlchemy apresentou o menor tempo médio de execução para o cenário avaliado, sendo a alternativa recomendada para novos desenvolvimentos.