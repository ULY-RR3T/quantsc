import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

import yfinance as yf
import yahoo_fin.stock_info as si
import core.timeseries as TimeSeries
#http://theautomatic.net/yahoo_fin-documentation/
#http://theautomatic.net/yahoo_fin-documentation/#methods

class Stock(TimeSeries):
    def __init__(self, ticker=None, data=None,date_range=None, freq=None):

    if data:
            TimeSeries.__init__(data=data)
        else:
            # Use yfinance to fetch data
            TimeSeries.__init__(ticker=ticker,date_range=date_range,freq=freq)
            self.ticker = ticker
            if freq is not None:
                self.period = self.is_valid_period(freq)

    def getIndicators(self):
        return self.indicators

    def is_valid_period(self, period):
        valid_period = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']
        if period in valid_period:
            return period
        else:
            return None

    def update_data(self, ticker, period = None):
        self.data = yf.download(ticker, period)
        self.indicators = dict()

    def get_data(self):
        return self.data

    def get_csv(self):
        return self.data.to_csv(self.ticker+'.csv')

    def get_earnings(self, ticker=None):  # , earnings_date: datetime):
        earning_data = si.get_earnings_history(self.ticker)
        df_eps = pd.DataFrame.from_dict(earning_data)
        eps_data = pd.DataFrame(df_eps["epsactual"])
        eps_data.index = df_eps["startdatetime"]
        self.indicators["earning"] = eps_data
        return self.indicators["earning"]

    def get_epsestimate(self):
        earning_data = si.get_earnings_history(self.ticker)
        df_eps = pd.DataFrame.from_dict(earning_data)
        eps_data = df_eps["epsestimate"]
        eps_data.index = df_eps["startdatetime"]
        self.indicators["epsestimate"] = eps_data
        return self.indicators["epsestimate"]

    def get_epsactual(self):
        return self.get_earnings()

    def get_epssurprisepct(self):
        earning_data = si.get_earnings_history(self.ticker)
        df_eps = pd.DataFrame.from_dict(earning_data)
        eps_data = df_eps["epssurprisepct"]
        eps_data.index = df_eps["startdatetime"]
        self.indicators["epssurprisepct"] = eps_data
        return self.indicators["epssurprisepct"]

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

    def dividends(self): # can have specified date for onwards
        return si.get_dividends(self.ticker)



