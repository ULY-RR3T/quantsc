import pandas as pd

import yfinance as yf
import yahoo_fin.stock_info as si
#http://theautomatic.net/yahoo_fin-documentation/
#http://theautomatic.net/yahoo_fin-documentation/#methods
from qsc.core.timeseries import TimeSeries


class Stock(TimeSeries):
    def __init__(self, ticker=None,start=None,end=None,interval='1d', data=None):
        if data:
            self.ticker = ticker
        else:
            if interval is not None:
                self.interval = self.is_valid_interval(interval)
            self.ticker = ticker
            super().__init__(data=ticker,start=start,end=end,interval=interval)
        self.indicators = dict()


    def getIndicators(self):
        return self.indicators

    def is_valid_interval(self, period):
        valid_period = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']
        if period in valid_period:
            return period
        else:
            raise("Interval must be one of '1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'!")
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

    def __add__(self, other):
        if isinstance(other, Stock):
            return self.data + other.data
        elif isinstance(other, TimeSeries):
            return self.data + other
        else:
            raise Exception("Second object in addition is not an instance of TimeSeries or Stock.")

    def __sub__(self, other):
        if isinstance(other, Stock):
            return self.data - other.data
        elif isinstance(other, TimeSeries):
            return self.data - other
        else:
            raise Exception("Second object in subtraction is not an instance of TimeSeries or Stock.")

    def __mul__(self, other):
        if isinstance(other, Stock):
            return self.data * other.data
        elif isinstance(other, TimeSeries):
            return self.data * other
        else:
            raise Exception("Second object in multiplication is not an instance of TimeSeries or Stock.")