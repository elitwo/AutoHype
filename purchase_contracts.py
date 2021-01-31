from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
import math

import config

def buy(ticker):
    client = Client(config.api_key, config.api_secret)

    price = float(client.get_symbol_ticker(symbol=ticker)['price'])
    
    trade_quantity = config.trade_size / price
    
    symbol_info = client.get_symbol_info(ticker)
    step_size = 0.0
    for f in symbol_info['filters']:
        if f['filterType'] == 'LOT_SIZE':
            step_size = float(f['stepSize'])

    precision = int(round(-math.log(step_size, 10), 0))
    
    if ticker == "BTCUSDT":
        precision = 3 #idk wtf is going on, but the normal precision doesn't work with BTC's price rn

    trade_quantity = "{:0.0{}f}".format(trade_quantity, precision)

    print("BUYING: " + str(trade_quantity) + " of " + ticker)
    client.futures_create_order(symbol=ticker, side='BUY', type='MARKET', quantity=trade_quantity)

    if config.cash_out_percent:
        if ticker == "BTCUSDT":
            take_profit = round(price + (price * (config.cash_out_percent/100)))
        elif ticker == "DOGEUSDT": # these need to be hard set for some reason.
            take_profit = round(price + (price * (config.cash_out_percent/100)), 6)
        else:
            take_profit = round(price + (price * (config.cash_out_percent/100)), precision)

        print("with TP: " + str(take_profit))
        client.futures_create_order(symbol=ticker, side='SELL', type='TAKE_PROFIT_MARKET', quantity=trade_quantity, stopPrice=take_profit)

