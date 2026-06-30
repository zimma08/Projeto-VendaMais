import azure.functions as func
import logging
import os
import pyodbc

bp = func.Blueprint()


@bp.timer_trigger(schedule="0 */1 * * * *", arg_name="timer", run_on_startup=False)
def extract_pedido(timer: func.TimerRequest) -> None:
    
    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")
    sql_server_dest = os.getenv("SQL_SERVER_DEST")
    sql_database_dest = os.getenv("SQL_DATABASE_DEST")
    sql_user_dest = os.getenv("SQL_USER_DEST")
    sql_pass_dest = os.getenv("SQL_PASSWORD_DEST")


    logging.info(f"servidor: {sql_server},  banco: {sql_database}, usuario:{sql_user}, senha: {sql_pass} ...")


    # Configura a string de conexão para o banco de dados SQL Server
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={sql_server};"
        f"DATABASE={sql_database};"
        f"UID={sql_user};"
        f"PWD={sql_pass};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    conn_str_dest = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={sql_server_dest};"
        f"DATABASE={sql_database_dest};"
        f"UID={sql_user_dest};"
        f"PWD={sql_pass_dest};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

   
    try:
        # Estabelece a conexão com o banco de dados usando pyodbc
        with pyodbc.connect(conn_str) as conn:
            # Cria um cursor para executar a consulta   
            cursor = conn.cursor()
            
            query = "select * from erp.pedido"

            # Executa a consulta SQL
            cursor.execute(query)

            # Busca todos os resultados da consulta
            rows = cursor.fetchall()

            with pyodbc.connect(conn_str_dest) as conn_dest:
                cursor_dest = conn_dest.cursor()

                cursor_dest.execute("DELETE FROM erp.pedido")

                for row in rows:
                    cursor_dest.execute(
                        """
                        INSERT INTO erp.pedido
                        (
                            id_pedido,
                            nr_pedido,
                            id_cliente,
                            id_representante,
                            id_regiao,
                            dt_emissao,
                            dt_faturamento,
                            ds_status_pedido,
                            vl_bruto,
                            vl_desconto,
                            vl_liquido,
                            ds_observacao,
                            dt_inclusao,
                            dt_atualizacao,
                            nm_sistema_origem,
                            cd_registro_origem
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        row.id_pedido,
                        row.nr_pedido,
                        row.id_cliente,
                        row.id_representante,
                        row.id_regiao,
                        row.dt_emissao,
                        row.dt_faturamento,
                        row.ds_status_pedido,
                        row.vl_bruto,
                        row.vl_desconto,
                        row.vl_liquido,
                        row.ds_observacao,
                        row.dt_inclusao,
                        row.dt_atualizacao,
                        row.nm_sistema_origem,
                        row.cd_registro_origem
                    )

                conn_dest.commit()

            logging.info(
                f"{len(rows)} registros inseridos em pedido"
            )

    except Exception as e:
        logging.error(f"Erro ao ler erp.pedido: {str(e)}")
        raise
