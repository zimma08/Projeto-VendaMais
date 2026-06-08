import azure.functions as func
import logging
import os
import pyodbc
import time

from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

bp = func.Blueprint()


@bp.timer_trigger(
    schedule="0 0 6 * * *",
    arg_name="timer",
    run_on_startup=False
)
def benchmark_database(timer: func.TimerRequest) -> None:

    logging.info(
        "INICIANDO POC DE COMPARAÇÃO PYODBC X SQLALCHEMY"
    )

    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")

    logging.info(
        f"servidor: {sql_server}, "
        f"banco: {sql_database}, "
        f"usuario: {sql_user}"
    )

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

    query = "SELECT * FROM erp.estoque_movimentacao"

    try:

        logging.info("========== TESTE PYODBC ==========")

        tempos_pyodbc = []

        for i in range(2):

            inicio = time.perf_counter()

            with pyodbc.connect(conn_str) as conn:

                cursor = conn.cursor()

                cursor.execute(query)

                rows = cursor.fetchall()

            fim = time.perf_counter()

            tempo = fim - inicio

            tempos_pyodbc.append(tempo)

            logging.info(
                f"PYODBC - Execução {i + 1}: "
                f"{tempo:.4f}s "
                f"- Registros: {len(rows)}"
            )

        media_pyodbc = sum(tempos_pyodbc) / len(tempos_pyodbc)

        logging.info(
            f"PYODBC - Média: {media_pyodbc:.4f}s"
        )

    except Exception as e:

        logging.error(
            f"Erro no teste PYODBC: {str(e)}"
        )

        raise

    try:

        logging.info("========== TESTE SQLALCHEMY ==========")

        tempos_sqlalchemy = []

        params = quote_plus(conn_str)

        engine = create_engine(
            f"mssql+pyodbc:///?odbc_connect={params}"
        )

        for i in range(2):

            inicio = time.perf_counter()

            with engine.connect() as conn:

                result = conn.execute(text(query))

                rows = result.fetchall()

            fim = time.perf_counter()

            tempo = fim - inicio

            tempos_sqlalchemy.append(tempo)

            logging.info(
                f"SQLALCHEMY - Execução {i + 1}: "
                f"{tempo:.4f}s "
                f"- Registros: {len(rows)}"
            )

        media_sqlalchemy = (
            sum(tempos_sqlalchemy)
            / len(tempos_sqlalchemy)
        )

        engine.dispose()

        logging.info(
            f"SQLALCHEMY - Média: "
            f"{media_sqlalchemy:.4f}s"
        )

    except Exception as e:

        logging.error(
            f"Erro no teste SQLALCHEMY: {str(e)}"
        )

        raise

    logging.info("========== RESULTADO FINAL ==========")

    logging.info(
        f"PYODBC Média: {media_pyodbc:.4f}s"
    )

    logging.info(
        f"SQLALCHEMY Média: {media_sqlalchemy:.4f}s"
    )