import pandas as pd
import matplotlib.pyplot as plt

class TimeSeries:
    def __init__(self,data=None,link=None,nan=None):
        if data is not None:
            self.load_data(data)
        elif link is not None:
            tmp_data = pd.read_csv(link)
            self.load_data(tmp_data)

    def __str__(self):
        pass

    def __dict__(self):
        pass

    def load_data(self,data):
        """Loads the input data into the timeseries object

        :param data:
        :return:
        """
        # If the data is an array, default to using array index as time series index
        if isinstance(data,np.array()):
            self.data = pd.Series(data=data,index=list(range(len(data))) + 1)
            return

        # If the index of data is string, change the format to datetime
        if isinstance(data, String):
            # Check if data is a filename
            if data[-4:] == ".csv" or data[-4:] == ".txt":


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




    def plot(self):
        plt.figure()
        if self.data is not None:
            plt.plot(self.data)

    def to_string(self):
        return self.__str__(self)

