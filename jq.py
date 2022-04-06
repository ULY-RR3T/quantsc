import pandas as pd
import matplotlib.pyplot as plt
import datetime

import yahoo_fin.stock_info as si
#http://theautomatic.net/yahoo_fin-documentation/
#http://theautomatic.net/yahoo_fin-documentation/#methods


def QSC.Stock.plot_earnings(stock: str): #, earnings_date: datetime):
    #get earning_history (no specified date)

    stock_earning_history = si.get_earnings_history(stock)
    frame = pd.DataFrame.from_dict(stock_earning_history)
    return frame.plot(x="startdatetime", y="espactual")

def QSC.Stock.balance_sheet(stock: str, yearly = True):
    return si.get_balance_sheet(stock, yearly)

def QSC.Stock.cash_flow(stock: str, yearly = True):
    return si.get_cash_flow(stock, yearly)

def QSC.Stock.income_statement(stock: str, yearly = True):
    return si.get_income_statement(stock, yearly)

def QSC.Stock.next_earnings_date(stock: str):
    return si.get_next_earnings_date(stock)

def QSC.Stock.dividends(stock: str) # can have specified date for onwards
    return si.get_dividends(stock)



