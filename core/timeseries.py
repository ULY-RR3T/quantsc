import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import statsmodels as sm

import statsmodels.api as sm
from scipy import stats
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from pandas import DataFrame
import yfinance as yf

class TimeSeries:
    def __init__(self, data=None, start=None, end=None, interval=None, delim=',',nan=None):
        self.indicators = dict()
        self.data = None
        if isinstance(data,str):
            if not('.csv' in data or '.txt' in data):
                self.data = yf.download(data, start=start, end=end, interval=interval)
            else:
                self.load_data(data,delim=delim)

    def __str__(self):
        if self.data is None:
            return ""
        else:
            return self.data.to_string()

    def __dict__(self):
        pass

    def load_data(self,data,delim=',',indicator=False):
        """Loads the input data into the timeseries object

        :param data: dict, array-like, pd.Series
        :return:
        """
        if isinstance(data,list):
            try:
                data = np.array(data)
            except:
                raise "Can't convert list to string!"

        # If the data is an array, default to using array index as time series index
        elif type(data).__module__ == np.__name__:
            if data.shape[1] == 1:
                self.data = pd.Series(data=data,index=list(range(len(data))) + 1)
            elif data.shape[1] == 2:
                self.data = pd.Series(data=data[:,1],index=data[:,0])
            return

        elif isinstance(data,dict):
            pass

        elif isinstance(data,pd.Series):
            self.data = data
            return

        # If the index of data is string, change the format to datetime
        elif isinstance(data,pd.DataFrame):
            series_data = data.iloc[:,0]
            self.data = pd.Series(data = series_data,index=data.index)
            for i in range(1,data.shape[1]):
                indicator_name = data.columns[i]
                self.indicators[indicator_name] = data.iloc[:,i]
            return

        elif isinstance(data, str):
            # Check if data is a filename
            if ".csv" in data:
                df = pd.read_csv(data,sep = delim,header=None,index_col=0)
                df.columns.name = None
                self.load_data(df)
            elif ".txt" in data:
                pass
            return

            # Else, data is a string representing the time series

        raise "Only numpy arrays, pandas Series, and csv files are supported!"

        # Sort the time series data by index
        # If index is None, raise exception
    @staticmethod
    def check_integrity(self, data=None):
        """Checks if the given data is a valid time series, raise exception if data is not a valid time series

        :param data:
        :return:
        """
        if data is None:
            data = self.data
        if not isinstance(data,pd.core.series.Series):
            raise "Time series data must be pd.Series!"

        ## Checks if all the indicies are in chronological order
        if not all(data.index[i] <= data.index[i+1] for i in range(len(data.index) - 1)):
            raise "Time series are not in chronological order!"

        if not isinstance(self.data.index,datetime.date):
            raise "Index of the series must be datetime!"


    def plot(self,figsize=(6,8),xlabel=None,ylabel=None,title=None,plot_indicator=False,style=None):
        plt.figure(figsize=figsize)
        n = len(self.indicators) + 1
        if not plot_indicator:
            plt.plot(self.data)
            plt.show()
        else:
            if style=='together':
                for i in range(n):
                    plt.plot(self.indicators)
            else:
                col  = n // 5
                row = 5
                fig,axs = plt.subplots(row,col)
                for i in range(n):
                    axs[i].plot(n)
                    axs.title(self.indicators[i].name)
                    axs.xlabel(self.indicators[i].name)
                    plt.subplot(1,2,1)


    def to_string(self,indicators=False):
        rslt_string = ""
        if self.data is not None:
           rslt_string += self.data.to_string()

        if isinstance(indicators,bool):
            if indicators:
                for name,indicator in self.indicators.items():
                    rslt_string += (str(self.indicators[name]) + "\n")
            else:
                return self.__str__()
        elif isinstance(indicators,str):
            return self.indicators[indicators] + "\n"
        else:
            for indicator in indicators:
                if indicator in self.indicators.keys():
                    rslt_string += str(self.indicators[indicator]) + "\n"

        return rslt_string

    def take_diff(self, d):
        df = pd.DataFrame(self.data.values)
        for i in range(d):
            df = df.diff()
        plt.plot(df)
        plt.show()

    def take_autocorrelation(self, d):
        df = pd.DataFrame(self.data.values)
        for i in range(d):
            df = df.diff()
        plot_acf(df.dropna())
        plt.show()

    def take_partial_autocorrelation(self, d):
        df = pd.DataFrame(self.data.values)
        for i in range(d):
            df = df.diff()
        plot_pacf(df.dropna())
        plt.show()

    def model_arima(self, p, d, q, plotResiduals = True, getSummary = True, ):
        df = pd.DataFrame(self.data.values)
        model = ARIMA(df, order=(p, d, q))
        model_fit = model.fit()
        if getSummary:
            print(model_fit.summary())
        residuals = DataFrame(model_fit.resid)
        if plotResiduals:
            fig, ax = plt.subplots(1, 2)
            residuals.plot(title="Residuals", ax=ax[0])
            residuals.plot(kind='kde', title='Density', ax=ax[1])
            plt.show()
        return model

        def __add__(self, other):
            if isinstance(other, TimeSeries):
                newData = (self.data + other.data).dropna()
                retVal = TimeSeries(newData)
                return retVal
            else:
                raise Exception("Second object in addition is not an instance of TimeSeries.")

        def __sub__(self, other):
            if isinstance(other, TimeSeries):
                newData = (self.data - other.data).dropna()
                retVal = TimeSeries(newData)
                return retVal
            else:
                raise Exception("Second object in subtraction is not an instance of TimeSeries.")

        def __mul__(self, other):
            if isinstance(other, TimeSeries):
                newData = (self.data * other.data).dropna()
                retVal = TimeSeries(newData)
                return retVal
            else:
                raise Exception("Second object in multiplication is not an instance of TimeSeries.")

                #for name,indicator_data in self.indicators.items():
    # def exp(self):

    """
    def plot_data(self,indicators=False):
        if indicators:
            total_indicators = len(indicators)
            fig,axs = plt.subplots(total_indicators // 2, 2)
            for idx,key,value in enumerate(indicators):
                axs[i]
    """
    # def plot(self,indicators=False):
    #     if indicators:
    #         total_indicators = len(indicators)
    #         fig,axs = plt.subplots(total_indicators // 2, 2)
    #         for idx,key,value in enumerate(indicators):
    #             axs[i]
