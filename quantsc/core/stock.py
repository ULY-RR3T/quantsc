import pandas as pd
import yfinance as yf
import yahoo_fin.stock_info as si
#http://theautomatic.net/yahoo_fin-documentation/
#http://theautomatic.net/yahoo_fin-documentation/#methods
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import quantsc.config as config
from quantsc.core.timeseries import TimeSeries

class Stock(TimeSeries):
    def __init__(self, ticker=None,start=None,end=None,interval='1d', data=None,name=None):
        if data:
            if name is not None:
                self.name = name
                self.ticker = None
            else:
                self.name = "Custom Stock"
        else:
            if interval is not None:
                self.interval = self.is_valid_interval(interval)
            self.ticker = ticker
            self.name = ticker
            stock_data = yf.download(ticker,start=start,end=end,interval=interval)
            series = pd.Series(data=stock_data['Open'],index=stock_data.index)
            super().__init__(series)
            self.open = stock_data['Open']
            self.close = stock_data['Close']
            self.low = stock_data['Low']
            self.high = stock_data['High']
            self.dates = stock_data.index
        self.indicators = dict()
        self.diff_count = 0

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

    def len(self):
        return super().__len__()

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

    def plot(self,backend=None,type='candle'):
        if backend is None:
            backend = config.config['plot_backend']
        if backend == "matplotlib":
            plt.plot(self.data)
            plt.show()
        elif backend == "plotly":
            if type == "candle":
                fig = go.Figure(data=[go.Candlestick(x=self.dates,
                        open=self.open,
                        high=self.high,
                        low=self.low,
                        close=self.close)])
            elif type == "line":
                fig = px.line(self.data)
            else:
                raise("type can only be 'candle' or 'line'")
            fig.show()
        else:
            raise("Backend must be either 'plotly' or 'matplotlib!'")

    # def sort_values(self, column = "Open"):
        #df = pd.DataFrame()
        #self.data

    # ""
    # def pairwise_sort(self):

    # def sort_index(self):
    # """
    # Reminder: Sort all self.data(default to 'open') self.open,self.close,self.high,self.low
    # """
    def diff(self):
        pass
    def covariance(self):
        """
        def test_method(self,a,b,c,d):
        we provide a description to the function test_method

       :param a:
       :param b:
       :param c:
       :param d:
       :return:
       """
        pass

