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
        # If the index of data is string, change the format to datetime
        self.data = data

        # Sort the time series data by index
        # If index is None, raise exception

    def integrity_check(self,data=None):
        if data is None:
            data = self.data
        if not isinstance(data,pd.core.series.Series):
            raise "Time series data must be pd.Series!"

    def plot(self):
        plt.figure()
        if self.data is not None:
            plt.plot(self.data)

    def to_string(self):
        return self.__str__(self)

