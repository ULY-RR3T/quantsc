from core.timeseries import TimeSeries
import testutil as util
import pandas as pd
from core.stock import Stock
import os
class testTimeSeries():

    def testEmptyInitialize(self):
        ts = TimeSeries()
        print(ts)

    def testLoadSeriesNoIndicatorSeries(self):
        pd_series = util.get_random_pandas_series(size=3)
        ts = TimeSeries(pd_series)
        print(ts)

    def testLoadSeriesNoIndicatorNumpy(self):
        np_ndarray = util.get_random_numpy_ndarray(size=3)
        ts = TimeSeries(np_ndarray)
        print(ts)

    def testLoadSeriesFromCSV(self,file=None):
        if file is None:
            file = "static/test_data.csv"
        # print(pd.read_csv(file,header=None,index_col=0))
        ts = TimeSeries(data=file)
        print(ts)

    def testAdd(self):
        a = Stock("AAPL").get_data()
        b = Stock("GE").get_data()
        c = a + b
        c.plot()


if __name__ == "__main__":
    test = testTimeSeries()
    test.testLoadSeriesFromCSV()
    # test.testInitialize()
    # test.testLoadSeriesNoIndicator()
    # test.testLoadSeriesNoIndicatorNumpy()
