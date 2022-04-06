import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

import yfinance as yf

import yahoo_fin.stock_info as si
#http://theautomatic.net/yahoo_fin-documentation/
#http://theautomatic.net/yahoo_fin-documentation/#methods

class Stock:
    def __init__(self, ticker, data=None, period=None):
        self.ticker = ticker
        if period is not None:
            self.period = self.is_valid_period(period)
        if data is not None:
            self.data = data
        elif data is None:
            self.data = yf.download(ticker, period)
        self.indicators = dict()

    def is_valid_period(self, period):
        valid_period = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']
        if period in valid_period:
            return period
        else:
            return None

    def update_data(self, ticker, period = None):
        self.data = yf.download(ticker, period)

    def get_data(self):
        return self.data

    def get_csv(self):
        return self.data.to_csv(self.ticker+'.csv')

    def get_earnings(self, ticker): #, earnings_date: datetime):
        #get earning_history (no specified date)

        stock_earning_history = si.get_earnings_history(self.ticker)
        self.indicators["earnings"].append(stock_earning_history)
        return self.indicators["earnings"]
        #frame = pd.DataFrame.from_dict(stock_earning_history)
        #return frame.plot(x="startdatetime", y="espactual")

    def balance_sheet(self, yearly = True):
        self.indicators["balance_sheet"] = si.get_balance_sheet(self.ticker, yearly)
        return self.indicators["balance_sheet"]

    def cash_flow(self, yearly = True):
        self.indicators["cash_flow"] = si.get_cash_flow(self.ticker, yearly)
        return self.indicators["cash_flow"]

    def income_statement(self, yearly = True):
        self.indicators["income_statement"] = si.get_income_statement(self.ticker, yearly)
        return self.indicators["income_statement"]

    def next_earnings_date(self):
        return si.get_next_earnings_date(self.ticker)

    def dividends(self) # can have specified date for onwards
        return si.get_dividends(self.ticker)



