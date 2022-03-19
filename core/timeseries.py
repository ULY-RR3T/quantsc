import pandas as pd

class TimeSeries:
    def __init__(self,data=None,link=None,nan=None):
        if data is not None:
            self.load_data(data)
        elif link is not None:
            tmp_data = pd.read_csv(link)
            self.load_data(tmp_data)

    def load_data(self,data):
        # If the index of data is string, change the format to datetime
        self.data = data

        #

    def integrity_check(self,data):
        if not isinstance(data,pd.core.series.Series):
            raise "Time series data must be pd.Series!"


