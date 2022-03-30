import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

class TimeSeries:
    def __init__(self,data=None,link=None,nan=None):
        if data is not None:
            self.load_data(data)
        elif link is not None:
            tmp_data = pd.read_csv(link)
            self.load_data(tmp_data)
        self.indicators = None

    def __str__(self):
        pass

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
        if type(data).__module__ == np.__name__:
            if data.shape[1] == 1:
                self.data = pd.Series(data=data,index=list(range(len(data))) + 1)
            elif data.shape[1] == 2:
                self.data = pd.Series(data=data[1],index=data[1])
            return

        if isinstance(data,dict):
            pass

        if isinstance(data,pd.Series):
            self.data = data
            return


        # If the index of data is string, change the format to datetime
        if isinstance(data, str):
            # Check if data is a filename
            if data[-4:] == ".csv":
                df  = pd.from_csv(str,sep = delim)
                df_index = df.index
                df.data = pd.Series(data = df.iloc[0,:].tolist(),index=df_index)
                iteritems = df.iteritems()
                next(iteritems)
                for (column_name,column_data) in df.iteritems():
                    self.indicators.append(pd.Series(data=column_data,index=df_index,name=column_name))
            if data[-4:] == ".txt":
                pass



            # Else, data is a string representing the time series

        self.data = data

        # Sort the time series data by index
        # If index is None, raise exception

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
        if not plot_indicator:
            plt.plot(self.data)
        else:
            if style='together':
                plt.subplot(1,2,1)



    def to_string(self):
        return self.__str__(self)

