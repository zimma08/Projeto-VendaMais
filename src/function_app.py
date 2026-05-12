import logging
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_categoria_produto(myTimer: func.TimerRequest) -> None:
    logging.info('tabela categoria_produto.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_cliente(myTimer: func.TimerRequest) -> None:
    logging.info('tabela cliente.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_entrega(myTimer: func.TimerRequest) -> None:
    logging.info('tabela entrega.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_estoque_movimentacao(myTimer: func.TimerRequest) -> None:
    logging.info('tabela estoque_movimentação.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_estoque_saldo(myTimer: func.TimerRequest) -> None:
    logging.info('tabela estoque_saldo.')


@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_pedido(myTimer: func.TimerRequest) -> None:
    logging.info('tabela pedido.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_pedido_item(myTimer: func.TimerRequest) -> None:
    logging.info('tabela pedido_item.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_produto(myTimer: func.TimerRequest) -> None:
    logging.info('tabela produto.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_regiao(myTimer: func.TimerRequest) -> None:
    logging.info('tabela regiao.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_representante(myTimer: func.TimerRequest) -> None:
    logging.info('tabela representante.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_titulo_receber(myTimer: func.TimerRequest) -> None:
    logging.info('tabela titulo_receber.')

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_transportadora(myTimer: func.TimerRequest) -> None:
    logging.info('tabela transportadora.')
