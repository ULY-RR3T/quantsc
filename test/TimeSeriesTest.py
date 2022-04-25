import testutil as util
import quantsc as qsc


# from core.stock import Stock
class TimeSeriesTest():

    # def testLoadLibrary(self):
    #     assert(isinstance(qsc.TimeSeries()))

    def testEmptyInitialize(self):
        ts = qsc.TimeSeries()
        print(ts)

    def testLoadSeriesNoIndicatorSeries(self):
        pd_series = util.get_random_pandas_series(size=3)
        ts = qsc.TimeSeries(pd_series)
        print(ts)

    def testLoadSeriesNoIndicatorNumpy(self):
        np_ndarray = util.get_random_numpy_ndarray(size=3)
        ts = qsc.TimeSeries(np_ndarray)
        print(ts)

    def testLoadSeriesFromCSV(self,file=None):
        if file is None:
            file = "static/test_data.csv"
        # print(pd.read_csv(file,header=None,index_col=0))
        ts = qsc.TimeSeries(data=file)
        print(ts)

    def testLoadSeriesFromTiker(self,ticker):
        ts = qsc.TimeSeries(ticker)
        print(ts)
        qsc.TimeSeries.check_integrity(ts)


if __name__ == "__main__":
    test = TimeSeriesTest()
    # test.testLoadSeriesFromCSV()
    # test.testInitialize()
    # test.testLoadSeriesNoIndicator()
    # test.testLoadSeriesNoIndicatorNumpy()
    # test.testLoadSeriesFromTiker("GE")